# Semana atual

A semana atual é o campo vivo da simulação HygiaTech.

Arquivos:

```text
simulation/data/tickets-current-week.yaml
simulation/data/events-current-week.yaml
```

Diferente das semanas históricas, a semana atual mantém tickets abertos e decisões pendentes. Ela existe para simular a operação do Atlas em tempo presente.

## Ver o quadro

```bash
cd /Users/alissonvale/Code/atlas
python simulation/scripts/current_board.py
```

O quadro destaca:

- S1 ativo ou recém-contido;
- S2 em movimento;
- demandas aguardando evidência;
- candidatos S3 prontos para programação;
- pressão comercial sem risco operacional;
- recorrências que pedem aprendizado.

## Uso com Mirror HygiaTech

Abra:

```bash
~/mirror-hygia.sh
```

Perguntas úteis:

```text
revise a semana atual da sustentação Atlas
prepare comunicação para o Hospital Mar Azul
quais S3 devem entrar na próxima programação?
o ticket da agenda é urgência real ou pressão comercial?
que aprendizado deve nascer da divergência de estoque?
```
