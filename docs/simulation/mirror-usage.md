# Uso do Mirror HygiaTech

A instalação HygiaTech do Mirror é o ambiente narrativo e operacional da empresa simulada.

Ela não substitui os dados YAML. Ela interpreta situações, ajuda papéis a decidir e registra aprendizados.

## Abrir

```bash
~/mirror-hygia.sh
```

## Papéis de uso

- Help desk: qualificação de entrada e evidência mínima.
- Gatekeeper: classificação R1/R2/R3 e reclassificação.
- Dev Delphi/C#: investigação e registro de hipótese.
- Coordenação: SLE Pulse, Learning Review e decisões de capacidade.
- Produto: programação S3 e fronteira entre sustentação e evolução.

## Prompts úteis

```text
revise o ticket TCK-2026-CW-003 e diga que evidências faltam
prepare uma comunicação S2 para o Hospital Mar Azul
avalie se TCK-2026-CW-005 deve continuar em S3
proponha a programação S3 da próxima semana
faça uma Learning Review da divergência de estoque recorrente
```

## Fronteira

A sessão HygiaTech pode gerar aprendizados e decisões simuladas. Alterações em dados canônicos devem ser feitas aqui no repositório Atlas, em `simulation/data`.
