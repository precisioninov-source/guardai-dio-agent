# GuardAI: Agente Inteligente para Cibersegurança e Análise de Vulnerabilidades

O **GuardAI** é uma especialização defensiva do [DIO Agent](https://github.com/digitalinnovationone/dio-agent). Ela ensina o agente a analisar vulnerabilidades junto com a pessoa: entender o contexto, confirmar o escopo, avaliar impacto e probabilidade, priorizar o risco e orientar a correção.

> Use somente código e ambientes próprios ou explicitamente autorizados. O exemplo deste projeto usa SQLite em memória, sem servidor e sem dados reais.

## O que foi acrescentado

| Arquivo | Alteração |
|---|---|
| `skills/vulnerability-analysis/SKILL.md` | Processo que o agente segue na análise |
| `skills/vulnerability-analysis/README.md` | Explicação da skill para pessoas |
| `agent/knowledge/security-basics.md` | Vocabulário, CIA, risco e boas práticas |
| `agent/persona.md` | Orientações de postura defensiva |
| `AGENTS.md` | Carrega o conhecimento e indica quando usar a skill |
| `skills/README.md` | Inclui a skill no catálogo |
| `examples/app.py` | Exemplo local vulnerável, apenas para análise |
| `examples/app_seguro.py` | Exemplo local com consulta parametrizada |

## Como usar o GuardAI

1. Baixe ou clone este repositório.
2. Instale um harness compatível seguindo a documentação oficial dele. O projeto base lista Hermes, Codex, Claude Code, Antigravity e outros.
3. Abra a pasta `guardai-dio-agent` no harness e inicie-o na raiz do repositório. Para o Hermes, use:
   ```bash
   hermes
   ```

O harness deve carregar o `AGENTS.md` ao abrir a pasta do projeto. Esse arquivo já aponta para a skill GuardAI e para a base de conhecimento de segurança.

## Demonstração local

Os exemplos usam apenas a biblioteca padrão do Python e criam um banco temporário em memória.

```bash
python examples/app.py
python examples/app_seguro.py
```

O primeiro arquivo monta a consulta juntando o valor digitado. O segundo usa parâmetros SQL para manter os valores separados da estrutura da consulta. A demonstração verifica somente um login fictício; não é um sistema de autenticação real.

## Prompt para conversar com o GuardAI

Depois de abrir o harness na pasta do fork, peça:

> Analise `examples/app.py` como um exercício local e autorizado. Explique a falha sem testar nenhum sistema externo. Avalie impacto, probabilidade, severidade e confiança; indique se o mapeamento MITRE ATT&CK se aplica neste contexto; compare com `examples/app_seguro.py` e diga como validar a correção.

Uma boa resposta deve identificar a montagem dinâmica da consulta, explicar por que dados de entrada não devem virar sintaxe SQL, distinguir o risco local de um serviço exposto e recomendar consultas parametrizadas. A técnica MITRE ATT&CK T1190 só deve ser considerada quando o cenário envolver exploração de uma aplicação exposta para acesso inicial; o identificador não é uma classificação automática de SQL injection. Consulte a [descrição oficial de T1190](https://attack.mitre.org/techniques/T1190/) e a [orientação da OWASP sobre prevenção de SQL injection](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).

## Formato da análise

O GuardAI organiza cada achado com:

1. Resumo e escopo assumido.
2. Evidência no código/configuração e nível de confiança.
3. Impacto sobre confidencialidade, integridade e disponibilidade.
4. Probabilidade, severidade e justificativa da prioridade.
5. Mapeamento MITRE ATT&CK, quando aplicável.
6. Correção recomendada e forma segura de validação.
7. Risco residual ou informação que ainda falta.

## Evidências para o portfólio

Na pasta `evidencias/`, guarde capturas de:

- análise do `examples/app.py`;
- pergunta do GuardAI sobre escopo e ambiente;
- comparação com `examples/app_seguro.py`;
- resposta com avaliação de risco e correção.

Use somente dados fictícios nos prints. Não mostre tokens, senhas, informações pessoais ou sistemas de terceiros.

## Base e autoria

Este repositório é um fork do [DIO Agent](https://github.com/digitalinnovationone/dio-agent). A especialização GuardAI e os exemplos locais foram escritos para este exercício educacional.

