"""
Script 1 — Classificador de mensagens de paciente Orthodontic.
Recebe mensagem, classifica em: PRECO, AGENDAMENTO, DUVIDA, RECLAMACAO, COBRANCA.
"""

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()


def classificar_mensagem(mensagem_paciente):
    system_prompt = """Você é um classificador de mensagens recebidas no WhatsApp da Orthodontic, clínica de aparelho ortodôntico popular.

Sua tarefa é classificar cada mensagem em UMA das seguintes categorias:
- PRECO: pessoa querendo saber valores, formas de pagamento, descontos
- AGENDAMENTO: pessoa querendo marcar, remarcar ou cancelar consulta
- DUVIDA: dúvida geral sobre tratamento, dor, manutenção, prazo
- RECLAMACAO: paciente insatisfeito com atendimento, dor não resolvida, demora
- COBRANCA: relacionado a pagamento, mensalidade, atraso, boleto
- OUTRO: não se encaixa nas categorias acima

Responda APENAS com o nome da categoria em maiúsculas, nada mais.
Se a mensagem for ambígua, escolha a categoria mais provável."""

    resposta = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=20,
        system=system_prompt,
        messages=[
            {"role": "user", "content": mensagem_paciente}
        ]
    )
    
    return resposta.content[0].text.strip()


# Teste com 5 mensagens reais (em linguagem de classe C/D)
mensagens_teste = [
    "kanto custa o aparelho fixo??",
    "oi bom dia, queria marca uma avaliação pra semana q vem se possivel",
    "Doutor, ta doendo muito o aparelho desde ontem, é normal??",
    "VCS NUNCA ATENDEM!!! Ja faz 3 dias q to esperando resposta!",
    "boleto da mensalidade de outubro nao chegou no meu email",
    "obg pelo atendimento foi otimo"
]

print("=" * 60)
print("CLASSIFICADOR DE MENSAGENS — ORTHODONTIC")
print("=" * 60)

for i, msg in enumerate(mensagens_teste, 1):
    categoria = classificar_mensagem(msg)
    print(f"\nMensagem {i}: {msg[:60]}...")
    print(f"   → Categoria: {categoria}")