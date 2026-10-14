# Atlas

Atlas é uma jornada de construção de um framework de gestão voltado para a sustentação de produtos de software.

O framework será desenvolvido primeiro como linguagem e documentação canônica, depois como práticas, templates, anexos e possíveis mecanismos operacionais.

## Estado inicial

Esta pasta foi criada como repositório local da jornada. O conteúdo canônico ainda será consolidado a partir do descritivo do framework, planilhas e demais anexos fornecidos pelo Alisson.

## Documentação

A documentação é publicada localmente com MkDocs.

```bash
uv run mkdocs serve
uv run mkdocs build
```

## Estrutura inicial

- `mkdocs.yml` — configuração do site de documentação.
- `docs/index.md` — mapa da documentação.
- `docs/project/briefing.md` — briefing vivo da jornada.
- `docs/project/roadmap/index.md` — roadmap inicial.
- `docs/method/` — documentação canônica do framework Atlas.
- `docs/adoption/` — materiais futuros de adoção e aplicação.
- `docs/operations/` — práticas, cadências, checklists e mecanismos de sustentação.
- `docs/attachments/` — índice dos anexos e materiais de contexto.
