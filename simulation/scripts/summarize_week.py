#!/usr/bin/env python3
"""Summarize a HygiaTech simulation week."""

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


def load_catalogs() -> dict[str, dict[str, Any]]:
    hospitals = load_yaml(DATA_DIR / "hospitals.yaml")["hospitals"]
    modules = load_yaml(DATA_DIR / "modules.yaml")["modules"]
    staff_data = load_yaml(DATA_DIR / "staff.yaml")
    demand_types = load_yaml(DATA_DIR / "demand-types.yaml")["demand_types"]

    staff = staff_data["staff"]
    teams = staff_data["teams"]

    return {
        "hospitals": {item["id"]: item for item in hospitals},
        "modules": {item["slug"]: item for item in modules},
        "staff": {item["id"]: item for item in staff},
        "teams": {item["slug"]: item for item in teams},
        "demand_types": {item["slug"]: item for item in demand_types},
    }


def label(mapping: dict[str, dict[str, Any]], key: str, fallback: str | None = None) -> str:
    item = mapping.get(key)
    if not item:
        return fallback or key
    return item.get("name", key)


def print_counter(title: str, counter: Counter[str], *, labels: dict[str, dict[str, Any]] | None = None) -> None:
    print(f"\n{title}")
    if not counter:
        print("  none")
        return
    for key, count in counter.most_common():
        name = label(labels, key) if labels else key
        print(f"  {name}: {count}")


def summarize(week: str) -> None:
    catalogs = load_catalogs()
    tickets_file = DATA_DIR / f"tickets-{week}.yaml"
    events_file = DATA_DIR / f"events-{week}.yaml"

    ticket_batch = load_yaml(tickets_file)
    event_batch = load_yaml(events_file)

    tickets = ticket_batch.get("tickets", [])
    events = event_batch.get("events", [])
    tickets_by_id = {ticket["id"]: ticket for ticket in tickets}

    events_by_ticket: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        events_by_ticket[event["ticket_id"]].append(event)

    print(f"HygiaTech Atlas Weekly Summary: {week}")
    print("=" * 48)
    print(ticket_batch.get("batch", {}).get("name", "unnamed batch"))
    period = ticket_batch.get("batch", {}).get("period", {})
    if period:
        print(f"Period: {period.get('start')} to {period.get('end')}")
    print(f"Tickets: {len(tickets)}")
    print(f"Events: {len(events)}")

    print_counter("Volume by response system", Counter(t["response_system"] for t in tickets))
    print_counter("Volume by Atlas class", Counter(t["initial_atlas_class"] for t in tickets))
    print_counter("Volume by module", Counter(t["module"] for t in tickets), labels=catalogs["modules"])
    print_counter("Volume by hospital", Counter(t["hospital_id"] for t in tickets), labels=catalogs["hospitals"])
    print_counter("Volume by technology", Counter(t.get("primary_technology", "unknown") for t in tickets))
    print_counter("Volume by demand type", Counter(t["demand_type"] for t in tickets), labels=catalogs["demand_types"])
    print_counter("Assigned teams", Counter(t["assigned_team"] for t in tickets), labels=catalogs["teams"])

    print_counter("Events by type", Counter(e["event_type"] for e in events))
    print_counter("Events by actor type", Counter(e["actor_type"] for e in events))

    mirror_events = [event for event in events if event.get("mirror_used") is True]
    print(f"\nMirror interactions: {len(mirror_events)}")
    for event in mirror_events:
        ticket = tickets_by_id.get(event["ticket_id"], {})
        print(f"  {event['ticket_id']}: {ticket.get('title', 'unknown ticket')}")
        print(f"    stage/event: {event.get('event_type')}")
        print(f"    output: {event.get('mirror_prompt_summary')}")

    s3_candidates = [event for event in events if event["event_type"] == "s3_candidate_created"]
    print(f"\nS3 candidates created: {len(s3_candidates)}")
    for event in s3_candidates:
        ticket = tickets_by_id.get(event["ticket_id"], {})
        print(f"  {event['ticket_id']}: {ticket.get('title', 'unknown ticket')}")
        print(f"    evidence: {event.get('evidence', event.get('summary'))}")

    learning_reviews = [event for event in events if event["event_type"] == "learning_review_created"]
    print(f"\nLearning reviews: {len(learning_reviews)}")
    for event in learning_reviews:
        print(f"  {event['occurred_at']}: {event['summary']}")
        if event.get("evidence"):
            print(f"    evidence: {event['evidence']}")

    final_status_by_ticket = {}
    for ticket_id, ticket_events in events_by_ticket.items():
        ordered = sorted(ticket_events, key=lambda event: event["occurred_at"])
        final_status = None
        for event in ordered:
            if event.get("to_status"):
                final_status = event["to_status"]
        if final_status:
            final_status_by_ticket[ticket_id] = final_status

    closed_statuses = {"closed", "support_resolved"}
    closed = [ticket for ticket in tickets if final_status_by_ticket.get(ticket["id"], ticket.get("status")) in closed_statuses]
    open_tickets = [ticket for ticket in tickets if final_status_by_ticket.get(ticket["id"], ticket.get("status")) not in closed_statuses]
    print(f"\nTicket status posture")
    print(f"  closed by timeline: {len(closed)}")
    print(f"  still open/in progress by timeline: {len(open_tickets)}")
    print_counter("Final status by timeline", Counter(final_status_by_ticket.get(ticket["id"], ticket.get("status")) for ticket in tickets))

    high_signal = []
    if Counter(t["primary_technology"] for t in tickets).get("delphi_2007_datasnap", 0) >= 8:
        high_signal.append("Delphi 2007/DataSnap dominates the week and should be treated as capacity risk.")
    if len(s3_candidates) >= 3:
        high_signal.append("The week generated multiple S3 candidates, which means support work is producing adaptation material.")
    weak_evidence = [ticket for ticket in tickets if ticket.get("evidence_quality") == "baixa"]
    if weak_evidence:
        high_signal.append(f"{len(weak_evidence)} tickets entered with low evidence quality, increasing identification risk.")
    if mirror_events:
        high_signal.append("Mirror is already useful at triage, qualification, and learning moments.")

    print("\nAtlas reading")
    if high_signal:
        for item in high_signal:
            print(f"  - {item}")
    else:
        print("  - No strong signal detected yet.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize a HygiaTech simulation week")
    parser.add_argument("week", help="week slug, for example week-01")
    args = parser.parse_args()
    summarize(args.week)


if __name__ == "__main__":
    main()
