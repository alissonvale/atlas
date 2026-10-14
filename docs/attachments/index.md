# Anexos

Este índice registra os materiais usados para construir o Atlas e separa fonte bruta, leitura inicial e decisões derivadas.

## Materiais recebidos

| Material | Tipo | Uso na jornada |
| --- | --- | --- |
| `materials/conceituais/capitulo-11-atlas-sustentacao-como-gestao-de-risco.md` | Capítulo de livro | Capítulo 11 de *Gestão Sistêmica e Complexidade para Projetos de Software*, de Alisson Vale (Software Zen); fonte conceitual histórica da linguagem do framework, da crítica à manutenção tradicional e da definição dos riscos e sistemas de resposta. |
| `materials/conceituais/artigos-manutencao-agil-2019.md` | Série de artigos | Base histórica sobre manutenção ágil, uso de métodos como repertório, transição para sustentação, gestão de riscos e consciência sistêmica. |
| `materials/planilhas/Atlas - Painel de Controle - Dashboard_ Pronto-Atendimento.csv` | Dashboard CSV | Visão agregada do Sistema de Pronto-Atendimento, com DDP, volume, entradas e saídas. |
| `materials/planilhas/Atlas - Painel de Controle - Dashboard_ Adaptação e Aperfeiçoamento.csv` | Dashboard CSV | Visão agregada do Sistema de Adaptação e Aperfeiçoamento, com eficiência da programação, acréscimos e entregas. |
| `materials/planilhas/Atlas - Painel de Controle - S1_ Resposta Imediata.csv` | Planilha operacional CSV | Ciclos semanais de resposta imediata, com SLE de 8 horas, DDP, alocação e delays por etapa. |
| `materials/planilhas/Atlas - Painel de Controle - S2_ Resposta Rápida.csv` | Planilha operacional CSV | Ciclos semanais de resposta rápida, com SLE de referência de 48 horas, DDP, alocação e delays por etapa. |
| `materials/planilhas/Atlas - Painel de Controle - Resposta Programada.csv` | Planilha operacional CSV | Ciclos de resposta programada, com itens programados, extras, entregas, não concluídos e eficiência da programação. |
| `materials/planilhas/Atlas - Painel de Controle - _dados_resposta_imediata.csv` | Dados brutos CSV | Tickets S1 com tempos entre chegada, identificação, reação, correção e entrega. |
| `materials/planilhas/Atlas - Painel de Controle - _dados_resposta_rapida.csv` | Dados brutos CSV | Tickets S2 com tempos entre chegada, identificação, reação, correção, entrega e dias úteis. |
| `materials/planilhas/Atlas - Painel de Controle - _dados_resposta_programada.csv` | Dados brutos CSV | Tickets de resposta programada com datas de commit, desenvolvimento, teste e produção. |
| `materials/planilhas/Atlas - Painel de Controle - _parametros.csv` | Parâmetros CSV | SLEs e custos usados no painel: resposta imediata, resposta rápida, custo hora de desenvolvimento e suporte. |

## Materiais removidos

Planilhas experimentais enviadas por engano foram removidas do repositório e do contexto ativo da jornada. Elas não devem ser usadas como fonte do Atlas neste momento.

## Leitura inicial

O capítulo 11 do livro estabelece a mudança central de linguagem: sair de manutenção como reparo de objeto e entrar em sustentação como gestão de um ecossistema vivo, no momento em que a operação do cliente passa a depender do software para funcionar.

A série de artigos de 2019 aprofunda a origem do framework. Ela mostra que a resposta não é implantar Kanban, Scrum ou qualquer framework como receita, mas usar métodos como repertório para desenhar um sistema aderente à realidade concreta da sustentação.

As planilhas mostram que Atlas já não é apenas um ensaio conceitual. Há um painel operacional com sistemas de resposta, métricas, parâmetros, cadências semanais e dados brutos. A documentação canônica precisa preservar essa dupla natureza: framework de pensamento e instrumento de gestão.

## Conceitos extraídos

- Sustentação substitui manutenção como categoria principal.
- O marco de entrada em sustentação é a dependência operacional do cliente, não uma data de entrega.
- O gestor deixa de ser despachante de tíquetes e passa a ser arquiteto de sistemas sociotécnicos.
- A triagem técnica, feita por um gatekeeper, impede que poder político ou volume de reclamação substituam critério objetivo.
- R1 exige resposta imediata.
- R2 exige resposta rápida.
- R3 exige resposta programada, adaptativa e previsível.
- S1 e S2 compõem o Sistema de Pronto-Atendimento.
- O Sistema de Adaptação e Aperfeiçoamento cuida da resposta programada às adaptações planejáveis.
- SLE é a nomenclatura correta para expectativa de nível de serviço.
- O SLE de resposta rápida usado como referência é 48 horas, mas o valor deve ser decidido por quem aplica o framework.
- A fronteira entre sustentação adaptativa e desenvolvimento de novas capacidades precisa ser explícita.

## Lacunas abertas

- Separar o que pertence ao livro original, o que pertence ao framework Atlas e o que pertence a templates de adoção. A procedência do capítulo 11 está registrada no seu front matter.
- Definir como transformar o painel atual em template vivo sem confundir ferramenta com framework.
- Aprofundar a relação entre os cinco riscos dos artigos de 2019 e o recorte atual do Atlas.
