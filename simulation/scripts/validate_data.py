#!/usr/bin/env python3
"""Validate HygiaTech simulation seed data."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "simulation" / "data"


def load_yaml(filename: str) -> dict[str, Any]:
    path = DATA_DIR / filename
    if not path.exists():
        raise AssertionError(f"missing file: {path}")
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise AssertionError(f"{filename}: expected YAML mapping")
    return data


def require_kind(data: dict[str, Any], expected: str, filename: str) -> None:
    actual = data.get("kind")
    if actual != expected:
        raise AssertionError(f"{filename}: expected kind {expected!r}, got {actual!r}")


def require_unique(items: list[dict[str, Any]], field: str, label: str) -> None:
    values = [item.get(field) for item in items]
    duplicates = sorted(value for value, count in Counter(values).items() if count > 1)
    if duplicates:
        raise AssertionError(f"{label}: duplicate {field}: {duplicates}")


def require_fields(item: dict[str, Any], fields: list[str], label: str) -> None:
    missing = [field for field in fields if field not in item or item[field] in (None, "")]
    if missing:
        raise AssertionError(f"{label}: missing fields: {missing}")


def validate_catalogs() -> dict[str, Any]:
    hospitals_data = load_yaml("hospitals.yaml")
    modules_data = load_yaml("modules.yaml")
    staff_data = load_yaml("staff.yaml")
    demand_types_data = load_yaml("demand-types.yaml")
    policies_data = load_yaml("policies.yaml")
    ticket_model_data = load_yaml("ticket-model.yaml")
    assignments_data = load_yaml("assignments-current-week.yaml")

    require_kind(hospitals_data, "hygiatech_hospitals", "hospitals.yaml")
    require_kind(modules_data, "hygiatech_modules", "modules.yaml")
    require_kind(staff_data, "hygiatech_staff", "staff.yaml")
    require_kind(demand_types_data, "hygiatech_demand_types", "demand-types.yaml")
    require_kind(policies_data, "hygiatech_policies", "policies.yaml")
    require_kind(ticket_model_data, "hygiatech_ticket_model", "ticket-model.yaml")
    require_kind(assignments_data, "hygiatech_assignments", "assignments-current-week.yaml")

    hospitals = hospitals_data["hospitals"]
    modules = modules_data["modules"]
    teams = staff_data["teams"]
    staff = staff_data["staff"]
    demand_types = demand_types_data["demand_types"]

    require_unique(hospitals, "id", "hospitals")
    require_unique(modules, "id", "modules")
    require_unique(modules, "slug", "modules")
    require_unique(teams, "id", "teams")
    require_unique(teams, "slug", "teams")
    require_unique(staff, "id", "staff")
    require_unique(demand_types, "id", "demand_types")
    require_unique(demand_types, "slug", "demand_types")

    team_slugs = {team["slug"] for team in teams}
    for person in staff:
        require_fields(person, ["id", "name", "team", "role"], f"staff.{person.get('id')}")
        if person["team"] not in team_slugs:
            raise AssertionError(f"staff.{person['id']}: unknown team {person['team']!r}")

    classes = {item["id"] for item in policies_data["classification"]["classes"]}
    systems = {item["system"] for item in policies_data["sle_policies"]}
    if classes != {"R1", "R2", "R3"}:
        raise AssertionError(f"policies: expected R1/R2/R3 classes, got {classes}")
    if systems != {"S1", "S2", "S3"}:
        raise AssertionError(f"policies: expected S1/S2/S3 SLE policies, got {systems}")

    print(f"validated {len(hospitals)} hospitals")
    print(f"validated {len(modules)} modules")
    print(f"validated {len(teams)} teams")
    print(f"validated {len(staff)} staff")
    print(f"validated {len(demand_types)} demand types")
    assignments = assignments_data["assignments"]
    require_unique(assignments, "staff_id", "assignments")
    staff_ids = {item["id"] for item in staff}
    valid_systems = {"S1", "S2", "S3", "suporte"}
    for assignment in assignments:
        label = f"assignment.{assignment.get('staff_id')}"
        require_fields(assignment, ["staff_id", "shift", "allocation", "response_systems", "role_today", "responsibilities"], label)
        if assignment["staff_id"] not in staff_ids:
            raise AssertionError(f"{label}: unknown staff_id {assignment['staff_id']!r}")
        unknown_systems = set(assignment["response_systems"]) - valid_systems
        if unknown_systems:
            raise AssertionError(f"{label}: unknown response systems {sorted(unknown_systems)}")

    print("validated policies, ticket model, and assignments")

    event_types = {
        event_type
        for group in ticket_model_data["event_types"].values()
        for event_type in group
    }

    return {
        "hospital_ids": {item["id"] for item in hospitals},
        "module_slugs": {item["slug"] for item in modules},
        "team_slugs": team_slugs,
        "staff_ids": staff_ids,
        "demand_type_slugs": {item["slug"] for item in demand_types},
        "event_types": event_types,
        "assignment_focus_tickets": {
            ticket_id
            for assignment in assignments
            for ticket_id in assignment.get("focus_tickets", [])
        },
    }


def validate_ticket_batch(filename: str, refs: dict[str, set[str]]) -> set[str]:
    data = load_yaml(filename)
    require_kind(data, "hygiatech_ticket_batch", filename)

    tickets = data.get("tickets", [])
    if not isinstance(tickets, list):
        raise AssertionError(f"{filename}: tickets must be a list")

    require_unique(tickets, "id", filename)

    declared_total = data.get("summary", {}).get("total_tickets")
    if declared_total != len(tickets):
        raise AssertionError(f"{filename}: summary total {declared_total} != actual {len(tickets)}")

    required_fields = [
        "id",
        "title",
        "hospital_id",
        "demand_type",
        "module",
        "opened_at",
        "source",
        "reported_by",
        "description",
        "perceived_urgency",
        "operational_impact",
        "affected_users",
        "workaround_available",
        "evidence_quality",
        "initial_atlas_class",
        "response_system",
        "status",
        "assigned_team",
        "sle_policy",
    ]

    allowed_class_system = {
        "R1": "S1",
        "R2": "S2",
        "R3": "S3",
        "suporte_sem_atlas": "suporte",
        "incerta": "incerto",
    }

    for ticket in tickets:
        label = f"{filename}.{ticket.get('id')}"
        require_fields(ticket, required_fields, label)

        if ticket["hospital_id"] not in refs["hospital_ids"]:
            raise AssertionError(f"{label}: unknown hospital_id {ticket['hospital_id']!r}")
        if ticket["module"] not in refs["module_slugs"]:
            raise AssertionError(f"{label}: unknown module {ticket['module']!r}")
        if ticket["demand_type"] not in refs["demand_type_slugs"]:
            raise AssertionError(f"{label}: unknown demand_type {ticket['demand_type']!r}")
        if ticket["assigned_team"] not in refs["team_slugs"]:
            raise AssertionError(f"{label}: unknown assigned_team {ticket['assigned_team']!r}")
        if ticket.get("assigned_staff") and ticket["assigned_staff"] not in refs["staff_ids"]:
            raise AssertionError(f"{label}: unknown assigned_staff {ticket['assigned_staff']!r}")

        expected_system = allowed_class_system.get(ticket["initial_atlas_class"])
        if expected_system and ticket["response_system"] != expected_system:
            raise AssertionError(
                f"{label}: class {ticket['initial_atlas_class']} expects response_system "
                f"{expected_system}, got {ticket['response_system']}"
            )

        if ticket["response_system"] in {"S1", "S2", "S3"} and ticket["sle_policy"] != ticket["response_system"]:
            raise AssertionError(f"{label}: sle_policy must match response_system")

    actual_distribution = Counter(ticket["response_system"] for ticket in tickets)
    declared_distribution = data.get("summary", {}).get("expected_distribution", {})
    if declared_distribution != dict(actual_distribution):
        raise AssertionError(
            f"{filename}: expected_distribution {declared_distribution} != actual {dict(actual_distribution)}"
        )

    print(f"validated {len(tickets)} tickets in {filename}: {dict(actual_distribution)}")
    return {ticket["id"] for ticket in tickets}


def validate_event_batch(filename: str, refs: dict[str, set[str]], ticket_ids: set[str]) -> None:
    data = load_yaml(filename)
    require_kind(data, "hygiatech_event_batch", filename)

    events = data.get("events", [])
    if not isinstance(events, list):
        raise AssertionError(f"{filename}: events must be a list")

    require_unique(events, "id", filename)

    known_actor_ids = refs["staff_ids"] | refs["hospital_ids"] | {
        "interno_hygiatech",
        "executivo_cliente",
    }

    required_fields = [
        "id",
        "ticket_id",
        "occurred_at",
        "event_type",
        "actor_type",
        "actor_id",
        "summary",
    ]

    per_ticket = Counter()
    for event in events:
        label = f"{filename}.{event.get('id')}"
        require_fields(event, required_fields, label)

        if event["ticket_id"] not in ticket_ids:
            raise AssertionError(f"{label}: unknown ticket_id {event['ticket_id']!r}")
        if event["event_type"] not in refs["event_types"]:
            raise AssertionError(f"{label}: unknown event_type {event['event_type']!r}")
        if event["actor_id"] not in known_actor_ids:
            raise AssertionError(f"{label}: unknown actor_id {event['actor_id']!r}")
        if "to_class" in event and event["event_type"] not in {"triage_decided", "reclassified", "closed"}:
            raise AssertionError(f"{label}: to_class only belongs to triage/reclassification/closure events")
        if event.get("mirror_used") is True and not event.get("mirror_prompt_summary"):
            raise AssertionError(f"{label}: mirror_used=true requires mirror_prompt_summary")
        per_ticket[event["ticket_id"]] += 1

    tickets_without_events = sorted(ticket_ids - set(per_ticket))
    if tickets_without_events:
        raise AssertionError(f"{filename}: tickets without events: {tickets_without_events}")

    print(f"validated {len(events)} events in {filename}")


def main() -> None:
    refs = validate_catalogs()
    ticket_ids_by_week: dict[str, set[str]] = {}
    for path in sorted(DATA_DIR.glob("tickets-*.yaml")):
        week = path.stem.removeprefix("tickets-")
        ticket_ids_by_week[week] = validate_ticket_batch(path.name, refs)
    all_ticket_ids = {ticket_id for ids in ticket_ids_by_week.values() for ticket_id in ids}
    unknown_focus = refs["assignment_focus_tickets"] - all_ticket_ids
    if unknown_focus:
        raise AssertionError(f"assignments-current-week.yaml: unknown focus tickets: {sorted(unknown_focus)}")
    for path in sorted(DATA_DIR.glob("events-*.yaml")):
        week = path.stem.removeprefix("events-")
        validate_event_batch(path.name, refs, ticket_ids_by_week.get(week, set()))


if __name__ == "__main__":
    main()
