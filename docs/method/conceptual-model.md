# Modelo conceitual

## Sustentação, não manutenção

Atlas substitui a linguagem de manutenção pela linguagem de sustentação.

Manutenção sugere um objeto entregue que precisa ser corrigido depois. Sustentação sugere um sistema vivo que precisa continuar apoiando uma operação real. A diferença não é estética. Ela muda o objeto da gestão.

Na manutenção, o foco tende a cair sobre o software. Na sustentação, o foco se desloca para a relação entre software e negócio.

## Marco de entrada em sustentação

Um produto entra em estado de sustentação quando a operação de negócio do cliente passa a depender dele para funcionar.

Esse é o ponto de virada do método. A sustentação não começa depois de uma entrega formal. Ela começa quando o software se torna parte da operação viva.

## Gestão orientada a risco operacional

Atlas organiza a sustentação pela leitura do risco operacional.

A pergunta de triagem não é somente "qual é o problema técnico?". A pergunta é "que tipo de risco esta situação impõe ao negócio sustentado pelo produto?".

Essa leitura impede que tudo vire uma única fila de urgências. Demandas diferentes pedem sistemas de resposta diferentes.

## Riscos

### R1: risco de perda imediata

R1 aparece quando o negócio perde valor relevante a cada momento de mau funcionamento. Pode envolver dinheiro, credibilidade, qualidade percebida, engajamento, dados críticos ou continuidade operacional.

O custo do atraso é imediato, linear e cumulativo. A resposta precisa ser imediata.

### R2: risco de operação bloqueada ou comprometida

R2 aparece quando uma operação de negócio não consegue ser concluída ou fica seriamente comprometida, gerando custo, ineficiência ou risco de consequência relevante.

Não há necessariamente uma perda a cada minuto, mas há uma janela curta de resposta antes que o impacto se torne grave. A resposta precisa ser rápida.

### R3: risco de adaptação

R3 aparece quando o produto precisa acompanhar novas necessidades de negócio, legislação, mercado, eficiência operacional ou melhoria de funcionalidades existentes.

O risco não é a falha imediata, mas a obsolescência, a perda progressiva de aderência e o acúmulo de demandas planejáveis que podem virar urgência se forem negligenciadas.

## Sistemas de resposta

### S1: resposta imediata

S1 responde a R1. Seu propósito é conter perdas imediatas e restaurar a operação com a maior prontidão possível.

A planilha original usa um SLE de 8 horas para resposta imediata.

### S2: resposta rápida

S2 responde a R2. Seu propósito é priorizar urgências reais sem tratá-las como emergências permanentes.

A planilha original registra resposta rápida com referência de 48 horas ou 3 dias, ponto que precisa ser normalizado na documentação canônica.

### S3: resposta programada

S3 responde a R3. Seu propósito é manter previsibilidade de adaptação e aperfeiçoamento.

A métrica central identificada no material é a eficiência da programação, relacionando o que foi programado para um ciclo com o que foi efetivamente entregue.

### S4: resposta projetizada

S4 aparece nas planilhas como sistema de resposta projetizada. Ele parece lidar com entregáveis maiores, com histórias, etapas de análise, desenvolvimento, teste, homologação, entrega, lead time e time to market.

Ainda é uma hipótese se S4 deve entrar como parte canônica do Atlas ou como template complementar para mudanças grandes demais para S3.

### S5: resposta disciplinada

S5 aparece nas planilhas como sistema de resposta disciplinada. Ele registra melhorias internas necessárias, área responsável, status, sistema de origem, ticket, impacto e observação.

A leitura inicial é que S5 transforma incidentes, atrasos e fragilidades recorrentes em aprendizado sistêmico. Ele pode ser o mecanismo que impede a sustentação de virar apenas reação.

## Gatekeeper

Atlas depende de uma triagem técnica objetiva.

O gatekeeper é o ponto de entrada que classifica a demanda segundo critérios explícitos. Sua função é proteger os sistemas de resposta contra dois desvios: a fila única em que tudo compete com tudo e a prioridade política em que vence quem tem mais poder ou grita mais alto.

## Métricas iniciais

### DDP

Due Date Performance mede o percentual de demandas concluídas dentro do SLE esperado. No material, ela aparece como indicador central de saúde de S1 e S2.

DDP não deve ser instrumento de punição. Deve ser escuta sistêmica: cada caso fora do SLE é sinal de revisão do sistema.

### Eficiência da programação

Eficiência da programação mede a relação entre o que foi planejado para um ciclo e o que foi efetivamente entregue.

Ela revela interrupções, acréscimos fora de ciclo, problemas de capacidade, estimativas frágeis e desalinhamentos entre seleção e delivery.

## Leitura estrutural

Atlas desenha sustentação como uma arquitetura de respostas. O método não tenta fazer a equipe trabalhar mais rápido dentro de uma fila única. Ele separa naturezas de risco, cria sistemas com propósitos distintos e usa métricas como sinais de saúde do sistema.

O gestor, nesse desenho, não é controlador de tarefas. É arquiteto e curador do sistema de sustentação.
