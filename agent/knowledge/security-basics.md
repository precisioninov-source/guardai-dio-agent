# Fundamentos de segurança defensiva

Este arquivo dá ao DIO Agent vocabulário consistente para explicar vulnerabilidades e recomendar correções. A análise deve separar o que foi observado do que ainda é hipótese.

## Conceitos

- **Ativo:** dado, serviço, aplicação ou recurso que precisa de proteção.
- **Ameaça:** situação ou agente capaz de causar dano a um ativo.
- **Vulnerabilidade:** fraqueza que pode ser explorada ou provocar falha.
- **Exposição:** condição que torna um ativo alcançável; por exemplo, uma aplicação publicada na internet.
- **Risco:** combinação contextual entre probabilidade de exploração e impacto possível.
- **Severidade:** gravidade técnica potencial do achado. Ela não é sempre igual ao risco real, que depende da exposição, dos controles e do valor do ativo.
- **Confiança:** quanto as evidências sustentam o achado. Não aumente a confiança sem confirmação.

## Tríade CIA

- **Confidencialidade:** impede que pessoas não autorizadas vejam informações.
- **Integridade:** protege dados e sistemas contra alterações indevidas.
- **Disponibilidade:** mantém os serviços e dados acessíveis quando necessários.

Ao avaliar impacto, indique qual dimensão pode ser afetada e explique a consequência concreta. Não marque as três dimensões por padrão.

## Priorização de risco

Use uma escala qualitativa consistente:

| Probabilidade | Referência |
|---|---|
| Baixa | Há barreiras relevantes ou o cenário de exploração não foi demonstrado |
| Média | A falha é alcançável em certas condições, mas depende de fatores adicionais |
| Alta | A entrada controlada pelo atacante alcança o ponto vulnerável com poucas barreiras |

| Impacto | Referência |
|---|---|
| Baixo | Efeito limitado, sem dados ou funções relevantes |
| Moderado | Afeta parte dos dados ou de uma função com recuperação simples |
| Alto | Pode expor ou alterar dados importantes, ou interromper função relevante |
| Crítico | Pode comprometer ativos essenciais ou causar dano amplo |

A prioridade deve explicar como probabilidade e impacto se combinam no ambiente informado. Se faltarem dados sobre exposição, privilégios, controles ou tipo de informação, declare a lacuna e peça contexto. Não apresente uma pontuação numérica como se fosse universal.

## Exemplo: SQL injection

SQL injection ocorre quando uma entrada não confiável é incorporada à sintaxe de uma consulta SQL. Analise o caminho entre a origem da entrada e a execução da consulta. Prefira consultas parametrizadas, em que o código SQL e os valores são enviados separadamente.

Para este tipo de achado:

- destaque a linha e a origem do dado;
- explique em termos simples como a consulta pode interpretar entrada como estrutura;
- estime o que a conta de banco de dados poderia ler ou alterar, considerando seus privilégios;
- recomende consultas parametrizadas e privilégio mínimo;
- não dependa de listas negras de caracteres como defesa principal;
- diferencie o exemplo local em memória de uma aplicação realmente exposta.

A [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) descreve consultas parametrizadas como defesa primária.

## CWE e MITRE ATT&CK

- **CWE** classifica tipos de fraqueza no software. Use uma categoria somente quando as evidências sustentarem.
- **MITRE ATT&CK** organiza táticas e técnicas observadas no comportamento adversário. Não é um catálogo de falhas de código.

A técnica [T1190 — Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) pode ser relevante se o cenário indicar exploração de uma aplicação exposta para obter acesso inicial. Uma SQL injection em código local não implica, por si só, T1190. Explique a condição ou diga que o mapeamento não se aplica com as informações atuais.

## Boas práticas defensivas

- Confirme autorização e escopo antes de qualquer teste contra um ambiente.
- Prefira revisão estática e exemplos locais; não faça varredura ou exploração externa sem escopo explícito.
- Valide entradas conforme o formato esperado, mas não use validação como substituto de consultas parametrizadas.
- Aplique privilégio mínimo a contas de aplicação.
- Proteja segredos fora do código-fonte e do histórico do Git.
- Registre erros sem expor consultas, senhas, tokens ou dados pessoais.
- Corrija a causa raiz, não apenas o sintoma.
- Indique como validar a correção em laboratório e declare o que não foi verificado.

## Referências

- [MITRE ATT&CK — T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP — SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

