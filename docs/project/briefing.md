# Briefing: Atlas

## Propósito

Construir o Atlas: um método de gestão voltado para a sustentação de produtos de software.

Atlas nasce de uma recusa: tratar o trabalho posterior à entrega como manutenção, no sentido pobre de reparo, ajuste ou custo inevitável. A linguagem central do método é sustentação. Sustentar é manter vivo um sistema sociotécnico do qual a operação do negócio passou a depender.

## Tese central

Um produto entra em estado de sustentação no momento em que a operação de negócio do cliente passa a depender dele para funcionar.

Esse marco desloca a gestão. O objeto de atenção deixa de ser apenas o software e passa a ser o risco operacional gerado na relação entre software, negócio, usuários, mercado, suporte e equipe técnica.

A pergunta orientadora deixa de ser "como consertamos este bug?" e passa a ser "qual risco esta situação impõe ao negócio que apoiamos?".

## Modelo inicial

O descritivo recebido organiza a sustentação em três arquétipos de risco:

- R1, risco de perda tangível imediata, no qual o negócio perde valor relevante a cada momento de mau funcionamento.
- R2, risco de operação bloqueada ou comprometida, no qual há urgência real, mas não necessariamente sangria imediata.
- R3, risco de adaptação, no qual o produto precisa acompanhar novas necessidades de negócio, legislação, mercado ou eficiência operacional para não se tornar obsoleto.

Esses riscos pedem sistemas de resposta distintos:

- S1, resposta imediata para R1.
- S2, resposta rápida para R2.
- S3, resposta programada para R3.

As planilhas recebidas expandem esse mapa com dois sistemas adicionais:

- S4, resposta projetizada, aparentemente voltada a entregáveis maiores e coordenados como projeto.
- S5, resposta disciplinada, aparentemente voltada ao aprendizado sistêmico e às melhorias internas necessárias após sinais vindos dos demais sistemas.

## Artefatos recebidos

A pasta `materials/` contém o descritivo conceitual e um conjunto de CSVs exportados do painel original do Atlas. O inventário está em `docs/attachments/index.md`.

## Fronteira inicial

Atlas é o método de sustentação de produtos de software. Planilhas, dashboards, templates, automações e rotinas são artefatos do método, não substitutos dele.

A primeira tarefa de documentação é separar três camadas:

- método, com vocabulário, princípios, riscos, sistemas e papéis;
- operação, com cadências, métricas, fluxos e critérios de triagem;
- adoção, com templates, guias e exemplos para aplicar Atlas em produtos reais.

## Hipóteses a validar

S4 e S5 podem ser a chave para transformar Atlas de um modelo de pronto-atendimento e adaptação em um sistema completo de sustentação. S4 parece cuidar de mudanças grandes demais para o fluxo programado comum. S5 parece cuidar da disciplina de melhoria interna, isto é, do aprendizado que impede o sistema de repetir as mesmas falhas.

Essa hipótese precisa ser validada antes de virar cânone.
