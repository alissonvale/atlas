# Workflows das demandas

Atlas não trata workflow como uma sequência universal e rígida.

O workflow é a forma visível que um sistema de resposta assume em um contexto. As planilhas originais e o descritivo do método permitem inferir dois desenhos principais: o fluxo do Sistema de Pronto-Atendimento e o fluxo do Sistema de Adaptação e Aperfeiçoamento.

## Sistema de Pronto-Atendimento

S1 e S2 compartilham o mesmo desenho básico de fluxo. A diferença está no risco, na prioridade e no SLE.

S1 responde a emergências. S2 responde a urgências. Ambos precisam medir onde o tempo é consumido, porque o atraso pode estar antes da correção técnica, não nela.

Workflow inferido:

```text
Chegada -> Identificação -> Reação -> Correção -> Entrega
```

## Chegada

Chegada é o momento em que o sinal entra no sistema.

Pode vir de suporte, cliente, monitoramento, usuário, operação interna ou liderança. Neste ponto, ainda não há necessariamente clareza sobre a natureza do risco.

O cuidado principal é registrar o horário de entrada e coletar evidências mínimas para triagem.

## Identificação

Identificação é a etapa em que o sinal é compreendido e classificado.

Aqui o gatekeeper, com apoio técnico quando necessário, distingue emergência, urgência e demanda programável. Nas planilhas, a demora na identificação aparece como uma causa possível de perda do SLE. Isso é relevante porque mostra que o problema do sistema nem sempre está na capacidade de corrigir, mas na capacidade de reconhecer o risco a tempo.

## Reação

Reação é o momento em que o sistema mobiliza resposta.

Em S1, reação significa prontidão imediata. Em S2, significa priorização rápida. A reação pode envolver acionar desenvolvedor, suporte, liderança técnica, pessoa especialista, ambiente de investigação ou comunicação com o cliente.

O tempo entre identificação e reação revela se o sistema tem capacidade mobilizável ou se depende de improviso.

## Correção

Correção é a intervenção que resolve ou contém o problema.

Pode ser correção de código, ajuste de configuração, procedimento operacional, contorno temporário, rollback, restauração de dados ou outra ação técnica. Em Atlas, a correção não deve ser analisada isoladamente. Um caso pode ter correção rápida e ainda assim perder SLE por identificação tardia ou reação lenta.

## Entrega

Entrega é o momento em que a solução ou contenção chega ao ambiente onde o risco é reduzido.

Pode envolver deploy, comunicação, validação com suporte, confirmação do cliente ou restauração da operação. A demanda só deve ser considerada concluída quando o risco que motivou a resposta foi tratado em nível adequado ao sistema.

## Sistema de Adaptação e Aperfeiçoamento

O Sistema de Adaptação e Aperfeiçoamento lida com demandas programáveis ligadas a R3.

Ele não usa o mesmo ritmo do pronto-atendimento. Seu foco é previsibilidade, programação explícita e aprendizado sobre capacidade real.

Workflow inferido das planilhas:

```text
Programação -> Desenvolvimento -> Teste -> Produção
```

As planilhas também registram commit, wait time, touch time, lead time e status. Esses campos ajudam a distinguir o tempo de execução do tempo produzido pelo sistema.

## Programação

Programação é a composição explícita do ciclo de trabalho.

Ela define quais itens entram no ciclo, quais são extras, qual capacidade está disponível e qual compromisso será observado. A programação é a fronteira que protege a resposta adaptativa de virar fila reativa.

## Desenvolvimento

Desenvolvimento é a etapa de implementação do item programado.

Pode envolver análise, alteração de código, ajuste de regra, melhoria técnica ou adaptação funcional. O ponto importante é que o item pertence a uma capacidade existente ou a uma adaptação planejável. Se ele exige criação de nova capacidade relevante, pode pertencer a um fluxo de desenvolvimento, não à sustentação adaptativa.

## Teste

Teste é a etapa de verificação da mudança.

Ela protege o produto contra o retorno de riscos mais graves. Em sustentação, teste não é apenas garantia técnica. É proteção da operação viva que depende do produto.

## Produção

Produção é a disponibilização da adaptação.

É nesse ponto que o sistema observa se o que foi programado chegou ao uso, se ficou dentro do compromisso do ciclo e se contribuiu para a aderência do produto à operação.

## Tempos do sistema

As planilhas distinguem tempos importantes:

- wait time, tempo de espera entre etapas;
- touch time, tempo de trabalho efetivo;
- lead time, tempo total produzido pelo sistema.

Essa distinção é essencial para o Atlas. A entrega não acontece no tempo que uma pessoa levaria trabalhando isoladamente. Ela acontece no tempo que o sistema produz.

## Uso dos workflows

Os workflows devem servir a três propósitos:

- tornar visível onde o tempo é consumido;
- revelar gargalos e atrasos recorrentes;
- orientar mudanças de desenho no sistema.

O objetivo não é preencher colunas. É aprender onde a sustentação perde prontidão, previsibilidade ou consciência sistêmica.
