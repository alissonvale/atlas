# Série Manutenção Ágil, 2019

Autor: Alisson Vale

Este anexo reúne a série de artigos usada como base histórica e conceitual do Atlas. A série antecede a formulação atual do método e usa a linguagem de manutenção ágil. Na documentação canônica do Atlas, essa linguagem é reinterpretada como sustentação de produtos de software.

## Parte 1: Dá pra ser Ágil na manutenção de produtos de software?

Publicado em 24 de janeiro de 2019.

O artigo parte da constatação de que grande parte dos desenvolvedores trabalha em manutenção de software, mas a gestão desse trabalho costuma ser tratada como assunto secundário. Times vivem apagando incêndios, tudo vira urgente, planejamentos são interrompidos, entregas são difíceis de prever e há pouco engajamento.

A resposta comum do mercado seria adotar Kanban, muitas vezes apoiada na simplificação de que Kanban seria para manutenção e Scrum para desenvolvimento. O artigo critica essa leitura. Kanban pode ajudar, mas não resolve sozinho. O ponto não é implementar o método, mas usar métodos como repertório para desenhar uma nova encarnação adaptada à realidade concreta.

A ideia central é a diferença entre princípio, método e realidade. Princípios são abstratos e carregam propósito. Métodos são receitas também abstratas. O concreto é o mundo real, com seus estímulos, restrições e decisões situadas. Quanto menos se conhece a própria realidade, maior a dependência de receitas externas.

O artigo estabelece necessidades típicas do contexto de manutenção: reagir rápido a desastres, absorver demandas urgentes, planejar e entregar ajustes com leveza, e manter a entrega continuada de projetos de expansão do produto.

## Parte 2: Uma nova perspectiva

Publicado em 30 de janeiro de 2019.

O artigo aprofunda a tese de que não basta aplicar métodos ágeis existentes. É preciso compreender o espírito dos princípios e materializá-los em uma forma adaptada ao propósito da manutenção.

A transição para manutenção não acontece quando o software é colocado em produção. Ela acontece quando o negócio do cliente passa a depender do produto. Nesse momento, o software deixa de ser apenas software e se torna parte integrante do negócio.

Essa transição muda a estrutura de riscos. O projeto passa a conviver com riscos operacionais adicionais, sem deixar de carregar riscos ligados a retorno sobre investimento. Essa mudança altera o modelo de gestão.

A virada conceitual do artigo é sair da gestão de demandas para a gestão de riscos. Demandas emergem da estrutura de riscos à qual o produto está exposto. O erro é desenhar sistemas para responder a demandas, quando o necessário é desenhar sistemas para responder aos riscos.

## Parte 3: Dominado pelo imprevisível, refém do caos

Publicado em 1 de fevereiro de 2019.

O artigo descreve uma estrutura de cinco riscos presentes em projetos de manutenção:

1. risco de perda financeira direta ou perda irrecuperável de credibilidade causada pelo software ou seu mau funcionamento;
2. risco de aumento de custo ou ineficiência em uma operação de negócio do cliente;
3. risco de o produto não acompanhar mudanças no ambiente de negócio que ele suporta;
4. risco de o produto não permitir expansão do negócio na direção de novas oportunidades, inovação ou ganho de eficiência;
5. risco de o software não evoluir tecnicamente para permanecer apto a sustentar a rede de riscos em que opera.

O artigo mostra que riscos diferentes geram demandas diferentes. Os dois primeiros estão ligados a demandas não planejadas. O terceiro se manifesta como demandas planejáveis, mas voláteis. O quarto aparece em projetos de expansão longos e frequentemente interrompidos. O quinto aponta para a qualidade técnica interna.

Um ponto importante é a distinção entre touch time e lead time. A entrega não acontece no tempo que o desenvolvedor levaria isoladamente para executar, mas no tempo produzido pelo sistema de desenvolvimento. O gestor que confunde esforço individual com tempo sistêmico de entrega cria expectativas irreais.

O artigo também critica a aplicação simplista de classes de serviço, como expedite, quando elas não dão conta da realidade concreta. A prática pode estar próxima do problema, mas ainda exige adaptação ao contexto.

## Parte final: Combatendo a ignorância sistêmica

Publicado em 4 de fevereiro de 2019.

O artigo fecha a série colocando o pensamento sistêmico como fundamento da solução. A pergunta deixa de ser o que há de errado com as pessoas e passa a ser o que há de errado com o sistema.

Em times de manutenção, cada pessoa pode estar fazendo sua parte racionalmente e ainda assim produzir coletivamente resultados indesejados. Essa é a ignorância sistêmica: agir localmente sem consciência da resultante global.

A alternativa é a consciência sistêmica. O interesse deixa de ser produzir mais demandas em menos tempo e passa a ser entregar a demanda certa no tempo certo. O valor mais alto deixa de ser eficiência local e passa a ser eficácia sistêmica.

O artigo reafirma que métodos ágeis podem apoiar essa direção, mas precisam ser ajustados à perspectiva de gestão de risco. Regras, cerimônias, métricas, estratégias e coordenação tática devem ser organizadas para lidar com o ambiente volátil e imprevisível da sustentação.

## Conceitos relevantes para o Atlas

- Métodos devem ser usados como repertório, não implantados como receita.
- A transição para sustentação acontece quando o negócio passa a depender do produto.
- O centro da gestão deve sair da demanda e ir para a estrutura de riscos.
- A manutenção tradicional sofre por ignorância sistêmica, fila única e heroísmo reativo.
- O sistema, não o indivíduo isolado, produz o lead time real.
- Urgência indiferenciada destrói previsibilidade.
- A expansão de produto e a evolução técnica são riscos relevantes, mas não devem ser confundidas com o fluxo de adaptação de funcionalidades existentes.
