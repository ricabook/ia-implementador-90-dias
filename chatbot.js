// chatbot.js — Chatbot da clínica odontológica usando API do Claude
// Instale antes: npm install @anthropic-ai/sdk dotenv

import Anthropic from "@anthropic-ai/sdk";
import fs from "fs";
import "dotenv/config";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

// Carrega o system prompt do arquivo
const SYSTEM_PROMPT = fs.readFileSync("./system_prompt.md", "utf-8");

/**
 * Envia uma mensagem pro chatbot e recebe a resposta.
 *
 * @param {Array} historico - Array de mensagens anteriores no formato [{role, content}]
 * @param {string} mensagemUsuario - A nova mensagem do cliente
 * @returns {Promise<{resposta: string, historicoAtualizado: Array}>}
 */
export async function conversar(historico, mensagemUsuario) {
  const novoHistorico = [
    ...historico,
    { role: "user", content: mensagemUsuario },
  ];

  const response = await client.messages.create({
    model: "claude-haiku-4-5-20251001", // Haiku 4.5 — rápido e barato, ideal pra atendimento
    max_tokens: 500, // Respostas curtas, estilo WhatsApp
    system: SYSTEM_PROMPT,
    messages: novoHistorico,
  });

  const resposta = response.content[0].text;

  return {
    resposta,
    historicoAtualizado: [
      ...novoHistorico,
      { role: "assistant", content: resposta },
    ],
  };
}

// ============================================================
// EXEMPLO DE USO — simula uma conversa pelo terminal
// ============================================================

import readline from "readline";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let historicoConversa = [];

console.log("\n🦷 Chatbot da Clínica iniciado! Digite 'sair' pra encerrar.\n");

function pergunta() {
  rl.question("Você: ", async (msg) => {
    if (msg.toLowerCase() === "sair") {
      rl.close();
      return;
    }

    try {
      const { resposta, historicoAtualizado } = await conversar(
        historicoConversa,
        msg
      );
      historicoConversa = historicoAtualizado;
      console.log(`\nBia: ${resposta}\n`);
    } catch (err) {
      console.error("Erro:", err.message);
    }

    pergunta();
  });
}

pergunta();
