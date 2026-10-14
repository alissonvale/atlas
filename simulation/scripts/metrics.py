#!/usr/bin/env python3
"""Atlas metrics for HygiaTech simulation data."""

from __future__ import annotations

import argparse
from collections import Counter

from simlib import all_week_slugs, events_by_ticket, label, load_catalogs, load_week, sle_state, stage_times


def summarize_week_metrics(week: str) -> dict:
    tickets_batch, events_batch = load_week(week)
    tickets = tickets_batch["tickets"]
    grouped = events_by_ticket(events_batch["events"])
    rows = []
    for ticket in tickets:
        ticket_events = grouped.get(ticket["id"], [])
        times = stage_times(ticket, ticket_events)
        rows.append({
            "id": ticket["id"],
            "system": ticket["response_system"],
            "module": ticket["module"],
            "technology": ticket.get("primary_technology", "unknown"),
            "evidence_quality": ticket.get("evidence_quality"),
            "sle": sle_state(ticket, ticket_events),
            **times,
        })
    return {"week": week, "rows": rows}


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute Atlas metrics")
    parser.add_argument("weeks", nargs="*", default=all_week_slugs(include_current=True))
    args = parser.parse_args()

    catalogs = load_catalogs()
    all_rows = []
    for week in args.weeks:
        data = summarize_week_metrics(week)
        all_rows.extend(data["rows"])
        print(f"\n{week}")
        print("-" * 32)
        print_counts(data["rows"])

    print("\nALL SELECTED WEEKS")
    print("=" * 32)
    print_counts(all_rows)
    print("\nSLE pulse by system")
    for system in ["S1", "S2", "S3", "suporte"]:
        rows = [row for row in all_rows if row["system"] == system]
        if not rows:
            continue
        print(f"  {system}: {dict(Counter(row['sle'] for row in rows))}")
    print("\nTop technology load")
    for key, count in Counter(row["technology"] for row in all_rows).most_common():
        print(f"  {key}: {count}")
    print("\nTop modules")
    for key, count in Counter(row["module"] for row in all_rows).most_common(8):
        print(f"  {label(catalogs['modules'], key)}: {count}")


def print_counts(rows: list[dict]) -> None:
    print(f"tickets: {len(rows)}")
    print(f"systems: {dict(Counter(row['system'] for row in rows))}")
    print(f"SLE: {dict(Counter(row['sle'] for row in rows))}")
    delivered = [row["time_to_delivery_h"] for row in rows if row["time_to_delivery_h"] is not None]
    identified = [row["time_to_identification_h"] for row in rows if row["time_to_identification_h"] is not None]
    if identified:
        print(f"avg time to identification: {round(sum(identified) / len(identified), 2)}h")
    if delivered:
        print(f"avg time to delivery: {round(sum(delivered) / len(delivered), 2)}h")


if __name__ == "__main__":
    main()
