# Anexos

Este índice registra os materiais usados para construir o Atlas e separa fonte bruta, leitura inicial e decisões derivadas.

## Materiais recebidos

| Material | Tipo | Uso na jornada |
| --- | --- | --- |
| `materials/descritivo-atlas.txt` | Texto conceitual | Fonte principal da linguagem do método, da crítica à manutenção tradicional e da definição dos riscos e sistemas de resposta. |
| `materials/planilhas/Atlas - Painel de Controle - Dashboard_ Pronto-Atendimento.csv` | Dashboard CSV | Visão agregada do Sistema de Pronto-Atendimento, com DDP, volume, entradas e saídas. |
| `materials/planilhas/Atlas - Painel de Controle - Dashboard_ Adaptação e Aperfeiçoamento.csv` | Dashboard CSV | Visão agregada do Sistema de Adaptação e Aperfeiçoamento, com eficiência da programação, acréscimos e entregas. |
| `materials/planilhas/Atlas - Painel de Controle - S1_ Resposta Imediata.csv` | Planilha operacional CSV | Ciclos semanais de resposta imediata, com SLE de 8 horas, DDP, alocação e delays por etapa. |
| `materials/planilhas/Atlas - Painel de Controle - S2_ Resposta Rápida.csv` | Planilha operacional CSV | Ciclos semanais de resposta rápida, com SLE de referência de 48 horas, DDP, alocação e delays por etapa. |
| `materials/planilhas/Atlas - Painel de Controle - S3_ Resposta Programada.csv` | Planilha operacional CSV | Ciclos de resposta programada, com itens programados, extras, entregas, não concluídos e eficiência da programação. |
| `materials/planilhas/Atlas - Painel de Controle - _dados_resposta_imediata.csv` | Dados brutos CSV | Tickets S1 com tempos entre chegada, identificação, reação, correção e entrega. |
| `materials/planilhas/Atlas - Painel de Controle - _dados_resposta_rapida.csv` | Dados brutos CSV | Tickets S2 com tempos entre chegada, identificação, reação, correção, entrega e dias úteis. |
| `materials/planilhas/Atlas - Painel de Controle - _dados_resposta_programada.csv` | Dados brutos CSV | Tickets S3 com datas de commit, desenvolvimento, teste e produção. |
| `materials/planilhas/Atlas - Painel de Controle - _parametros.csv` | Parâmetros CSV | SLEs e custos usados no painel: resposta imediata, resposta rápida, custo hora de desenvolvimento e suporte. |

## Materiais removidos

As planilhas de S4 e S5 foram enviadas por engano e removidas do repositório e do contexto ativo da jornada:

- `Atlas - Painel de Controle - S4_ Resposta Projetizada.csv`
- `Atlas - Painel de Controle - S5_ Resposta Disciplinada.csv`

S4 e S5 eram experimentais e não devem ser tratados como parte do Atlas neste momento.

## Leitura inicial

O descritivo estabelece a mudança central de linguagem: sair de manutenção como reparo de objeto e entrar em sustentação como gestão de um ecossistema vivo, no momento em que a operação do cliente passa a depender do software para funcionar.

As planilhas mostram que Atlas já não é apenas um ensaio conceitual. Há um painel operacional com sistemas de resposta, métricas, parâmetros, cadências semanais e dados brutos. A documentação canônica precisa preservar essa dupla natureza: método de pensamento e instrumento de gestão.

## Conceitos extraídos

- Sustentação substitui manutenção como categoria principal.
- O marco de entrada em sustentação é a dependência operacional do cliente, não uma data de entrega.
- O gestor deixa de ser despachante de tíquetes e passa a ser arquiteto de sistemas sociotécnicos.
- A triagem técnica, feita por um gatekeeper, impede que poder político ou volume de reclamação substituam critério objetivo.
- R1 exige resposta imediata.
- R2 exige resposta rápida.
- R3 exige resposta programada, adaptativa e previsível.
- S1 e S2 compõem o Sistema de Pronto-Atendimento.
- S3 compõe o Sistema de Adaptação e Aperfeiçoamento.
- SLE é a nomenclatura correta para expectativa de nível de serviço.
- O SLE de resposta rápida usado como referência é 48 horas, mas o valor deve ser decidido por quem aplica o método.

## Lacunas abertas

- Separar o que pertence ao livro original, o que pertence ao método Atlas e o que pertence a templates de adoção.
- Definir se o painel atual deve ser convertido em template vivo do método ou preservado apenas como material histórico/contextual.
- Definir o próximo documento canônico após o modelo conceitual inicial.
