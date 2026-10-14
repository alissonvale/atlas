#!/usr/bin/env python3
"""Shared helpers for HygiaTech simulation scripts."""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "simulation" / "data"
GENERATED_DIR = ROOT / "simulation" / "generated"


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"expected YAML mapping: {path}")
    return data


def load_data_file(filename: str) -> dict[str, Any]:
    return load_yaml(DATA_DIR / filename)


def load_catalogs() -> dict[str, dict[str, Any]]:
    staff_data = load_data_file("staff.yaml")
    return {
        "hospitals": {item["id"]: item for item in load_data_file("hospitals.yaml")["hospitals"]},
        "modules": {item["slug"]: item for item in load_data_file("modules.yaml")["modules"]},
        "teams": {item["slug"]: item for item in staff_data["teams"]},
        "staff": {item["id"]: item for item in staff_data["staff"]},
        "demand_types": {item["slug"]: item for item in load_data_file("demand-types.yaml")["demand_types"]},
    }


def label(catalog: dict[str, dict[str, Any]], key: str) -> str:
    item = catalog.get(key)
    return item.get("name", key) if item else key


def load_week(week: str) -> tuple[dict[str, Any], dict[str, Any]]:
    return load_data_file(f"tickets-{week}.yaml"), load_data_file(f"events-{week}.yaml")


def parse_dt(value: str) -> datetime:
    return datetime.fromisoformat(value)


def events_by_ticket(events: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        grouped[event["ticket_id"]].append(event)
    for ticket_events in grouped.values():
        ticket_events.sort(key=lambda event: event["occurred_at"])
    return grouped


def final_status(ticket: dict[str, Any], ticket_events: list[dict[str, Any]]) -> str:
    status = ticket.get("status", "unknown")
    for event in ticket_events:
        if event.get("to_status"):
            status = event["to_status"]
    return status


def stage_times(ticket: dict[str, Any], ticket_events: list[dict[str, Any]]) -> dict[str, float | None]:
    opened = parse_dt(ticket["opened_at"])
    first_triage = next((event for event in ticket_events if event["event_type"] == "triage_decided"), None)
    first_action = next(
        (
            event
            for event in ticket_events
            if event["event_type"] in {"assigned", "investigation_started", "workaround_applied", "fix_completed", "script_executed"}
        ),
        None,
    )
    first_delivery = next(
        (
            event
            for event in ticket_events
            if event.get("to_status") in {"delivering", "closed", "support_resolved"}
            or event["event_type"] in {"customer_validated", "closed"}
        ),
        None,
    )

    def hours_until(event: dict[str, Any] | None) -> float | None:
        if not event:
            return None
        return round((parse_dt(event["occurred_at"]) - opened).total_seconds() / 3600, 2)

    return {
        "time_to_identification_h": hours_until(first_triage),
        "time_to_reaction_h": hours_until(first_action),
        "time_to_delivery_h": hours_until(first_delivery),
    }


def sle_limit_hours(system: str) -> float | None:
    return {"S1": 8.0, "S2": 48.0}.get(system)


def sle_state(ticket: dict[str, Any], ticket_events: list[dict[str, Any]]) -> str:
    limit = sle_limit_hours(ticket.get("response_system"))
    if limit is None:
        return "not_applicable"
    delivered = stage_times(ticket, ticket_events)["time_to_delivery_h"]
    if delivered is None:
        return "open"
    return "in" if delivered <= limit else "out"


def all_week_slugs(include_current: bool = False) -> list[str]:
    weeks = sorted(path.stem.removeprefix("tickets-") for path in DATA_DIR.glob("tickets-week-*.yaml"))
    if include_current and (DATA_DIR / "tickets-current-week.yaml").exists():
        weeks.append("current-week")
    return weeks
