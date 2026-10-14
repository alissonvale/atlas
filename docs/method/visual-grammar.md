# Gramática visual

Este documento propõe uma linguagem visual para o Atlas.

Ele é separado do [Modelo conceitual](conceptual-model.md) e dos [Workflows das demandas](workflows.md). O método define conceitos, riscos, sistemas de resposta, etapas, métricas e políticas. A gramática visual escolhe como esses elementos aparecem em uma interface, conversa, painel, relatório ou ferramenta operacional.

## Fronteira de desenho

Componentes visuais ajudam a operar o Atlas, mas não definem o método.

Uma demanda R1 continua sendo R1 se aparecer como card, linha de tabela, alerta, registro de planilha ou resumo narrativo. Uma reclassificação continua sendo reclassificação mesmo sem animação, seta ou cor. A gramática visual torna a leitura mais rápida, mas a verdade metodológica permanece nos critérios de risco, nas políticas de resposta e nas evidências registradas.

## Direção visual

Atlas precisa mostrar quatro coisas antes do texto ser lido:

```text
qual risco está em jogo
qual sistema responde
em que estágio a demanda está
onde o tempo está sendo consumido
```

Ariad usa triângulos para exploração e blocos para entrega. Atlas precisa de outro centro visual: risco em movimento através de um sistema de resposta.

A forma primária proposta é o losango, porque ele sugere decisão, triagem, bifurcação e leitura de risco.

```text
△ Exploration: sinal, tensão, emergência de sentido
■ Delivery: compromisso delimitado, artefato verificável
◆ Atlas: risco classificado, resposta escolhida, fluxo operacional
```

## Conjunto provisório de símbolos

```text
◇ sinal ainda incerto
◆ sinal triado
◆R1 risco de perda imediata
◆R2 risco de operação bloqueada ou comprometida
◆R3 risco de adaptação planejável

↯ S1 resposta imediata
⇢ S2 resposta rápida
▦ Sistema de Adaptação e Aperfeiçoamento

⏱ SLE ativo
⌛ espera consumindo tempo
✓ dentro do SLE ou etapa concluída
✕ fora do SLE, bloqueio ou ruptura
◉ em acompanhamento ativo
○ pendente ou ainda não iniciado
↻ revisão e aprendizado
⇄ reclassificação entre sistemas
```

Esses símbolos são escolhas provisórias de renderização. Eles podem mudar conforme o Atlas amadurecer em ferramenta, painel ou documentação aplicada.

## Semântica de cor

As cores devem representar postura de resposta, não status genérico.

```text
vermelho    R1, S1, perda imediata, interrupção legítima
laranja     R2, S2, urgência real, janela crítica
azul        R3, Sistema de Adaptação e Aperfeiçoamento, adaptação planejável, ciclo programado
amarelo     classificação incerta, atenção, revisão necessária
verde       risco tratado, SLE cumprido, ciclo saudável
cinza       encerrado, histórico, contexto
preto       ruptura grave ou recorrência não aprendida
```

A paleta exata pertence à ferramenta ou interface. O método preserva apenas a semântica.

## Anatomia de um card Atlas

Um card Atlas deve deixar visível a relação entre risco, sistema, estágio e evidência.

```text
[forma][risco] título                           estado
  sistema: sistema de resposta escolhido
  etapa: estágio atual no workflow
  tempo: SLE, espera, lead time ou ciclo
  evidência: por que a leitura foi feita
  próximo movimento: decisão ou ação necessária
```

Exemplo:

```text
◆R2  Faturamento bloqueado                         ◉ ativo
  sistema: ⇢ S2 resposta rápida
  etapa: reação
  tempo: ⏱ SLE 48h ativo, maior espera em identificação
  evidência: operação financeira relevante não conclui
  próximo movimento: mobilizar correção e revisar impacto
```

## Superfícies principais

Atlas pode ter várias superfícies visuais. Cada superfície responde a uma pergunta operacional específica.

```text
Risk Intake
  Que sinal entrou e que evidência mínima existe?

Triage Gate
  Que risco esta demanda impõe ao negócio sustentado?

Response Flow
  Onde a demanda está dentro de S1 ou S2?

SLE Pulse
  Onde o tempo está sendo consumido em S1 ou S2?

Programmed Cycle
  Como está a saúde do ciclo de adaptação e aperfeiçoamento?

Reclassification
  Por que uma demanda mudou de sistema?

Learning Review
  Que ajuste sistêmico nasce do caso ou do ciclo?
```

## Risk Intake

`Risk Intake` mostra o sinal antes da decisão estabilizada.

Use quando:

