# Importa a biblioteca base64 para codificação de imagens e a API da OpenAI para interação com o modelo de linguagem
import base64
from openai import OpenAI

# Cria uma instância do cliente OpenAI utilizando a chave de API.
# Nota: Para segurança, a chave de API deve ser armazenada em variáveis de ambiente ou serviços de gerenciamento de segredos.
client = OpenAI(api_key="Insira sua chave aqui.")


# Define uma função para codificar uma imagem no formato base64
# O formato base64 é usado para embutir dados binários, como imagens, em mensagens JSON.
def encode_image(image_path):
    """
    Codifica uma imagem no formato base64 a partir de um caminho fornecido.

    Args:
        image_path (str): Caminho do arquivo de imagem no sistema.

    Returns:
        str: Representação da imagem codificada em base64.
    """
    with open(image_path, "rb") as image_file:  # Abre o arquivo de imagem no modo binário
        return base64.b64encode(image_file.read()).decode("utf-8")  # Codifica a imagem e converte para string


# Caminho para a imagem que será codificada
# Certifique-se de que o caminho seja acessível e o arquivo esteja no formato correto.
image_path = "Insira o caminho da imagem aqui."

# Codifica a imagem no formato base64 para uso na requisição da API
base64_image = encode_image(image_path)

# Faz uma solicitação à API da OpenAI para gerar uma resposta baseada na entrada fornecida
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Modelo de linguagem utilizado para processar a solicitação
    messages=[
        {
            "role": "user",  # Define que a mensagem foi enviada pelo usuário
            "content": [  # O conteúdo da mensagem é uma lista com texto e imagem
                {
                    "type": "text",  # Tipo de conteúdo: texto
                    "text": ("qual a cor dos olhos do cat?"),  # Pergunta feita ao modelo
                },
                {
                    "type": "image_url",  # Tipo de conteúdo: URL da imagem
                    "image_url": {  # A imagem é passada como uma string base64 embutida
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
)

# Exibe a primeira opção de resposta gerada pelo modelo no console.
print(response.choices[0])
