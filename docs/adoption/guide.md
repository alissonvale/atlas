# Guia de adoção do Atlas

Este guia descreve uma adoção inicial do Atlas em um produto real.

A adoção não começa pela planilha. Começa pela leitura do sistema vivo que o produto sustenta.

## Preparar o contexto

Antes de definir fluxos e métricas, explicite:

- qual produto será sustentado;
- qual operação de negócio depende dele;
- quais perdas aparecem quando ele falha;
- quais áreas participam da sustentação;
- quais canais recebem demandas;
- quais decisões hoje são informais;
- onde a equipe sofre com urgência, interrupção ou imprevisibilidade.

## Mapear riscos

Classifique exemplos reais recentes em R1, R2 e R3.

Use incidentes, tickets, pedidos de melhoria, bugs, atrasos, reclamações e mudanças legais ou operacionais. O objetivo não é criar uma taxonomia perfeita. O objetivo é treinar a organização a ver naturezas diferentes de risco.

## Definir o gatekeeper

Estabeleça quem faz a triagem e com quais critérios.

A função pode começar simples. Uma pessoa ou pequeno grupo pode assumir a triagem inicial, desde que registre classificação, justificativa e encaminhamento.

## Desenhar S1 e S2

Para S1 e S2, defina:

- critérios de entrada;
- SLE de cada sistema;
- capacidade dedicada ou mobilizável;
- fila ou canal de trabalho;
- responsáveis;
- etapas mínimas do fluxo;
- forma de medir DDP;
- cadência de revisão.

Use 8 horas para S1 e 48 horas para S2 apenas como referências iniciais do material original. O valor certo depende do contexto.

## Desenhar S3

Para S3, defina:

- cadência de programação;
- quem seleciona demandas;
- como capacidade é considerada;
- como extras entram ou são recusados;
- como entregas são registradas;
- como medir eficiência da programação;
- como revisar desvios.

S3 precisa ser protegido. Se toda demanda entra no meio do ciclo, a programação deixa de ser programação e vira teatro.

## Usar as planilhas

As planilhas originais podem cumprir dois papéis.

Elas ajudam a entender a origem concreta do método, porque mostram uma aplicação real do Atlas. Também podem servir como base para templates, desde que sejam adaptadas ao contexto e não copiadas mecanicamente.

A adoção deve extrair delas a lógica operacional, não apenas replicar abas.

## Revisar depois do primeiro ciclo

Após o primeiro ciclo de uso, revise:

- se a triagem distinguiu bem R1, R2 e R3;
- se os SLEs foram realistas;
- se DDP revelou gargalos úteis;
- se S3 conseguiu manter programação;
- se a equipe entendeu a diferença entre urgência real e pressão;
- se o negócio percebeu mais clareza no atendimento;
- se alguma regra precisa ser simplificada.

A primeira adoção do Atlas deve ser pequena o bastante para aprender e concreta o bastante para doer onde o sistema realmente falha.
