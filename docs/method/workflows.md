# Workflows das demandas

Atlas não trata workflow como uma sequência universal e rígida.

O workflow é a forma visível que um sistema de resposta assume em um contexto. Ele não existe para padronizar todos os trabalhos em uma fila única. Existe para tornar explícito onde a demanda está, que risco está sendo tratado, que decisão precisa acontecer e onde o tempo do sistema está sendo consumido.

Nos materiais originais aparecem dois desenhos principais: o fluxo do Sistema de Pronto-Atendimento, usado por S1 e S2, e o fluxo do Sistema de Adaptação e Aperfeiçoamento.

## Visão geral dos sistemas

| Sistema | Risco tratado | Ritmo | Workflow-base |
| --- | --- | --- | --- |
| S1, resposta imediata | R1, perda imediata de valor relevante | Prontidão imediata | Chegada -> Identificação -> Reação -> Correção -> Entrega |
| S2, resposta rápida | R2, operação bloqueada ou comprometida | Prioridade rápida | Chegada -> Identificação -> Reação -> Correção -> Entrega |
| Sistema de Adaptação e Aperfeiçoamento | R3, adaptação planejável | Programação explícita | Programação -> Desenvolvimento -> Teste -> Produção |

S1 e S2 compartilham o mesmo desenho de etapas porque ambos pertencem ao Sistema de Pronto-Atendimento. A diferença entre eles não está no nome das colunas, mas na natureza do risco, na regra de interrupção, no SLE, na intensidade de acompanhamento e no tipo de decisão que cada etapa exige.

O Sistema de Adaptação e Aperfeiçoamento não é a terceira fila de atendimento. É o sistema que protege a adaptação planejável do produto. Ele recebe demandas que podem ser programadas sem dano imediato relevante ao negócio.

## A fronteira antes do workflow

Toda demanda passa por uma fronteira anterior ao fluxo de execução: a triagem.

A triagem responde à pergunta central do Atlas:

> Que risco esta demanda impõe ao negócio sustentado pelo produto?

A saída da triagem define o sistema de resposta inicial:

| Classificação | Encaminhamento | Decisão produzida |
| --- | --- | --- |
| R1 | S1 | Interromper, mobilizar imediatamente e conter perda |
| R2 | S2 | Priorizar rapidamente e proteger janela relevante |
| R3 | Sistema de Adaptação e Aperfeiçoamento | Programar em ciclo e preservar previsibilidade |
| Incerta | Revisão explícita | Investigar evidências antes de estabilizar a classificação |

A triagem não encerra a leitura do risco. Ela cria uma hipótese operacional. Uma demanda pode mudar de sistema quando novas evidências mostram que o risco foi lido de forma incompleta ou mudou de natureza.

## Workflow de S1: resposta imediata

S1 é usado quando há perda imediata de valor relevante enquanto o problema persiste. O sistema precisa entrar em prontidão, reduzir o dano e restaurar a operação.

```text
Chegada -> Identificação -> Reação -> Correção -> Entrega -> Encerramento
```

### Chegada

Chegada é o momento em que o sinal entra no sistema.

Pode vir de suporte, cliente, monitoramento, usuário, operação interna ou liderança. Neste ponto, ainda não há necessariamente clareza sobre a natureza do risco.

Em S1, a chegada precisa registrar o horário de entrada, a origem do sinal, o sintoma observado e a evidência mínima do dano em curso. A pergunta não é apenas o que aconteceu. É que perda está se acumulando enquanto o problema permanece aberto.

Saída esperada da etapa:

- sinal registrado;
- horário de entrada preservado;
- evidências mínimas coletadas;
- demanda colocada em triagem imediata.

### Identificação

Identificação é a etapa em que o sinal é compreendido e classificado.

Em S1, a identificação confirma se existe R1. O gatekeeper, com apoio técnico quando necessário, verifica se há perda imediata, interrupção crítica, risco regulatório, risco de confiança, perda financeira, indisponibilidade relevante ou dano operacional acumulando.

A demora na identificação é uma causa possível de perda do SLE. Isso mostra que a saúde de S1 não depende apenas da velocidade técnica de corrigir, mas da capacidade do sistema de reconhecer emergência a tempo.

Saída esperada da etapa:

- classificação R1 confirmada ou revista;
- SLE aplicável definido;
- responsável inicial nomeado;
- regra de interrupção acionada quando necessário;
- comunicação mínima iniciada com quem depende da resposta.

### Reação

Reação é o momento em que o sistema mobiliza resposta.