- um sinal acabou de entrar;
- ainda não há classificação confiável;
- é preciso coletar evidência mínima para triagem;
- existe risco de responder à pressão antes de ler o risco.

```text
Atlas
╭────────────────────────────────────────────────────────╮
│        ◇  RISK INTAKE                                  │
│                                                        │
│  sinal                                                 │
│  Cliente não consegue concluir faturamento             │
│                                                        │
│  evidência                                             │
│  operação financeira bloqueada                         │
│                                                        │
│  leitura inicial                                       │
│  possível R2                                           │
│                                                        │
│  decisão necessária                                    │
│  confirmar se há perda imediata acumulando ou apenas   │
│  bloqueio operacional com janela relevante             │
╰────────────────────────────────────────────────────────╯
```

## Triage Gate

`Triage Gate` é a superfície central do Atlas. Ela mostra a fronteira entre ruído e sistema de resposta.

Use quando:

- uma demanda precisa entrar em S1, S2 ou Sistema de Adaptação e Aperfeiçoamento;
- uma classificação precisa ser justificada;
- há disputa entre urgência real e pressão política;
- a classificação está incerta e exige revisão explícita.

```text
Atlas
╭────────────────────────────────────────────────────────╮
│        ◆  TRIAGE GATE                                  │
│                                                        │
│  pergunta central                                      │
│  Que risco esta demanda impõe ao negócio sustentado?   │
│                                                        │
│  classificação                                         │
│  ◆R2 operação bloqueada ou comprometida                │
│                                                        │
│  sistema escolhido                                     │
│  ⇢ S2 resposta rápida                                  │
│                                                        │
│  justificativa                                         │
│  faturamento não está indisponível para todos, mas     │
│  uma operação relevante não consegue ser concluída     │
│                                                        │
│  SLE                                                   │
│  ⏱ 48 horas                                            │
│                                                        │
│  revisão                                               │
│  revisar se impacto financeiro começar a acumular      │
╰────────────────────────────────────────────────────────╯
```

## Response Flow

`Response Flow` mostra onde a demanda está dentro de S1 ou S2.

Use quando:

- uma demanda de pronto-atendimento está ativa;
- é preciso saber se o atraso está na identificação, reação, correção ou entrega;
- o Navigator precisa entender o estado sem ler todo o histórico do caso.

```text
Atlas
╭────────────────────────────────────────────────────────╮
│        ⇢  RESPONSE FLOW                                │
│                                                        │
│  demanda                                               │
│  #604312 faturamento bloqueado                         │
│                                                        │
│  sistema                                               │
│  ◆R2 -> ⇢ S2                                           │
│                                                        │
│  fluxo                                                 │
│  Chegada ✓                                             │
│  Identificação ✓                                       │
│  Reação ◉                                              │
│  Correção ○                                            │
│  Entrega ○                                             │
│                                                        │
│  tempo                                                 │
│  ⏱ SLE ativo                                           │
│  ⌛ maior espera até agora: reação                      │
╰────────────────────────────────────────────────────────╯
```

## SLE Pulse

`SLE Pulse` mostra a saúde temporal de S1 e S2.

Use quando:

- um ciclo de revisão observa S1 ou S2;
- o DDP caiu ou os casos fora do SLE aumentaram;
- é preciso distinguir atraso técnico de atraso sistêmico;
- o sistema precisa aprender onde o tempo vaza.

```text
Atlas
╭────────────────────────────────────────────────────────╮
│        ⏱  SLE PULSE                                    │
│                                                        │
│  sistema                                               │
│  ↯ S1 resposta imediata                                │
│                                                        │
│  ciclo                                                 │
│  Semana #2                                             │
│                                                        │
│  DDP                                                   │
│  33,33%                                                │
│                                                        │
│  dentro / fora                                         │
│  ✓ 1 dentro                                            │
│  ✕ 2 fora                                              │
│                                                        │
│  onde o tempo vazou                                    │
│  Identificação: 5h10                                   │
│  Reação: 18h39                                         │
│  Correção: 3h38                                        │
│  Entrega: 1h40                                         │
│                                                        │
│  leitura                                               │
│  o problema principal não é só correção técnica;       │
│  a resposta está perdendo tempo antes de agir          │
╰────────────────────────────────────────────────────────╯
```

## Programmed Cycle

`Programmed Cycle` é a superfície própria do Sistema de Adaptação e Aperfeiçoamento.

Use quando:

- um ciclo de adaptação está sendo planejado, acompanhado ou revisado;
- é preciso ver a relação entre itens programados, extras e entregas;
- a previsibilidade do Sistema de Adaptação e Aperfeiçoamento está sendo invadida por urgências ou escopo instável.

