# Revisão mensal

A revisão mensal consolida as quatro semanas históricas da HygiaTech.

Arquivos usados:

```text
simulation/data/tickets-week-01.yaml
simulation/data/events-week-01.yaml
simulation/data/tickets-week-02.yaml
simulation/data/events-week-02.yaml
simulation/data/tickets-week-03.yaml
simulation/data/events-week-03.yaml
simulation/data/tickets-week-04.yaml
simulation/data/events-week-04.yaml
```

## Resumo estrutural

```bash
cd /Users/alissonvale/Code/atlas
python simulation/scripts/summarize_month.py
```

## Relatório narrativo

```bash
python simulation/scripts/monthly_report.py
```

Saída:

```text
simulation/generated/monthly-report-2026-06.md
```

## Perguntas Atlas

A revisão mensal deve responder:

- S1 e S2 protegeram a operação?
- Onde o SLE foi consumido?
- Quais módulos concentraram risco?
- Delphi virou gargalo explícito?
- Quais recorrências viraram S3?
- O help desk coletou evidência suficiente?
- Que decisão de capacidade, produto ou processo precisa nascer agora?