Em S1, reação significa prontidão imediata. A demanda não deve disputar atenção com trabalho programado comum. A reação pode envolver acionar desenvolvedor, suporte, liderança técnica, pessoa especialista, ambiente de investigação, comunicação com o cliente, rollback, plano de contenção ou sala de crise proporcional ao risco.

O tempo entre identificação e reação revela se a organização tem capacidade mobilizável ou se depende de improviso.

Saída esperada da etapa:

- pessoa ou grupo responsável mobilizado;
- interrupção registrada quando afetar trabalho planejado;
- caminho de contenção ou correção definido;
- próximo ponto de acompanhamento conhecido.

### Correção

Correção é a intervenção que resolve ou contém o problema.

Pode ser alteração de código, ajuste de configuração, procedimento operacional, restauração de dados, rollback, mitigação temporária, desativação controlada de funcionalidade ou outra ação técnica. Em S1, conter a perda pode ser mais importante que resolver definitivamente a causa raiz no primeiro movimento.

Saída esperada da etapa:

- perda contida ou correção aplicada;
- decisão registrada entre solução definitiva e contorno temporário;
- risco residual explicitado;
- necessidade de ação posterior identificada.

### Entrega

Entrega é o momento em que a solução ou contenção chega ao ambiente onde o risco é reduzido.

Pode envolver deploy, validação operacional, confirmação com suporte, comunicação com cliente, restauração de operação, monitoramento pós-ação ou aceite de quem foi afetado. A demanda não está entregue apenas porque a alteração técnica terminou. Ela está entregue quando o risco R1 foi reduzido a um nível aceitável.

Saída esperada da etapa:

- operação restaurada ou perda interrompida;
- confirmação mínima obtida;
- status de SLE registrado como dentro ou fora;
- causa principal de atraso registrada quando houver perda de SLE.

### Encerramento

Encerramento transforma o caso em aprendizado.

Em S1, nem todo caso exige uma análise pesada, mas todo desvio relevante precisa deixar sinal. O encerramento observa se a classificação foi correta, onde o tempo foi consumido, se a interrupção foi legítima, se o SLE protegeu o negócio e se há recorrência que deveria virar melhoria técnica, ajuste de triagem ou mudança de capacidade.

Saída esperada da etapa:

- caso encerrado;
- causa de perda de SLE registrada, quando houver;
- aprendizado mínimo capturado;
- follow-up criado quando a contenção não elimina a causa.

## Workflow de S2: resposta rápida

S2 é usado quando há urgência real, mas não perda imediata contínua no mesmo grau de S1. A operação está bloqueada ou comprometida, uma janela relevante precisa ser preservada, ou uma consequência séria pode emergir se a resposta atrasar.

```text
Chegada -> Identificação -> Reação -> Correção -> Entrega -> Encerramento
```

S2 usa as mesmas etapas de S1, mas com outra política de ritmo. Ele não deve interromper tudo como emergência, mas também não pode cair na fila comum de itens programáveis.

### Chegada

A chegada de S2 registra o sinal, o horário, a origem, a operação afetada e a janela de urgência. A evidência central é o bloqueio ou comprometimento operacional, não a intensidade emocional da solicitação.

Saída esperada da etapa:

- demanda registrada;
- operação afetada descrita;
- janela relevante identificada;
- triagem rápida iniciada.

### Identificação

A identificação confirma se o caso é R2 ou se deve subir para S1, seguir para o Sistema de Adaptação e Aperfeiçoamento ou aguardar mais evidências.

Uma demanda tende a permanecer em S2 quando pode aguardar brevemente, mas precisa ficar acima das demandas programáveis. Se há perda imediata acumulando, sobe para S1. Se não há urgência real, volta para o Sistema de Adaptação e Aperfeiçoamento.

Saída esperada da etapa:

- classificação R2 confirmada ou revista;
- SLE definido;
- justificativa breve registrada;
- responsável inicial indicado;
- momento de revisão definido quando houver incerteza.

### Reação

A reação de S2 coloca a demanda em prioridade rápida.

Ela pode acionar capacidade técnica, suporte, análise, comunicação com cliente ou preparação de ambiente. A diferença para S1 é que a mobilização deve ser rápida e protegida, mas não necessariamente imediata a ponto de suspender toda a operação.

Saída esperada da etapa:

- prioridade reconhecida;
- capacidade alocada ou reservada;
- sequência de atendimento definida;
- impacto sobre trabalho programado registrado se houver.

### Correção

A correção trata a causa ou remove o bloqueio operacional.

