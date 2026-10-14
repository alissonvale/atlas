# Triagem e gatekeeper

O gatekeeper é o ponto de entrada do Atlas.

Sua responsabilidade é classificar demandas segundo o risco que elas impõem ao negócio sustentado pelo produto. Ele não existe para burocratizar o fluxo. Existe para impedir que o sistema seja governado por ruído, pressão e ordem de chegada.

## Função do gatekeeper

O gatekeeper protege três fronteiras:

- a fronteira entre emergência real e urgência;
- a fronteira entre urgência real e demanda programável;
- a fronteira entre critério objetivo e pressão política.

Quando essa função não existe, a organização tende a chamar tudo de urgente. Quando tudo é urgente, nada é realmente priorizado. O custo aparece na exaustão da equipe, na perda de previsibilidade e na incapacidade de aprender com o próprio fluxo.

## Pergunta de triagem

A pergunta de triagem do Atlas é:

> Que risco esta demanda impõe ao negócio sustentado pelo produto?

A partir dela, a demanda é encaminhada para S1, S2 ou Sistema de Adaptação e Aperfeiçoamento.

## Critérios iniciais

### Candidato a R1

Uma demanda tende a ser R1 quando:

- há perda relevante acumulando enquanto o problema persiste;
- há interrupção crítica da operação;
- há risco imediato a receita, confiança, dados, conformidade ou continuidade;
- a espera aumenta diretamente o dano;
- o negócio precisa de resposta imediata para conter a perda.

### Candidato a R2

Uma demanda tende a ser R2 quando:

- uma operação importante não consegue ser concluída;
- há uma janela curta para evitar consequência relevante;
- a demanda pode aguardar brevemente, mas deve ficar no topo da fila;
- o impacto cresce com o atraso, mas não como sangria imediata;
- o negócio precisa de resposta rápida, não de parada total.

### Candidato a R3

Uma demanda tende a ser R3 quando:

- representa adaptação, melhoria ou ajuste planejável;
- responde a mudança de negócio, legislação, mercado ou operação;
- melhora uma funcionalidade já existente;
- reduz custo, atrito ou obsolescência;
- pode ser programada sem dano relevante imediato.

## Saída da triagem

A triagem deve produzir ao menos:

- classificação de risco;
- sistema de resposta escolhido;
- justificativa breve;
- SLE aplicável, quando houver;
- responsável inicial;
- momento de revisão, se a classificação for incerta.

## Revisão de classificação

Classificação não é sentença. É leitura situada.

O Atlas deve permitir revisão quando novas informações aparecem. A disciplina está em revisar por evidência, não por pressão.

## Anti-padrões

O gatekeeper falha quando:

- classifica pela autoridade de quem pediu;
- classifica pelo volume emocional da reclamação;
- evita dizer não;
- transforma S1 e S2 em atalhos para acelerar demandas comuns;
- retém decisões por excesso de centralização;
- não registra justificativas;
- não revisa classificações equivocadas.

## Gatekeeper como função, não cargo

O gatekeeper pode ser uma pessoa, um par, uma escala ou um pequeno grupo. O importante é que a função exista e seja reconhecida.

Em contextos menores, pode ser exercida pelo responsável técnico ou pelo gestor de sustentação. Em contextos maiores, pode envolver suporte, produto, liderança técnica e negócio. O framework não exige um cargo fixo. Exige uma fronteira clara.
