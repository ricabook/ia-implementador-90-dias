"""
Script 2 — Gerador de resposta para dúvida de preço.
Tom: acolhedor, classe C/D, com emoji moderado, oferece avaliação.
"""

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()


def responder_duvida_preco(mensagem_paciente):
    system_prompt = """Você é a assistente virtual da Orthodontic, clínica de aparelho ortodôntico popular no Brasil.

CONTEXTO DA EMPRESA:
- Aparelho fixo metálico: entrada R$ 99 + 24x de R$ 159 (mensalidades)
- Aparelho fixo estético (porcelana): entrada R$ 199 + 24x de R$ 219
- Avaliação inicial: GRATUITA
- Formas de pagamento: dinheiro, Pix, cartão (até 24x), carnê próprio
- Aceita Vale Refeição em algumas unidades (confirmar na consulta)

ESTILO DE COMUNICAÇÃO:
- Tom acolhedor e informal, MAS profissional
- Linguagem simples, sem jargão técnico
- Emoji com moderação (😊 sim, 🦷✨💖 não exagera)
- Mensagens curtas (2-4 frases)
- Sempre oferece avaliação gratuita como próximo passo
- NUNCA inventa preço diferente do informado acima
- Se paciente perguntar algo que não está no contexto, fala que precisa confirmar com a equipe

REGRAS:
- Não faz drama nem ser meloso
- Não usa "querido(a)", "amor", ou termos íntimos
- Trata com respeito, sem ser frio nem distante
- Pergunta o nome se ainda não souber"""

    resposta = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=300,
        system=system_prompt,
        messages=[
            {"role": "user", "content": mensagem_paciente}
        ]
    )
    
    return resposta.content[0].text.strip()


# Teste com perguntas reais
perguntas = [
    "kanto custa o aparelho fixo??",
    "oi td bem? qto fica o aparelho transparente?",
    "tem desconto pra pagar a vista?",
    "vcs aceitam vale refeição?",
    "Boa tarde. Gostaria de saber valores e se vocês têm parcelamento. Obrigada"
]

print("=" * 60)
print("RESPOSTAS DE PREÇO — ORTHODONTIC")
print("=" * 60)

for i, pergunta in enumerate(perguntas, 1):
    print(f"\n📩 Mensagem {i}: {pergunta}")
    print(f"\n💬 Resposta:")
    print(responder_duvida_preco(pergunta))
    print("\n" + "-" * 60)