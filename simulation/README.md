# Simulação HygiaTech

Esta pasta contém os dados estruturados da simulação HygiaTech.

A documentação narrativa da simulação fica em `docs/simulation/`. Esta pasta é a fonte operacional versionável: hospitais sintéticos, equipe, módulos, políticas, tickets, eventos, ciclos e dados derivados.

## Princípio de separação

```text
simulation/data
  fonte canônica editável e versionável

simulation/generated
  artefatos derivados, regeneráveis e não autorais

Mirror HygiaTech
  memória narrativa, decisões e aprendizados operacionais
```

O `memory.db` da instalação HygiaTech não deve ser usado como banco operacional primário da simulação. Ele registra conversas, memórias e aprendizados. Os dados operacionais vivem aqui e podem gerar um SQLite próprio quando houver web console ou consultas estruturadas.

## Estrutura

```text
simulation/
  README.md
  data/
    hospitals.yaml
    modules.yaml
    staff.yaml
    demand-types.yaml
    policies.yaml
    ticket-model.yaml
    tickets-*.yaml
    events-*.yaml
  scripts/
    validate_data.py
    current_board.py
    summarize_week.py
    summarize_month.py
    metrics.py
    monthly_report.py
    build_db.py
    generate_static.py
  generated/
    hygiatech.sqlite
    index.html
    monthly-report-2026-06.md
```

## Comandos principais

```bash
python simulation/scripts/validate_data.py
python simulation/scripts/current_board.py
python simulation/scripts/summarize_month.py
python simulation/scripts/monthly_report.py
python simulation/scripts/build_db.py
python simulation/scripts/generate_static.py
```

## Regra de simulação

A realidade é inspiradora, mas todos os dados são sintéticos. Nenhum nome, ticket, hospital, pessoa ou evidência deve identificar um cliente real.
