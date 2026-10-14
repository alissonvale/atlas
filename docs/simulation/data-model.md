# Modelo de dados da simulação

A simulação HygiaTech usa YAML como fonte canônica e artefatos derivados para consulta.

## Fonte canônica

```text
simulation/data/hospitals.yaml
simulation/data/modules.yaml
simulation/data/staff.yaml
simulation/data/demand-types.yaml
simulation/data/policies.yaml
simulation/data/ticket-model.yaml
simulation/data/tickets-*.yaml
simulation/data/events-*.yaml
```

Os arquivos de tickets e eventos são separados por semana. As semanas `week-01` a `week-04` são histórico fechado. `current-week` é a operação viva.

## Artefatos derivados

```text
simulation/generated/hygiatech.sqlite
simulation/generated/index.html
simulation/generated/monthly-report-2026-06.md
```

Esses arquivos podem ser regenerados e não são fonte autoral.

## Regra de fronteira

O banco `memory.db` da instalação HygiaTech guarda memória narrativa, conversas e aprendizados. Os dados operacionais da simulação ficam no repositório Atlas.
