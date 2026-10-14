# Roteiro de instalação do Mirror HygiaTech

Este roteiro registra a criação da instalação isolada do Mirror para a simulação HygiaTech.

## Decisão

A HygiaTech deve usar uma instalação própria do Mirror, não uma jornada dentro do Mirror pessoal de Alisson.

Motivo: personas, usuários, projetos e parte da identidade operacional do Mirror não são isolados por jornada. Criar atores sintéticos dentro do Mirror pessoal contaminaria o campo de identidade, memória e roteamento do próprio Alisson.

## Fronteira

```text
/Users/alissonvale/.mirror-minds/alisson-vale
  Mirror pessoal de Alisson

/Users/alissonvale/.mirror-minds/hygiatech
  Mirror sandbox da HygiaTech
```

## Estado criado

A instalação HygiaTech foi criada em:

```text
/Users/alissonvale/.mirror-minds/hygiatech
```

O banco da instalação fica em:

```text
/Users/alissonvale/.mirror-minds/hygiatech/memory.db
```

## Comandos executados

### Verificar se a instalação já existia

```bash
MIRROR_HOME=/Users/alissonvale/.mirror-minds/hygiatech
if [ -e "$MIRROR_HOME" ]; then
  echo "exists:$MIRROR_HOME"
else
  echo "missing:$MIRROR_HOME"
fi
```

Resultado: a instalação ainda não existia.

### Inicializar identidade base

O comando `memory init` atualmente cria a identidade no layout legado `~/.mirror/<user>` e não respeita `MIRROR_HOME` diretamente. Por isso a identidade foi inicializada e depois movida para o layout desejado.

```bash
cd /Users/alissonvale/mirror
MIRROR_USER= MIRROR_HOME=/Users/alissonvale/.mirror-minds/hygiatech \
  uv run python -m memory init HygiaTech
```

Resultado inicial:

```text
/Users/alissonvale/.mirror/HygiaTech
```

### Mover para o Mirror home isolado

```bash
mv /Users/alissonvale/.mirror/HygiaTech /Users/alissonvale/.mirror-minds/hygiatech
```

### Seed inicial

```bash
cd /Users/alissonvale/mirror
MIRROR_USER= MIRROR_HOME=/Users/alissonvale/.mirror-minds/hygiatech \
  uv run python -m memory seed
```

O seed criou o banco e carregou a identidade base. O comando retornou erro apenas para `ego/constraints`, porque o arquivo template está vazio. A instalação ficou operacional mesmo assim.

### Customizar identidade da HygiaTech

Foram atualizados:

```text
/Users/alissonvale/.mirror-minds/hygiatech/identity/user/identity.yaml
/Users/alissonvale/.mirror-minds/hygiatech/identity/organization/identity.yaml
```

Também foi criada a jornada operacional:

```text
/Users/alissonvale/.mirror-minds/hygiatech/identity/journeys/sustentacao.yaml
```

### Reseed com identidade customizada

```bash
cd /Users/alissonvale/mirror
MIRROR_USER= MIRROR_HOME=/Users/alissonvale/.mirror-minds/hygiatech \
  uv run python -m memory seed \
  --mirror-home /Users/alissonvale/.mirror-minds/hygiatech \
  --force
```

Resultado: identidade, organização, personas padrão e jornada `sustentacao` foram carregadas. O único erro permaneceu o arquivo vazio `ego/constraints`.

### Validar jornada operacional

```bash
cd /Users/alissonvale/mirror
MIRROR_USER= MIRROR_HOME=/Users/alissonvale/.mirror-minds/hygiatech \
  uv run python -m memory journey sustentacao
```

Resultado: jornada criada e legível, sem memórias ou conversas iniciais. A jornada foi renomeada para `sustentacao` para refletir a linguagem natural de entrada dos funcionários.

### Validar runtime

```bash
cd /Users/alissonvale/mirror
MIRROR_USER= MIRROR_HOME=/Users/alissonvale/.mirror-minds/hygiatech \
  uv run python -m memory runtime status \
  --mirror-home /Users/alissonvale/.mirror-minds/hygiatech
```

Resultado:

```text
Status: ready
Database exists: yes
Core migrations: current (12/12)
Extension health: ready (0 checked)
```

## Regra de uso

Todo comando operacional da HygiaTech deve limpar `MIRROR_USER` e definir `MIRROR_HOME` explicitamente:

```bash
MIRROR_USER= MIRROR_HOME=/Users/alissonvale/.mirror-minds/hygiatech uv run python -m memory ...
```

Isso evita que o `.env` do repositório repovoe o usuário pessoal e direcione comandos para o banco errado.

## Próximos passos

- Criar papéis operacionais específicos da HygiaTech.
- Definir clientes hospitais sintéticos.
- Criar modelo de dados da simulação.
- Converter as planilhas originais em tickets sintéticos.
- Criar cenários de S1, S2, S3 e reclassificação.
- Definir como o sistema web lerá ou espelhará os dados da simulação.
