# Proposta inicial de design de fluxo operacional

Este documento registra a primeira visão de fluxo do usuário depois que ele entra na jornada `sustentacao` no Mirror HygiaTech.

A proposta ainda não define a implementação das surfaces no Maestro. Ela organiza o comportamento esperado da experiência para orientar o desenho posterior.

## Entrada

O funcionário não deveria precisar pensar em termos de framework ou jornada técnica. A entrada natural é:

```text
vamos trabalhar na sustentação
```

Por baixo, o Mirror ativa a jornada:

```text
sustentacao
```

A primeira superfície é a `Operational Entry`, alimentada pelos dados de escala e situação operacional atual.

Ela responde:

- quem é a pessoa no turno;
- onde ela está alocada;
- quais sistemas de resposta ela deve observar;
- qual é a situação geral da sustentação;
- quais tickets estão no seu foco;
- qual atenção imediata é sugerida.

## Fluxo geral

```text
Operational Entry
        │
        ├─ Entrada nova
        │     ▼
        │   Risk Intake
        │     ├─ Support Resolved
        │     ├─ Evidence Request
        │     └─ Triage Handoff
        │             ▼
        │           Triage Gate
        │
        ├─ Decisão de risco
        │     ▼
        │   Triage Gate
        │     ├─ S1 -> Response Flow ↯
        │     ├─ S2 -> Response Flow ⇢
        │     ├─ S3 -> S3 Candidate Gate
        │     └─ Evidence Gap
        │
        ├─ Execução S1/S2
        │     ▼
        │   Response Flow
        │     ├─ Customer Update
        │     ├─ Risk Treated
        │     └─ Learning Review / S3 Candidate
        │
        ├─ Programação S3
        │     ▼
        │   Programmed Cycle
        │     ├─ S3 Candidate Gate
        │     ├─ Capacity Posture
        │     └─ Cycle Commitment
        │
        └─ Revisão do sistema
              ▼
            SLE Pulse / Learning Review
              ├─ Policy Adjustment
              ├─ Capacity Decision
              └─ Monthly Review
```

## Fluxo por papel

### Help desk

O help desk sai da `Operational Entry` para `Risk Intake`.

```text
Operational Entry
        │
        ├─ nova demanda chegou
        │     ▼
        │   Risk Intake
        │     ├─ suporte resolve
        │     ├─ pedir evidência
        │     └─ Triage Handoff
        │
        └─ demanda aguardando evidência
              ▼
            Risk Intake atualizado
              ├─ evidência suficiente
              └─ acionar gatekeeper
```

O help desk não decide a classificação final S1/S2/S3. Ele qualifica a entrada, registra urgência percebida sem aceitá-la automaticamente como risco real e prepara handoff para o gatekeeper quando houver risco operacional.

### Gatekeeper

O gatekeeper sai da `Operational Entry` para `Triage Gate` ou `Reclassification`.

```text
Operational Entry
        │
        ├─ demanda precisa de classificação
        │     ▼
        │   Triage Gate
        │     ├─ S1
        │     ├─ S2
        │     ├─ S3
        │     └─ voltar para evidência
        │
        └─ risco mudou
              ▼
            Reclassification
              ├─ S3 -> S2
              ├─ S2 -> S1
              ├─ S1 -> S2/S3
              └─ manter classificação
```

O gatekeeper protege a fronteira entre risco operacional e pressão política ou comercial.

### Dev Delphi / Dev C#

O dev sai da `Operational Entry` para `Response Flow`.

```text
Operational Entry
        │
        ├─ assumir ticket S1/S2
        │     ▼
        │   Response Flow
        │     ├─ hipótese técnica
        │     ├─ evidências analisadas
        │     ├─ ação proposta
        │     ├─ risco da correção
        │     └─ próxima comunicação
        │
        └─ correção concluída
              ▼
            Risk Treated
              ├─ cliente valida
              ├─ contorno documentado
              └─ aprendizado ou S3 candidato
```

No Atlas, o dev não entra em uma unidade de delivery. Ele entra em correção, contenção, entrega ou aprendizado operacional.

### Coordenação de sustentação

A coordenação sai da `Operational Entry` para `Current Board`, `SLE Pulse`, `Learning Review` ou `Capacity Posture`.

```text
Operational Entry
        │
        ├─ ver situação geral
        │     ▼
        │   Current Board
        │
        ├─ revisar risco de atraso
        │     ▼
        │   SLE Pulse
        │
        ├─ rever semana/ciclo
        │     ▼
        │   Learning Review
        │
        └─ decidir capacidade
              ▼
            Capacity Posture
```

A coordenação observa o sistema inteiro: SLE, gargalos, qualidade de triagem, capacidade Delphi e recorrências que precisam virar adaptação.

### Produto

Produto sai da `Operational Entry` para `Programmed Cycle` e `S3 Candidate Gate`.

```text
Operational Entry
        │
        ├─ ver candidatos S3
        │     ▼
        │   Programmed Cycle
        │
        ├─ comparar valor e recorrência
        │     ▼
        │   S3 Candidate Gate
        │
        ├─ rejeitar pressão comercial
        │     ▼
        │   Boundary Note
        │
        └─ fechar programação
              ▼
            Cycle Commitment
```

Produto protege o Sistema de Adaptação e Aperfeiçoamento contra duas distorções: virar fila genérica de pedidos ou ser invadido por urgências falsas.

## Surfaces existentes ou já propostas

- `Operational Entry`
- `Risk Intake`
- `Triage Gate`
- `Response Flow`
- `SLE Pulse`
- `Programmed Cycle`
- `Reclassification`
- `Learning Review`

## Surfaces candidatas

Estas surfaces apareceram como lacunas naturais do fluxo:

- `Evidence Request`, quando falta dado mínimo para triagem;
- `Triage Handoff`, ponte entre help desk e gatekeeper;
- `Risk Treated`, quando contenção ou correção reduz o risco;
- `Customer Update`, comunicação proporcional a S1/S2/S3;
- `S3 Candidate Gate`, decisão sobre entrada no ciclo S3;
- `Capacity Posture`, visibilidade de capacidade Delphi/C#/help desk;
- `Cycle Commitment`, fechamento da programação S3;
- `Monthly Review`, consolidação mensal.

Para manter o primeiro recorte enxuto, as surfaces candidatas mais importantes são:

```text
Triage Handoff
Evidence Request
S3 Candidate Gate
Capacity Posture
```

## Foco inicial

O próximo passo de design deve focar apenas no primeiro perfil padrão da simulação:

```text
Renata Pires, HD-003
```

Ela está alocada na semana atual como:

```text
role_today: help_desk_intake
allocation: pronto_atendimento
response_systems: S1, S2
focus_ticket: TCK-2026-CW-003
```

O primeiro fluxo a detalhar será:

```text
Operational Entry -> Risk Intake / Evidence Request -> Triage Handoff
```
