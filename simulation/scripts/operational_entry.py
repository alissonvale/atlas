#!/usr/bin/env python3
"""Show an operational entry view for a HygiaTech staff member."""

from __future__ import annotations

import argparse
import json
from collections import Counter

from simlib import events_by_ticket, final_status, label, load_catalogs, load_data_file, load_week, sle_state


def main() -> None:
    parser = argparse.ArgumentParser(description="Render staff operational entry data")
    parser.add_argument("--staff", required=True, help="Staff id, for example HD-003")
    parser.add_argument("--json", action="store_true", help="Emit structured Operational Entry JSON")
    args = parser.parse_args()

    payload = operational_entry_payload(args.staff)
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    print("HygiaTech Operational Entry")
    print("=" * 40)
    staff = payload["staff"]
    print(f"staff: {staff['name']} ({staff['id']})")
    print(f"role today: {staff['roleToday']}")
    print(f"shift: {staff['shift']}")
    print(f"allocation: {staff['allocation']}")
    print(f"response systems: {', '.join(staff['responseSystems'])}")

    print("\nResponsibilities")
    for item in payload["responsibilities"]:
        print(f"  - {item}")

    print("\nCurrent system posture")
    print(f"  systems: {payload['systemPosture']['systems']}")
    print(f"  statuses: {payload['systemPosture']['statuses']}")

    print("\nFocus tickets")
    if not payload["focusTickets"]:
        print("  none")
    for ticket in payload["focusTickets"]:
        print(f"  {ticket['id']} [{ticket['responseSystem']}] {ticket['title']}")
        print(f"    hospital: {ticket['hospital']}")
        print(f"    module: {ticket['module']}")
        print(f"    status: {ticket['status']} | SLE: {ticket['sle']}")
        print(f"    suggested attention: {ticket['suggestedAttention']}")


def operational_entry_payload(staff_id: str) -> dict:
    catalogs = load_catalogs()
    assignments = load_data_file("assignments-current-week.yaml")["assignments"]
    assignment = next((item for item in assignments if item["staff_id"] == staff_id), None)
    if not assignment:
        raise SystemExit(f"assignment not found for staff: {staff_id}")

    ticket_batch, event_batch = load_week("current-week")
    tickets = {ticket["id"]: ticket for ticket in ticket_batch["tickets"]}
    grouped = events_by_ticket(event_batch["events"])
    focus = [tickets[ticket_id] for ticket_id in assignment.get("focus_tickets", []) if ticket_id in tickets]
    all_tickets = ticket_batch["tickets"]

    return {
        "surface": "operational_entry",
        "journey": "sustentacao",
        "staff": {
            "id": assignment["staff_id"],
            "name": assignment["staff_name"],
            "roleToday": assignment["role_today"],
            "shift": assignment["shift"],
            "allocation": assignment["allocation"],
            "responseSystems": assignment["response_systems"],
        },
        "responsibilities": assignment["responsibilities"],
        "systemPosture": {
            "systems": dict(Counter(ticket["response_system"] for ticket in all_tickets)),
            "statuses": dict(Counter(final_status(ticket, grouped.get(ticket["id"], [])) for ticket in all_tickets)),
        },
        "focusTickets": [
            {
                "id": ticket["id"],
                "title": ticket["title"],
                "responseSystem": ticket["response_system"],
                "hospital": label(catalogs["hospitals"], ticket["hospital_id"]),
                "module": label(catalogs["modules"], ticket["module"]),
                "status": final_status(ticket, grouped.get(ticket["id"], [])),
                "sle": sle_state(ticket, grouped.get(ticket["id"], [])),
                "suggestedAttention": suggested_attention(ticket, final_status(ticket, grouped.get(ticket["id"], []))),
            }
            for ticket in focus
        ],
    }


def suggested_attention(ticket: dict, status: str) -> str:
    if status == "awaiting_evidence":
        return "complete evidence before stabilizing triage"
    if ticket["response_system"] == "S1":
        return "confirm validation and capture learning"
    if ticket["id"] == "TCK-2026-CW-005":
        return "keep in S3 unless operational risk changes"
    if ticket["response_system"] == "S3":
        return "prepare programming decision"
    if ticket["response_system"] == "S2":
        return "protect SLE and make next action explicit"
    return "monitor"


if __name__ == "__main__":
    main()
