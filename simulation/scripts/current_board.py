#!/usr/bin/env python3
"""Render the current operational board for HygiaTech."""

from __future__ import annotations

from collections import defaultdict

from simlib import events_by_ticket, final_status, label, load_catalogs, load_week, sle_state, stage_times

DECISION_STATUSES = {"prioritized", "awaiting_evidence", "investigating", "s3_candidate", "qualified", "s2_confirmed", "delivering"}


def main() -> None:
    catalogs = load_catalogs()
    ticket_batch, event_batch = load_week("current-week")
    tickets = ticket_batch["tickets"]
    grouped_events = events_by_ticket(event_batch["events"])

    lanes: dict[str, list[dict]] = defaultdict(list)
    for ticket in tickets:
        status = final_status(ticket, grouped_events.get(ticket["id"], []))
        if status in {"closed", "support_resolved"}:
            lane = "resolved"
        elif ticket["response_system"] == "S1":
            lane = "S1 active / recently contained"
        elif status == "awaiting_evidence":
            lane = "awaiting evidence"
        elif ticket["response_system"] == "S2":
            lane = "S2 in motion"
        elif ticket["response_system"] == "S3":
            lane = "S3 programming candidates"
        else:
            lane = "other"
        lanes[lane].append({"ticket": ticket, "status": status})

    print("HygiaTech Current Atlas Board")
    print("=" * 44)
    print(ticket_batch["batch"]["name"])
    print()

    for lane in ["S1 active / recently contained", "S2 in motion", "awaiting evidence", "S3 programming candidates", "resolved", "other"]:
        items = lanes.get(lane, [])
        if not items:
            continue
        print(f"\n{lane.upper()}")
        for item in items:
            ticket = item["ticket"]
            ticket_events = grouped_events.get(ticket["id"], [])
            times = stage_times(ticket, ticket_events)
            print(f"  {ticket['id']} [{ticket['response_system']}] {ticket['title']}")
            print(f"    hospital: {label(catalogs['hospitals'], ticket['hospital_id'])}")
            print(f"    module: {label(catalogs['modules'], ticket['module'])}")
            print(f"    status: {item['status']} | SLE: {sle_state(ticket, ticket_events)}")
            print(f"    team: {label(catalogs['teams'], ticket['assigned_team'])}")
            if times["time_to_identification_h"] is not None:
                print(f"    time to identification: {times['time_to_identification_h']}h")
            print(f"    decision signal: {decision_signal(ticket, item['status'])}")


def decision_signal(ticket: dict, status: str) -> str:
    if ticket["response_system"] == "S1" and status != "closed":
        return "confirm customer validation and capture learning before closing"
    if status == "awaiting_evidence":
        return "help desk must obtain evidence before classification hardens"
    if ticket["id"] == "TCK-2026-CW-002":
        return "protect S2 window without letting every S3 deadline become urgency"
    if ticket["id"] == "TCK-2026-CW-005":
        return "keep as S3 unless new operational risk appears"
    if ticket["response_system"] == "S3" and status == "qualified":
        return "candidate for next S3 programming decision"
    if ticket.get("recurrence_group"):
        return "recurrence should feed Learning Review after containment"
    if ticket["response_system"] == "S2":
        return "track SLE and capacity consumption"
    return "no immediate decision"


if __name__ == "__main__":
    main()
