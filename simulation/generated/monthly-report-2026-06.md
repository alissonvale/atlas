# Relatório mensal Atlas: HygiaTech, junho de 2026

Este relatório é gerado a partir das quatro semanas históricas da simulação HygiaTech.

## Resumo executivo

- Tickets no mês: 45.
- Eventos operacionais registrados: 162.
- Distribuição Atlas: {'S1': 4, 'S2': 21, 'S3': 17, 'suporte': 3}.
- Interações com Mirror: 25.
- Candidatos S3 criados: 16.
- Learning Reviews semanais: 4.

## Saúde de S1 e S2

S1 e S2 somaram 25 tickets. O pulso de SLE ficou em `{'in': 25, 'not_applicable': 20}`.
O padrão dominante é que o pronto-atendimento operacional depende da capacidade Delphi e da qualidade de evidência coletada pelo help desk.

## Saúde de S3

S3 acumulou 17 tickets e 16 eventos de candidatura/qualificação.
O sinal é positivo: sustentação está produzindo material de adaptação. O risco é S3 virar depósito de tudo que não coube em S1/S2.

## Gargalo técnico

Delphi 2007/DataSnap concentrou 34 tickets. C# API concentrou 9 tickets.
Delphi é a restrição central do sistema. A programação S3 precisa proteger capacidade Delphi, não apenas reagir ao volume de tickets.

## Módulos mais sensíveis

- Faturamento: 10
- Prescrição: 4
- Laboratório: 4
- Imagem: 4
- Dados e Rotinas Técnicas: 4
- Agenda: 3
- Farmácia: 3
- Pronto Atendimento: 2

## Clientes com maior presença

- Hospital Vida Serena: 4
- Hospital Metropolitano Lumen: 4
- Hospital São Lucas do Cerrado: 4
- Hospital Santa Aurora: 3
- Hospital Esperança Norte: 3
- Instituto Clínico Horizonte: 3
- Centro Médico Primavera: 3
- Hospital Central das Araucárias: 2

## Aprendizados do mês

- Evidência fraca continua aumentando tempo de identificação em hospitais de menor maturidade.
- Faturamento concentra pressão recorrente, especialmente perto de janelas de fechamento.
- Observabilidade em DataSnap e integrações é uma alavanca de redução de S1/S2.
- Customizações executivas precisam permanecer em S3 quando não há risco operacional real.

## Decisões recomendadas

- Programar um ciclo S3 focado em faturamento e observabilidade DataSnap.
- Criar checklist de evidência mínima por tipo de demanda no help desk.
- Definir limite de capacidade Delphi protegida para S3.
- Consolidar comunicação padrão para S1 e S2 em hospitais de alta criticidade.

## Próximo ciclo

A semana atual deve ser operada como campo vivo: resolver S1/S2 pendentes, decidir programação S3 e impedir que pressão comercial substitua leitura de risco.
