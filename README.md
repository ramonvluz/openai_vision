# OpenAI Vision

**OpenAI Vision** é um projeto que integra visão computacional e a API da OpenAI para permitir interações avançadas baseadas em mensagens e imagens. O sistema é projetado para processar imagens e gerar respostas inteligentes utilizando modelos de linguagem, suportando tanto URLs de imagens quanto imagens codificadas em Base64.

## Funcionalidades Principais

- **Conversas Interativas**: Interaja com o sistema por meio de mensagens e imagens, permitindo perguntas baseadas em contexto visual.
  
- **Processamento de Imagens Base64**: Suporte para codificação de imagens em Base64 e envio como parte das mensagens.

- **Envio de URLs de Imagens**: Permite enviar imagens utilizando URLs para análises e respostas baseadas em conteúdo visual.

- **Histórico de Conversas**: Armazena o histórico das interações para manter o contexto durante as conversas.

- **Integração com OpenAI**: Utiliza o modelo OpenAI GPT para gerar respostas baseadas em texto e imagens.

## Estrutura do Projeto

- **`chat.py`**: Script principal que gerencia interações com o modelo OpenAI, permitindo perguntas e respostas baseadas em mensagens e imagens.
  
- **`quickstart_url.py`**: Exemplo de envio de imagens por URLs para interação com o modelo OpenAI.
  
- **`uploading_base64_encoded_images.py`**: Script para codificação de imagens em Base64 e envio ao modelo como parte de mensagens.

- **`input_dir/`**: Diretório de entrada para imagens, com subdiretórios organizados por categorias, como `cat/`.

## Instalação

### Pré-requisitos

- Python 3.10 ou superior
- Conta na OpenAI (para chave da API)

### Passos para Instalação

1. Clone este repositório para sua máquina local:

```bash
git clone https://github.com/ramonvluz/openai_vision.git
```

2. Crie e ative um ambiente virtual:

```bash
cd openai_vision
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows
```

3. Instale a biblioteca da OpenAi:

```bash
pip install openai
```

4. Configure sua chave de API da OpenAI diretamente nos scripts.

5. Execute o projeto:

- Para o chat principal:
  ```bash
  python chat.py
  ```
- Para o envio de URLs de imagens:
  ```bash
  python quickstart_url.py
  ```
- Para o envio de imagens em Base64:
  ```bash
  python uploading_base64_encoded_images.py
  ```

## Como Usar

1. Coloque as imagens que deseja usar no diretório `input_dir/` ou forneça uma URL para o script `quickstart_url.py`.
2. Use o script apropriado para iniciar a interação:
   - **Chat com mensagens e imagens**: `chat.py`.
   - **Análise de URLs**: `quickstart_url.py`.
   - **Codificação e envio de imagens Base64**: `uploading_base64_encoded_images.py`.
