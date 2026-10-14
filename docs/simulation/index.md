# Simulação HygiaTech

A simulação HygiaTech é o laboratório operacional do Atlas.

Ela representa uma empresa fictícia brasileira de tecnologia em saúde que sustenta um produto hospitalar usado por 20 clientes empresas. A realidade é inspirada em padrões reais de sustentação, mas todos os dados, clientes, pessoas, tickets e eventos são sintéticos.

## Premissas principais

- Core legado em Delphi 2007 com DataSnap, composto por client e server.
- Alguns serviços em Delphi Seattle.
- Backend/API em C#.
- Equipe técnica com 3 devs Delphi e 2 devs C#.
- Help desk com aproximadamente 8 pessoas.
- Maior volume de demanda concentrado no core Delphi.
- Hospitais usam o software na operação diária.

## Fronteira de isolamento

A HygiaTech roda em uma instalação própria do Mirror para evitar contaminação do Mirror pessoal de Alisson.

```text
Mirror pessoal de Alisson
  framework Atlas, decisões e documentação

Mirror sandbox da HygiaTech
  atores, personas, jornadas, demandas, memórias e conversas da simulação
```

A jornada Atlas no Mirror pessoal acompanha o framework. A instalação HygiaTech acompanha a operação simulada.

## Documentos

- [Modelo de dados](data-model.md)
- [Runbook da simulação](runbook.md)
- [Semana atual](current-week.md)
- [Design de fluxo operacional](operational-flow-design.md)
- [Revisão mensal](monthly-review.md)
- [Uso do Mirror HygiaTech](mirror-usage.md)
- [Roteiro de instalação do Mirror HygiaTech](mirror-installation-runbook.md)
