# Importa a biblioteca OpenAI para interação com a API
from openai import OpenAI

# Cria uma instância do cliente OpenAI, utilizando a chave de API fornecida.
# Nota: Recomenda-se armazenar a chave de API em variáveis de ambiente ou gerenciadores de segredo para evitar exposição.
client = OpenAI(api_key="Insira sua chave aqui.")

# Cria uma solicitação de completions do modelo GPT, incluindo uma mensagem do usuário.
# A mensagem contém duas partes: um texto introdutório e uma URL de uma imagem.
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Especifica o modelo de linguagem a ser utilizado
    messages=[
        {
            "role": "user",  # Define o papel do remetente da mensagem (usuário)
            "content": [  # O conteúdo da mensagem é uma lista que mistura texto e imagem
                {"type": "text", "text": "What's in this image?"},  # Mensagem em texto
                {
                    "type": "image_url",  # Indica que o próximo item é uma URL de imagem
                    "image_url": {
                        "url": "Insira a URL da imagem aqui.",  # URL da imagem a ser analisada
                    },
                },
            ],
        }
    ],
    max_tokens=300,  # Limita o número máximo de tokens na resposta do modelo
)

# Exibe a primeira opção de resposta gerada pelo modelo no console.
# O `choices` contém todas as respostas geradas pelo modelo, e geralmente a primeira opção é suficiente.
print(response.choices[0])
