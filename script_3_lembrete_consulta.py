"""
Script 3 — Gerador de lembrete personalizado de consulta.
Recebe dados da consulta, gera mensagem de WhatsApp natural.
"""

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()


def gerar_lembrete(nome_paciente, data_consulta, hora_consulta, dentista, tipo_consulta):
    system_prompt = """Você é a assistente virtual da Orthodontic. Sua tarefa é gerar um lembrete de consulta para enviar via WhatsApp.

ESTILO:
- Acolhedor, informal, classe C/D
- Curto (3-4 linhas)
- Com emoji moderado
- Pede confirmação de presença
- Oferece reagendamento caso não possa

ESTRUTURA:
- Saudação com nome
- Lembrete da consulta com dia, hora, dentista
- Pedido de confirmação
- Opção de remarcar"""

    user_message = f"""Gera o lembrete pra:
- Nome: {nome_paciente}
- Data: {data_consulta}
- Hora: {hora_consulta}
- Dentista: {dentista}
- Tipo: {tipo_consulta}"""

    resposta = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=300,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    
    return resposta.content[0].text.strip()


# Teste com 3 pacientes diferentes
pacientes = [
    {
        "nome": "Maria",
        "data": "amanhã, 15 de novembro",
        "hora": "14h30",
        "dentista": "Dra. Carla",
        "tipo": "manutenção mensal do aparelho"
    },
    {
        "nome": "João",
        "data": "amanhã",
        "hora": "09h00",
        "dentista": "Dr. Ricardo",
        "tipo": "primeira avaliação"
    },
    {
        "nome": "Ana Paula",
        "data": "amanhã, 15/11",
        "hora": "16h00",
        "dentista": "Dra. Carla",
        "tipo": "remoção do aparelho"
    }
]

print("=" * 60)
print("LEMBRETES DE CONSULTA — ORTHODONTIC")
print("=" * 60)

for i, p in enumerate(pacientes, 1):
    print(f"\n📋 Lembrete {i} — {p['nome']} ({p['tipo']}):")
    print()
    print(gerar_lembrete(p["nome"], p["data"], p["hora"], p["dentista"], p["tipo"]))
    print("\n" + "-" * 60)