S2 também pode usar contornos, ajustes operacionais, configuração, correção técnica ou orientação ao usuário. O critério é reduzir o risco dentro da janela útil, sem transformar uma urgência em emergência artificial.

Saída esperada da etapa:

- bloqueio removido ou risco reduzido;
- correção ou contorno aplicado;
- risco residual conhecido;
- próxima ação definida quando necessário.

### Entrega

A entrega confirma que a operação pode seguir.

Pode envolver disponibilização em produção, comunicação com suporte, validação com usuário, confirmação do cliente ou registro de procedimento. O trabalho é entregue quando a urgência que justificou S2 deixou de governar a demanda.

Saída esperada da etapa:

- operação desbloqueada ou janela preservada;
- confirmação mínima obtida;
- status de SLE registrado;
- causa de atraso registrada quando houver.

### Encerramento

O encerramento de S2 observa se a urgência foi legítima e se o sistema respondeu no ritmo adequado.

A pergunta de aprendizado é se S2 protegeu o negócio sem virar atalho político para acelerar demanda comum. Casos recorrentes de S2 podem revelar problema estrutural que precisa ir para o Sistema de Adaptação e Aperfeiçoamento como melhoria programada ou para desenvolvimento se exigir nova capacidade relevante.

Saída esperada da etapa:

- caso encerrado;
- legitimidade da classificação revisada quando necessário;
- causa de perda de SLE registrada;
- melhoria ou ajuste sistêmico criado quando houver recorrência.

## Workflow do Sistema de Adaptação e Aperfeiçoamento

O Sistema de Adaptação e Aperfeiçoamento Ele responde a R3, risco de adaptação. Seu foco é preservar a capacidade do produto de continuar aderente à operação do negócio com previsibilidade.

```text
Entrada R3 -> Qualificação -> Programação -> Desenvolvimento -> Teste -> Produção -> Encerramento
```

As planilhas originais simplificam esse fluxo como:

```text
Programação -> Desenvolvimento -> Teste -> Produção
```

A documentação do framework explicita duas fronteiras adicionais. Antes da programação existe a entrada qualificada de R3. Depois da produção existe o encerramento como aprendizado sobre previsibilidade, capacidade e aderência.

### Entrada R3

Entrada R3 é o momento em que uma demanda planejável entra no território de adaptação.

Ela pode nascer de solicitação de cliente, mudança legal, necessidade operacional, melhoria de funcionalidade existente, redução de atrito, ajuste de regra, obsolescência percebida ou aprendizado vindo de S1 e S2.

Saída esperada da etapa:

- demanda registrada como candidata a R3;
- vínculo com necessidade de negócio descrito;
- ausência de urgência imediata confirmada;
- origem identificada, inclusive quando vier de recorrência em S1 ou S2.

### Qualificação

Qualificação transforma uma demanda planejável em item possível de programação.

Aqui o sistema decide se o item pertence mesmo à sustentação adaptativa ou se exige desenvolvimento de nova capacidade relevante. Também esclarece escopo mínimo, benefício esperado, risco de não fazer, dependências e critérios de conclusão.

Saída esperada da etapa:

- item qualificado para programação ou retirado do fluxo;
- critério de conclusão definido;
- esforço ou complexidade em nível suficiente para programação;
- dependências conhecidas;
- fronteira com desenvolvimento de novas capacidades revisada.

### Programação

Programação é a composição explícita do ciclo de trabalho.

Ela define quais itens entram no ciclo, quais são extras, qual capacidade está disponível e qual compromisso será observado. A programação é a fronteira que protege o Sistema de Adaptação e Aperfeiçoamento de virar fila reativa.

Saída esperada da etapa:

- ciclo definido;
- itens programados escolhidos;
- capacidade disponível explicitada;
- compromisso de entrega visível;
- critério para entrada de extras acordado.

### Desenvolvimento

Desenvolvimento é a etapa de implementação do item programado.

Pode envolver análise, alteração de código, ajuste de regra, melhoria técnica ou adaptação funcional. O ponto importante é que o item pertence a uma capacidade existente ou a uma adaptação planejável. Se ele exige criação de nova capacidade relevante, pode pertencer a um fluxo de desenvolvimento, não à sustentação adaptativa.

Saída esperada da etapa:

- mudança implementada;
- touch time capturado quando aplicável;
- impedimentos e esperas registrados;
- desvio de escopo identificado quando ocorrer.

### Teste

Teste é a etapa de verificação da mudança.

Ele protege o produto contra o retorno de riscos mais graves. Em sustentação, teste não é apenas garantia técnica. É proteção da operação viva que depende do produto.

