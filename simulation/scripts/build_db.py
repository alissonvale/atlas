#!/usr/bin/env python3
"""Build a derived SQLite database for the HygiaTech simulation."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from simlib import DATA_DIR, GENERATED_DIR, all_week_slugs, load_data_file, load_week

DB_PATH = GENERATED_DIR / "hygiatech.sqlite"


def main() -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    if DB_PATH.exists():
        DB_PATH.unlink()
    con = sqlite3.connect(DB_PATH)
    con.execute("pragma foreign_keys=on")
    create_schema(con)
    insert_catalogs(con)
    insert_batches(con)
    con.commit()
    con.close()
    print(f"generated {DB_PATH}")


def create_schema(con: sqlite3.Connection) -> None:
    con.executescript(
        """
        create table hospitals(id text primary key, name text, payload text not null);
        create table modules(slug text primary key, name text, payload text not null);
        create table teams(slug text primary key, name text, payload text not null);
        create table staff(id text primary key, name text, team text, payload text not null);
        create table demand_types(slug text primary key, name text, payload text not null);
        create table tickets(
            id text primary key,
            week text not null,
            title text not null,
            hospital_id text,
            demand_type text,
            module text,
            response_system text,
            atlas_class text,
            status text,
            assigned_team text,
            assigned_staff text,
            opened_at text,
            payload text not null
        );
        create table events(
            id text primary key,
            week text not null,
            ticket_id text not null,
            occurred_at text not null,
            event_type text not null,
            actor_type text,
            actor_id text,
            mirror_used integer not null,
            summary text,
            payload text not null,
            foreign key(ticket_id) references tickets(id)
        );
        """
    )


def insert_catalogs(con: sqlite3.Connection) -> None:
    for item in load_data_file("hospitals.yaml")["hospitals"]:
        con.execute("insert into hospitals values (?, ?, ?)", (item["id"], item["name"], dump(item)))
    for item in load_data_file("modules.yaml")["modules"]:
        con.execute("insert into modules values (?, ?, ?)", (item["slug"], item["name"], dump(item)))
    staff_data = load_data_file("staff.yaml")
    for item in staff_data["teams"]:
        con.execute("insert into teams values (?, ?, ?)", (item["slug"], item["name"], dump(item)))
    for item in staff_data["staff"]:
        con.execute("insert into staff values (?, ?, ?, ?)", (item["id"], item["name"], item["team"], dump(item)))
    for item in load_data_file("demand-types.yaml")["demand_types"]:
        con.execute("insert into demand_types values (?, ?, ?)", (item["slug"], item["name"], dump(item)))


def insert_batches(con: sqlite3.Connection) -> None:
    for week in all_week_slugs(include_current=True):
        ticket_batch, event_batch = load_week(week)
        for ticket in ticket_batch["tickets"]:
            con.execute(
                """
                insert into tickets values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    ticket["id"], week, ticket["title"], ticket["hospital_id"], ticket["demand_type"], ticket["module"],
                    ticket["response_system"], ticket["initial_atlas_class"], ticket["status"], ticket["assigned_team"],
                    ticket.get("assigned_staff"), ticket["opened_at"], dump(ticket),
                ),
            )
        for event in event_batch["events"]:
            con.execute(
                "insert into events values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    event["id"], week, event["ticket_id"], event["occurred_at"], event["event_type"],
                    event.get("actor_type"), event.get("actor_id"), 1 if event.get("mirror_used") else 0,
                    event.get("summary"), dump(event),
                ),
            )


def dump(value: dict) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    main()
