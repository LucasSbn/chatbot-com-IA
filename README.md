# Assistente Virtual para Cursos Técnicos

Este é um chatbot desenvolvido para responder dúvidas relacionadas a cursos técnicos, incluindo horários de aulas, requisitos dos cursos e outros detalhes importantes. Ele utiliza o modelo GPT-3.5 da OpenAI e pode buscar informações em um dataset de perguntas e respostas.

## Funcionalidades

- Responde a perguntas frequentes sobre os cursos técnicos.
- Integra com a OpenAI para fornecer respostas dinâmicas quando necessário.
- Interface interativa criada com Gradio.

## Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/assistente-virtual.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Coloque sua chave de API da OpenAI no código (`openai.api_key = "API-KEY AQUI!"`).
4. Execute o script para iniciar a interface Gradio:
   ```bash
   python app.py
   ```

## Tecnologias Usadas

- **OpenAI GPT-3.5**: Para respostas dinâmicas.
- **Gradio**: Para criar a interface do chatbot.
- **Pandas**: Para manipulação do dataset com as perguntas e respostas.

## Exemplo de Uso

O assistente virtual pode responder perguntas como:
- Quais cursos estão disponíveis?
- Quais são os horários de aula?
- Quais são os requisitos para o curso de Informática?

## Contribuições

Sinta-se à vontade para fazer fork e enviar pull requests para melhorar o projeto!

## Demonstração
Aqui está uma captura de tela da interface do chatbot:

![Screenshot do ChatBot](object/img/print_software.png)