Saída esperada da etapa:

- mudança verificada;
- risco de regressão reduzido;
- pendências explicitadas;
- item liberado para produção ou devolvido para desenvolvimento.

### Produção

Produção é a disponibilização da adaptação.

É nesse ponto que o sistema observa se o que foi programado chegou ao uso, se ficou dentro do compromisso do ciclo e se contribuiu para a aderência do produto à operação.

Saída esperada da etapa:

- adaptação disponibilizada;
- entrega classificada como programada entregue, acrescida entregue ou não concluída;
- lead time registrado quando aplicável;
- confirmação de uso ou disponibilidade obtida.

### Encerramento

Encerramento observa a saúde do ciclo.

O Sistema de Adaptação e Aperfeiçoamento aprende pela diferença entre o que foi programado, o que foi acrescentado, o que foi entregue e o que não foi concluído. O objetivo não é punir variação. É entender se a programação protege a previsibilidade ou se está sendo invadida por urgências, escopo instável, capacidade insuficiente ou critérios frágeis de seleção.

Saída esperada da etapa:

- item encerrado;
- status final registrado;
- eficiência da programação atualizada;
- causas de desvio relevantes capturadas;
- ajustes de seleção, capacidade ou política criados quando necessário.

## Status operacionais sugeridos

As etapas conceituais podem ser traduzidas em status operacionais. Os nomes podem variar por ferramenta, mas a semântica deve ser preservada.

| Sistema | Status sugeridos |
| --- | --- |
| S1 | Novo sinal, em identificação, R1 confirmado, resposta mobilizada, em correção/contenção, em entrega/validação, encerrado |
| S2 | Novo sinal, em identificação, R2 confirmado, priorizado, em correção, em entrega/validação, encerrado |
| Sistema de Adaptação e Aperfeiçoamento | Candidato R3, qualificado, programado, em desenvolvimento, em teste, pronto para produção, entregue, encerrado |

A organização pode colapsar etapas quando o volume é baixo, mas não deve apagar as decisões. Um quadro simples pode ter poucas colunas desde que preserve os marcos: classificação do risco, mobilização ou programação, execução, entrega e aprendizado.

## Movimento entre sistemas

Demandas podem mudar de sistema quando a leitura do risco muda.

| Movimento | Quando acontece | Cuidado de governança |
| --- | --- | --- |
| Sistema de Adaptação e Aperfeiçoamento -> S2 | Uma demanda planejável passa a bloquear operação ou ganha janela crítica real | Registrar evidência nova, não apenas pressão |
| Sistema de Adaptação e Aperfeiçoamento -> S1 | A postergação passa a gerar perda imediata relevante | Acionar interrupção e revisar por que o risco envelheceu |
| S2 -> S1 | A urgência revela perda imediata em curso | Trocar SLE e mobilização sem apagar histórico |
| S1 -> S2 | A perda imediata foi contida, mas ainda há urgência residual | Separar contenção de resolução completa |
| S1/S2 -> Sistema de Adaptação e Aperfeiçoamento | O caso foi contido e resta melhoria planejável | Criar item de adaptação sem manter falsa urgência |
| Sistema de Adaptação e Aperfeiçoamento -> desenvolvimento | A demanda exige nova capacidade relevante, não adaptação de capacidade existente | Proteger a fronteira entre sustentação e evolução maior do produto |

Reclassificação deve ser evento explícito. Sem justificativa, a mudança de sistema vira instrumento de pressão. Com justificativa, ela vira aprendizado sobre risco.

## Tempos do sistema

As planilhas distinguem tempos importantes:

- wait time, tempo de espera entre etapas;
- touch time, tempo de trabalho efetivo;
- lead time, tempo total produzido pelo sistema.

Essa distinção é essencial para o Atlas. A entrega não acontece no tempo que uma pessoa levaria trabalhando isoladamente. Ela acontece no tempo que o sistema produz.

Em S1 e S2, a leitura principal é onde o SLE foi consumido: identificação, reação, correção ou entrega. No Sistema de Adaptação e Aperfeiçoamento, a leitura principal é a diferença entre capacidade programada, trabalho efetivo, espera e conclusão do ciclo.

## Uso dos workflows

Os workflows devem servir a três propósitos:

- tornar visível onde o tempo é consumido;
- revelar gargalos e atrasos recorrentes;
- orientar mudanças de desenho no sistema.

O objetivo não é preencher colunas. É aprender onde a sustentação perde prontidão, previsibilidade ou consciência sistêmica.
