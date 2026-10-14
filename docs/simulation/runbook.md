# Runbook da simulação HygiaTech

## Validar dados

```bash
cd /Users/alissonvale/Code/atlas
python simulation/scripts/validate_data.py
```

## Ver quadro atual

```bash
python simulation/scripts/current_board.py
```

## Ver entrada operacional por funcionário

```bash
python simulation/scripts/operational_entry.py --staff HD-003
python simulation/scripts/operational_entry.py --staff COORD-001
python simulation/scripts/operational_entry.py --staff PROD-001
```

## Resumir uma semana

```bash
python simulation/scripts/summarize_week.py week-01
python simulation/scripts/summarize_week.py current-week
```

## Calcular métricas

```bash
python simulation/scripts/metrics.py
```

## Gerar relatório mensal

```bash
python simulation/scripts/monthly_report.py
```

Saída:

```text
simulation/generated/monthly-report-2026-06.md
```

## Gerar SQLite derivado

```bash
python simulation/scripts/build_db.py
```

Saída:

```text
simulation/generated/hygiatech.sqlite
```

## Gerar console HTML estático

```bash
python simulation/scripts/generate_static.py
```

Saída:

```text
simulation/generated/index.html
```

## Abrir Mirror HygiaTech

```bash
~/mirror-hygia.sh
```

Use o Mirror HygiaTech para operar a semana atual, não para editar a fonte da simulação.
