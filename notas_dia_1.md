1) O que é um token? Por que importa pra custo?
Token = unidade básica de texto (pedaços de palavras, pontuação, etc.).
Modelos cobram por tokens processados (entrada + saída).
👉 Mais tokens = mais custo + mais latência.
2) O que é context window? Qual a janela atual?
Context window = limite de tokens que o modelo consegue considerar de uma vez.

Atualmente:

OpenAI (GPT): ~128k tokens (até ~1M em casos específicos)
Anthropic (Claude): ~200k tokens (até ~1M)
3) Diferença entre system prompt e user prompt?
System prompt: define regras, comportamento, tom (nível “invisível” e prioritário).
User prompt: pedido direto do usuário.
👉 System tem mais peso na hierarquia.
4) O que é temperatura? Quando usar?
Controla aleatoriedade/criatividade.
Valor	Uso
0	Determinístico (código, cálculos, respostas exatas)
0.7	Equilíbrio (uso geral)
1.0	Criativo (copy, ideias, brainstorming)
5) O que é alucinação? Como diminuir?
Alucinação = modelo inventa informação incorreta com confiança.

Como reduzir:

Prompt específico e bem estruturado
Pedir fontes ou justificativa
Usar RAG (dados externos)
Reduzir temperatura
Limitar escopo da resposta