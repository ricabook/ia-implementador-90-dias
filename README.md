# Chatbot Clínica Odontológica — Guia de uso

## O que tem aqui

- `system_prompt.md` — A "personalidade" e instruções da Bia. **Edite este arquivo** pra colocar o nome da clínica, endereço, horário.
- `chatbot.js` — Código Node.js que conecta com a API do Claude.

## Como rodar (passo a passo)

### 1. Instalar Node.js
Se ainda não tem, baixa em https://nodejs.org (versão LTS).

### 2. Pegar uma API key do Claude
Cria conta em https://console.anthropic.com → vai em "API Keys" → cria uma nova.

### 3. Configurar o projeto
Na pasta do projeto, roda no terminal:

```bash
npm init -y
npm install @anthropic-ai/sdk dotenv
```

Depois, no `package.json` que foi criado, adiciona essa linha:
```json
"type": "module"
```

### 4. Criar arquivo `.env`
Cria um arquivo chamado `.env` na pasta com isso dentro:
```
ANTHROPIC_API_KEY=cole_sua_chave_aqui
```

### 5. Editar o system prompt
Abre o `system_prompt.md` e troca:
- `[NOME DA CLÍNICA]` pelo nome real
- `[ENDEREÇO]` pelo endereço
- `[HORÁRIO]` pelo horário de atendimento

### 6. Testar no terminal
```bash
node chatbot.js
```

Vai abrir um chat no terminal. Conversa com a Bia como se fosse cliente, vê se o tom tá legal, e ajusta o system prompt se precisar.

---

## Como integrar no WhatsApp

A API do Claude **não conecta direto no WhatsApp**. Você precisa de uma camada que receba mensagens do WhatsApp e mande pra função `conversar()`. Opções:

### Opção 1: WhatsApp Business API oficial (Meta)
- Mais profissional, escalável
- Precisa de aprovação da Meta e número dedicado
- Tutoriais: https://developers.facebook.com/docs/whatsapp

### Opção 2: Plataformas SaaS (mais fácil pra começar)
Essas plataformas conectam no WhatsApp e permitem chamar APIs externas (Claude/OpenAI) via webhook:
- **Z-API** (br) — barato, fácil
- **Twilio**
- **360Dialog**
- **ManyChat** (limitado pra IA, mas tem)

### Opção 3: Biblioteca não-oficial (só pra teste, nunca produção)
- `whatsapp-web.js` (Node) — usa o WhatsApp Web, **a Meta pode banir o número**

### Fluxo geral da integração

```
Cliente manda mensagem no WhatsApp
        ↓
Plataforma (Z-API/Twilio) recebe
        ↓
Webhook chama seu servidor (essa função `conversar()`)
        ↓
Claude responde
        ↓
Seu servidor manda a resposta de volta pra plataforma
        ↓
Cliente recebe no WhatsApp
```

Você precisa **guardar o histórico de cada conversa em banco de dados** (PostgreSQL, MongoDB, Redis...) pra que a Bia "lembre" do que cada cliente já falou. A chave do banco geralmente é o número de telefone do cliente.

---

## Custos aproximados (Claude Haiku 4.5)

Pra dar uma ideia de ordem de grandeza:
- Conversa típica de atendimento (~10-15 trocas): centavos por conversa
- 1.000 conversas/mês: provavelmente abaixo de R$ 50

Verifica os preços atuais em https://www.anthropic.com/pricing — eles mudam.

Se for muito volume e quiser economizar mais, dá pra usar **prompt caching** da API (o system prompt é grande e seria cacheado) — isso reduz custo bastante. Documentação: https://docs.claude.com

---

## Próximos passos sugeridos

1. **Testa muito no terminal antes de plugar no WhatsApp.** Manda mensagens difíceis: "qto custa?", "tá caro?", "vc é robô?", "to com dor", "manda o pix". Vê se a Bia segura a onda.
2. **Ajusta o system prompt** com base nos testes — adiciona casos que aparecerem.
3. **Implementa logging** de todas as conversas (banco de dados) — vai ser ouro pra melhorar o bot depois.
4. **Define um critério claro pra "passar pra humano"** e implementa um sistema de notificação (ex: bot manda email/Slack pro time quando agendamento é fechado).
5. **Mede conversão**: % de conversas que viraram agendamento, % que viraram comparecimento, % que viraram fechamento.

---

## Dica final

A diferença entre um chatbot bom e ruim **não tá no modelo de IA, tá no system prompt e no fluxo**. Gasta tempo testando e refinando o prompt. Conversa com a Bia, anota onde ela falhou, e ajusta. Depois de 1-2 semanas de iteração, você tem um atendimento que muita clínica grande não tem.
