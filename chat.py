# Importa a biblioteca base64 para codificação de imagens e a API da OpenAI para interação com o modelo de linguagem
import base64
from openai import OpenAI

# Inicializa o cliente OpenAI utilizando a chave de API.
# Nota: A chave de API deve ser armazenada de forma segura, como em variáveis de ambiente.
client = OpenAI(api_key="Insira sua chave aqui")

# Define uma função para codificar imagens no formato base64
def encode_image(image_path):
    """
    Codifica uma imagem no formato base64 para uso em mensagens JSON.

    Args:
        image_path (str): Caminho completo do arquivo de imagem no sistema.

    Returns:
        str: Representação da imagem codificada em base64.
    """
    with open(image_path, "rb") as image_file:  # Abre o arquivo de imagem em modo binário
        return base64.b64encode(image_file.read()).decode("utf-8")  # Codifica em base64 e converte para string

# Define o caminho para a imagem que será enviada
image_path = "Insira o caminho da imagem aqui."

# Codifica a imagem no formato base64
base64_image = encode_image(image_path)

# Inicia o chat interativo com o usuário
print("Bem-vindo ao chat! Digite 'sair' para encerrar.\n")

# Histórico de conversa para armazenar mensagens do usuário e respostas do assistente
conversation_history = []

# Loop principal do chat
while True:
    # Captura a entrada do usuário
    user_input = input("Você: ")
    if user_input.lower() == "sair":  # Verifica se o usuário deseja encerrar o chat
        print("Encerrando o chat. Até logo!")
        break

    # Adiciona a entrada do usuário ao histórico de conversa
    conversation_history.append({"role": "user", "content": user_input})

    # Adiciona a imagem à mensagem apenas na primeira interação
    if len(conversation_history) == 1:
        conversation_history.append({
            "role": "user",  # Define o remetente como usuário
            "content": [  # Inclui a mensagem do usuário e a imagem
                {"type": "text", "text": user_input},  # Mensagem textual
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}  # Imagem em base64
            ]
        })

    # Envia a solicitação à API da OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Modelo de linguagem utilizado
            messages=conversation_history  # Histórico de mensagens enviado como contexto
        )

        # Obtém a resposta do assistente e adiciona ao histórico
        assistant_message = response.choices[0].message.content  # Extrai o conteúdo da resposta
        conversation_history.append({"role": "assistant", "content": assistant_message})  # Armazena a resposta

        # Exibe a resposta no console
        print(f"Assistente: {assistant_message}\n")
    except Exception as e:
        # Captura e exibe erros durante a interação com a API
        print(f"Erro: {e}")