```text
Atlas
╭────────────────────────────────────────────────────────╮
│        ▦  PROGRAMMED CYCLE                             │
│                                                        │
│  sistema                                               │
│  ◆R3 -> ▦ Sistema de Adaptação e Aperfeiçoamento                                           │
│                                                        │
│  ciclo                                                 │
│  Agosto, Semana #1                                     │
│                                                        │
│  programação                                           │
│  itens programados: 17                                 │
│  extras: 7                                             │
│  entregues programados: 11                             │
│  entregues acrescidos: 7                               │
│  não concluídos: 6                                     │
│                                                        │
│  eficiência                                            │
│  75,00%                                                │
│                                                        │
│  leitura                                               │
│  o ciclo entregou, mas a entrada de extras revela      │
│  invasão parcial da programação                        │
╰────────────────────────────────────────────────────────╯
```

## Reclassification

`Reclassification` mostra uma mudança explícita de sistema.

Use quando:

- uma demanda muda de R3 para R2 ou R1;
- uma urgência é contida e volta para o Sistema de Adaptação e Aperfeiçoamento;
- uma demanda inicialmente urgente se revela planejável;
- é preciso proteger a mudança de sistema contra pressão política.

```text
Atlas
╭────────────────────────────────────────────────────────╮
│        ⇄  RECLASSIFICATION                             │
│                                                        │
│  demanda                                               │
│  Ajuste de regra fiscal                                │
│                                                        │
│  de                                                    │
│  ◆R3 -> ▦ Sistema de Adaptação e Aperfeiçoamento                                           │
│                                                        │
│  para                                                  │
│  ◆R2 -> ⇢ S2                                           │
│                                                        │
│  evidência nova                                        │
│  prazo legal próximo bloqueia emissão em operação      │
│  relevante                                             │
│                                                        │
│  cuidado                                               │
│  reclassificação aceita por mudança de risco, não por  │
│  pressão de prioridade                                 │
╰────────────────────────────────────────────────────────╯
```

## Learning Review

`Learning Review` mostra o aprendizado produzido por um caso, ciclo ou desvio relevante.

Use quando:

- um caso perdeu SLE;
- um padrão recorrente apareceu;
- o Sistema de Adaptação e Aperfeiçoamento perdeu previsibilidade;
- uma política, checklist, capacidade ou critério precisa ser ajustado.

```text
Atlas
╭────────────────────────────────────────────────────────╮
│        ↻  LEARNING REVIEW                              │
│                                                        │
│  origem                                                │
│  S2, três atrasos recorrentes em identificação         │
│                                                        │
│  padrão observado                                      │
│  suporte recebe o sinal cedo, mas evidência mínima     │
│  chega tarde ao gatekeeper                             │
│                                                        │
│  ajuste de sistema                                     │
│  revisar checklist de chegada para R2                  │
│                                                        │
│  efeito esperado                                       │
│  reduzir espera antes da reação sem aumentar falsas    │
│  urgências                                             │
╰────────────────────────────────────────────────────────╯
```

## Mapa compacto de fluxo

A gramática visual pode representar o fluxo geral assim:

```text
◇ sinal
  │
  ▼
◆ triagem
  ├─ ◆R1 -> ↯ S1 -> Chegada -> Identificação -> Reação -> Correção -> Entrega -> ↻
  ├─ ◆R2 -> ⇢ S2 -> Chegada -> Identificação -> Reação -> Correção -> Entrega -> ↻
  └─ ◆R3 -> ▦ Sistema de Adaptação e Aperfeiçoamento -> Qualificação -> Programação -> Desenvolvimento -> Teste -> Produção -> ↻
```

E o movimento entre sistemas assim:

```text
▦ Sistema de Adaptação e Aperfeiçoamento ⇄ ⇢ S2 ⇄ ↯ S1
      risco muda
      evidência muda
      classificação muda
```

## Uso da gramática visual

A gramática visual deve servir à leitura do sistema, não à decoração da ferramenta.

Ela é útil quando acelera perguntas como:

- o risco foi classificado ou ainda está incerto?
- a resposta escolhida combina com o risco?
- o caso está parado em qual etapa?
- o SLE está sendo consumido onde?
- a programação do Sistema de Adaptação e Aperfeiçoamento está saudável ou invadida?
- a mudança de sistema foi causada por evidência ou pressão?
- que aprendizado precisa fechar o ciclo?

O Atlas perde sua força quando vira planilha de controle. A visual grammar deve impedir essa redução. O objetivo não é deixar o quadro bonito. É fazer o risco, a resposta e o tempo aparecerem com clareza.
