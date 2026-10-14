#!/usr/bin/env python3
"""Generate a small static HTML console for the HygiaTech simulation."""

from __future__ import annotations

import html
from collections import Counter

from simlib import GENERATED_DIR, all_week_slugs, events_by_ticket, final_status, label, load_catalogs, load_week, sle_state


def main() -> None:
    catalogs = load_catalogs()
    weeks = all_week_slugs(include_current=True)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    cards = []
    all_tickets = []
    for week in weeks:
        tb, eb = load_week(week)
        grouped = events_by_ticket(eb["events"])
        all_tickets.extend(tb["tickets"])
        cards.append(render_week(week, tb["tickets"], grouped, catalogs))
    systems = Counter(ticket["response_system"] for ticket in all_tickets)
    html_doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>HygiaTech Atlas Console</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; margin: 2rem; background: #f7f7f7; color: #222; }}
    h1, h2 {{ margin-bottom: .2rem; }}
    .summary, .week {{ background: white; border-radius: 12px; padding: 1rem 1.2rem; margin: 1rem 0; box-shadow: 0 1px 4px #ddd; }}
    .ticket {{ border-left: 5px solid #999; padding: .6rem .8rem; margin: .6rem 0; background: #fafafa; }}
    .S1 {{ border-color: #d33; }} .S2 {{ border-color: #f28c28; }} .S3 {{ border-color: #2775d1; }} .suporte {{ border-color: #777; }}
    code {{ background: #eee; padding: .1rem .3rem; border-radius: 4px; }}
  </style>
</head>
<body>
  <h1>HygiaTech Atlas Console</h1>
  <div class="summary">
    <h2>Resumo</h2>
    <p>Tickets carregados: {len(all_tickets)}</p>
    <p>Distribuição: {html.escape(str(dict(systems)))}</p>
    <p>Fonte: YAML em <code>simulation/data</code>. Este HTML é derivado e regenerável.</p>
  </div>
  {''.join(cards)}
</body>
</html>
"""
    out = GENERATED_DIR / "index.html"
    out.write_text("\n".join(line.rstrip() for line in html_doc.splitlines()) + "\n", encoding="utf-8")
    print(f"generated {out}")


def render_week(week: str, tickets: list[dict], grouped: dict, catalogs: dict) -> str:
    rows = []
    for ticket in tickets:
        status = final_status(ticket, grouped.get(ticket["id"], []))
        rows.append(f"""
        <div class="ticket {html.escape(ticket['response_system'])}">
          <strong>{html.escape(ticket['id'])}</strong> [{html.escape(ticket['response_system'])}] {html.escape(ticket['title'])}<br>
          Hospital: {html.escape(label(catalogs['hospitals'], ticket['hospital_id']))}<br>
          Módulo: {html.escape(label(catalogs['modules'], ticket['module']))}<br>
          Status: <code>{html.escape(status)}</code> | SLE: <code>{html.escape(sle_state(ticket, grouped.get(ticket['id'], [])))}</code>
        </div>
        """)
    return f"<section class='week'><h2>{html.escape(week)}</h2>{''.join(rows)}</section>"


if __name__ == "__main__":
    main()
