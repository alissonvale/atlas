#!/usr/bin/env python3
"""Summarize a HygiaTech simulation month from historical weeks."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "simulation" / "data"


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"missing file: {path}")
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise SystemExit(f"expected YAML mapping: {path}")
    return data


def catalog(filename: str, key: str, id_field: str) -> dict[str, dict[str, Any]]:
    data = load_yaml(DATA_DIR / filename)
    return {item[id_field]: item for item in data[key]}


def label(items: dict[str, dict[str, Any]], key: str) -> str:
    item = items.get(key)
    return item.get("name", key) if item else key


def print_counter(title: str, counter: Counter[str], labels: dict[str, dict[str, Any]] | None = None, limit: int | None = None) -> None:
    print(f"\n{title}")
    entries = counter.most_common(limit)
    if not entries:
        print("  none")
        return
    for key, count in entries:
        name = label(labels, key) if labels else key
        print(f"  {name}: {count}")


def final_statuses(tickets: list[dict[str, Any]], events: list[dict[str, Any]]) -> dict[str, str]:
    events_by_ticket: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        events_by_ticket[event["ticket_id"]].append(event)

    result = {}
    for ticket in tickets:
        status = ticket.get("status", "unknown")
        for event in sorted(events_by_ticket.get(ticket["id"], []), key=lambda item: item["occurred_at"]):
            if event.get("to_status"):
                status = event["to_status"]
        result[ticket["id"]] = status
    return result


def load_week(week: str) -> tuple[dict[str, Any], dict[str, Any]]:
    return (
        load_yaml(DATA_DIR / f"tickets-{week}.yaml"),
        load_yaml(DATA_DIR / f"events-{week}.yaml"),
    )


def summarize(weeks: list[str]) -> None:
    hospitals = catalog("hospitals.yaml", "hospitals", "id")
    modules = catalog("modules.yaml", "modules", "slug")
    demand_types = catalog("demand-types.yaml", "demand_types", "slug")
    teams = catalog("staff.yaml", "teams", "slug")

    all_tickets: list[dict[str, Any]] = []
    all_events: list[dict[str, Any]] = []
    week_ticket_counts: Counter[str] = Counter()
    week_event_counts: Counter[str] = Counter()

    for week in weeks:
        ticket_batch, event_batch = load_week(week)
        tickets = ticket_batch.get("tickets", [])
        events = event_batch.get("events", [])
        all_tickets.extend(tickets)
        all_events.extend(events)
        week_ticket_counts[week] = len(tickets)
        week_event_counts[week] = len(events)

    statuses = final_statuses(all_tickets, all_events)
    closed_statuses = {"closed", "support_resolved"}
    closed = [ticket for ticket in all_tickets if statuses[ticket["id"]] in closed_statuses]
    open_items = [ticket for ticket in all_tickets if statuses[ticket["id"]] not in closed_statuses]

    print("HygiaTech Atlas Monthly Summary")
    print("=" * 48)
    print(f"Weeks: {', '.join(weeks)}")
    print(f"Tickets: {len(all_tickets)}")
    print(f"Events: {len(all_events)}")
    print(f"Closed by timeline: {len(closed)}")
    print(f"Open / in progress by timeline: {len(open_items)}")

    print_counter("Tickets by week", week_ticket_counts)
    print_counter("Events by week", week_event_counts)
    print_counter("Volume by response system", Counter(ticket["response_system"] for ticket in all_tickets))
    print_counter("Volume by Atlas class", Counter(ticket["initial_atlas_class"] for ticket in all_tickets))
    print_counter("Top modules", Counter(ticket["module"] for ticket in all_tickets), modules, limit=8)
    print_counter("Top hospitals", Counter(ticket["hospital_id"] for ticket in all_tickets), hospitals, limit=8)
    print_counter("Technology load", Counter(ticket.get("primary_technology", "unknown") for ticket in all_tickets))
    print_counter("Demand types", Counter(ticket["demand_type"] for ticket in all_tickets), demand_types, limit=10)
    print_counter("Assigned teams", Counter(ticket["assigned_team"] for ticket in all_tickets), teams)
    print_counter("Final status by timeline", Counter(statuses.values()))

    mirror_events = [event for event in all_events if event.get("mirror_used") is True]
    s3_candidates = [event for event in all_events if event["event_type"] == "s3_candidate_created"]
    learning_reviews = [event for event in all_events if event["event_type"] == "learning_review_created"]
    low_evidence = [ticket for ticket in all_tickets if ticket.get("evidence_quality") == "baixa"]

    print("\nOperational signals")
    print(f"  Mirror interactions: {len(mirror_events)}")
    print(f"  S3 candidates created: {len(s3_candidates)}")
    print(f"  Learning reviews: {len(learning_reviews)}")
    print(f"  Low-evidence tickets: {len(low_evidence)}")

    delphi_count = Counter(ticket.get("primary_technology") for ticket in all_tickets).get("delphi_2007_datasnap", 0)
    csharp_count = Counter(ticket.get("primary_technology") for ticket in all_tickets).get("csharp_api", 0)
    s1_count = Counter(ticket["response_system"] for ticket in all_tickets).get("S1", 0)
    s2_count = Counter(ticket["response_system"] for ticket in all_tickets).get("S2", 0)
    s3_count = Counter(ticket["response_system"] for ticket in all_tickets).get("S3", 0)

    print("\nAtlas monthly reading")
    if delphi_count:
        print(f"  - Delphi 2007/DataSnap carried {delphi_count} tickets, confirming it as the central capacity constraint.")
    if csharp_count:
        print(f"  - C# API carried {csharp_count} tickets, mostly around integrations and diagnostic surfaces.")
    print(f"  - Pronto-atendimento pressure: {s1_count} S1 and {s2_count} S2 tickets crossed the month.")
    print(f"  - Adaptation material: {s3_count} S3 tickets and {len(s3_candidates)} S3-candidate events show support turning into learning.")
    if low_evidence:
        print(f"  - Evidence quality remains a triage risk in {len(low_evidence)} tickets, especially for lower-maturity hospitals.")
    if learning_reviews:
        print("  - Weekly Learning Reviews exist in the data. The monthly report can now consolidate recurring patterns.")

    print("\nSuggested monthly actions")
    print("  - Protect Delphi capacity explicitly in S3 planning.")
    print("  - Convert recurring faturamento and DataSnap observability items into a visible S3 cycle.")
    print("  - Improve help desk evidence prompts for low-maturity hospitals.")
    print("  - Separate customer pressure from operational risk in financial/reporting requests.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize a HygiaTech simulation month")
    parser.add_argument("weeks", nargs="*", default=["week-01", "week-02", "week-03", "week-04"])
    args = parser.parse_args()
    summarize(args.weeks)


if __name__ == "__main__":
    main()
