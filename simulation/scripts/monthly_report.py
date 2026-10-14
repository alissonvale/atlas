#!/usr/bin/env python3
"""Generate a narrative monthly Atlas report for HygiaTech."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from simlib import GENERATED_DIR, events_by_ticket, label, load_catalogs, load_week, sle_state

WEEKS = ["week-01", "week-02", "week-03", "week-04"]


def main() -> None:
    catalogs = load_catalogs()
    tickets = []
    events = []
    for week in WEEKS:
        tb, eb = load_week(week)
        tickets.extend(tb["tickets"])
        events.extend(eb["events"])
    grouped = events_by_ticket(events)

    systems = Counter(ticket["response_system"] for ticket in tickets)
    technologies = Counter(ticket.get("primary_technology", "unknown") for ticket in tickets)
    modules = Counter(ticket["module"] for ticket in tickets)
    hospitals = Counter(ticket["hospital_id"] for ticket in tickets)
    sle = Counter(sle_state(ticket, grouped.get(ticket["id"], [])) for ticket in tickets)
    s3_events = [event for event in events if event["event_type"] == "s3_candidate_created"]
    mirror_events = [event for event in events if event.get("mirror_used")]
    learning = [event for event in events if event["event_type"] == "learning_review_created"]

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    out = GENERATED_DIR / "monthly-report-2026-06.md"
    lines = [
        "# Relatório mensal Atlas: HygiaTech, junho de 2026",
        "",
        "Este relatório é gerado a partir das quatro semanas históricas da simulação HygiaTech.",
        "",
        "## Resumo executivo",
        "",
        f"- Tickets no mês: {len(tickets)}.",
        f"- Eventos operacionais registrados: {len(events)}.",
        f"- Distribuição Atlas: {dict(systems)}.",
        f"- Interações com Mirror: {len(mirror_events)}.",
        f"- Candidatos S3 criados: {len(s3_events)}.",
        f"- Learning Reviews semanais: {len(learning)}.",
        "",
        "## Saúde de S1 e S2",
        "",
        f"S1 e S2 somaram {systems.get('S1', 0) + systems.get('S2', 0)} tickets. O pulso de SLE ficou em `{dict(sle)}`.",
        "O padrão dominante é que o pronto-atendimento operacional depende da capacidade Delphi e da qualidade de evidência coletada pelo help desk.",
        "",
        "## Saúde de S3",
        "",
        f"S3 acumulou {systems.get('S3', 0)} tickets e {len(s3_events)} eventos de candidatura/qualificação.",
        "O sinal é positivo: sustentação está produzindo material de adaptação. O risco é S3 virar depósito de tudo que não coube em S1/S2.",
        "",
        "## Gargalo técnico",
        "",
        f"Delphi 2007/DataSnap concentrou {technologies.get('delphi_2007_datasnap', 0)} tickets. C# API concentrou {technologies.get('csharp_api', 0)} tickets.",
        "Delphi é a restrição central do sistema. A programação S3 precisa proteger capacidade Delphi, não apenas reagir ao volume de tickets.",
        "",
        "## Módulos mais sensíveis",
        "",
    ]
    for module, count in modules.most_common(8):
        lines.append(f"- {label(catalogs['modules'], module)}: {count}")
    lines += ["", "## Clientes com maior presença", ""]
    for hospital, count in hospitals.most_common(8):
        lines.append(f"- {label(catalogs['hospitals'], hospital)}: {count}")
    lines += [
        "",
        "## Aprendizados do mês",
        "",
        "- Evidência fraca continua aumentando tempo de identificação em hospitais de menor maturidade.",
        "- Faturamento concentra pressão recorrente, especialmente perto de janelas de fechamento.",
        "- Observabilidade em DataSnap e integrações é uma alavanca de redução de S1/S2.",
        "- Customizações executivas precisam permanecer em S3 quando não há risco operacional real.",
        "",
        "## Decisões recomendadas",
        "",
        "- Programar um ciclo S3 focado em faturamento e observabilidade DataSnap.",
        "- Criar checklist de evidência mínima por tipo de demanda no help desk.",
        "- Definir limite de capacidade Delphi protegida para S3.",
        "- Consolidar comunicação padrão para S1 e S2 em hospitais de alta criticidade.",
        "",
        "## Próximo ciclo",
        "",
        "A semana atual deve ser operada como campo vivo: resolver S1/S2 pendentes, decidir programação S3 e impedir que pressão comercial substitua leitura de risco.",
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"generated {out}")


if __name__ == "__main__":
    main()
