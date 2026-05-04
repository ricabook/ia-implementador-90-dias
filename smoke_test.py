"""
Smoke test — confirma que ambiente está funcionando.
Roda isso uma vez. Se imprimir as 3 mensagens, está tudo certo.
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Verifica se a chave foi carregada
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    print("❌ ERRO: ANTHROPIC_API_KEY não foi carregada do .env")
    print("Verifica se o arquivo .env está na raiz do projeto e tem a linha:")
    print("ANTHROPIC_API_KEY=sk-ant-...")
    exit()

print("✅ Chave da API carregada com sucesso")

# Faz uma chamada de teste
client = Anthropic()

resposta = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=200,
    messages=[
        {
            "role": "user",
            "content": "Em uma frase curta, me dê uma boa-vinda pra alguém que está começando a estudar IA aplicada a empresas."
        }
    ]
)

print("✅ Conexão com Claude funcionou")
print()
print("Resposta da IA:")
print(resposta.content[0].text)
print()
print(f"Tokens usados: {resposta.usage.input_tokens} entrada + {resposta.usage.output_tokens} saída")