# Métricas e sinais de saúde

Atlas usa métricas como escuta sistêmica.

Uma métrica não deve ser tratada como instrumento de culpa. Ela é um sinal. Quando o sinal se repete, o sistema está pedindo revisão.

## SLE

SLE significa Service Level Expectation.

No Atlas, SLE é a expectativa explícita de resposta de um sistema. Ele ajuda a desenhar capacidade, priorização, cadência e revisão.

SLE não é valor universal. Cada contexto define o que faz sentido para S1 e S2, considerando criticidade do negócio, capacidade disponível, horário de operação, custo de atraso e maturidade da equipe.

O material original usa 8 horas como referência para S1. Para S2, a referência validada é 48 horas. Esses valores são exemplos de uma aplicação concreta, não regras fixas do framework.

## DDP

DDP significa Due Date Performance.

DDP mede o percentual de demandas concluídas dentro do SLE esperado.

Em S1 e S2, DDP responde à pergunta:

> O sistema está conseguindo responder dentro da expectativa que ele mesmo assumiu?

Quando DDP cai, o Atlas não procura culpados. Ele procura causas sistêmicas.

Possíveis causas:

- triagem lenta;
- identificação imprecisa;
- capacidade insuficiente;
- dependências externas;
- excesso de interrupções;
- SLE irrealista;
- critérios frouxos de entrada;
- gargalos na correção, teste, homologação ou entrega.

## Eficiência da programação

Eficiência da programação mede a relação entre o que foi programado para um ciclo e o que foi efetivamente entregue.

Ela é central para o Sistema de Adaptação e Aperfeiçoamento porque a resposta programada depende de previsibilidade.

A baixa eficiência da programação pode revelar:

- acréscimos frequentes no meio do ciclo;
- programação maior do que a capacidade real;
- estimativas frágeis;
- dependências não consideradas;
- invasão de S1 e S2 sobre o Sistema de Adaptação e Aperfeiçoamento;
- desalinhamento entre seleção de demandas e delivery;
- falta de clareza sobre pronto, entregue e concluído.

## Métrica como pergunta

Cada métrica do Atlas deve virar pergunta de melhoria.

Quando uma demanda S1 fica fora do SLE, a pergunta não é quem atrasou. A pergunta é onde o sistema perdeu tempo e por quê.

Quando S2 acumula atrasos, a pergunta não é por que a equipe não foi mais rápida. A pergunta é se a triagem, a fila, a capacidade e as dependências estão desenhadas para o risco assumido.

Quando o Sistema de Adaptação e Aperfeiçoamento perde eficiência, a pergunta não é por que o time não cumpriu o combinado. A pergunta é se o combinado era realista e se o sistema foi protegido para cumpri-lo.

## Sinais mínimos de saúde

Um sistema Atlas saudável tende a mostrar:

- critérios de triagem compreendidos;
- SLEs explícitos e revisáveis;
- DDP acompanhado em S1 e S2;
- eficiência da programação acompanhada no Sistema de Adaptação e Aperfeiçoamento;
- revisão dos casos fora da expectativa;
- aprendizado convertido em mudança de processo;
- menor dependência de heroísmo;
- maior previsibilidade sem perda de responsividade.
