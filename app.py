import openai
import pandas as pd
import gradio as gr

openai.api_key = "API-KEY AQUI!"

dataset_path = "objects/spreadsheet/FAQ_Cursos_Extenso.xlsx"

try:
    faq_data = pd.read_excel(dataset_path)
except FileNotFoundError:
    print("Erro: O arquivo do dataset não foi encontrado no caminho especificado.")
    exit()

faq_context = "\n".join([f"Pergunta: {row['pergunta']}\nResposta: {row['resposta']}" for _, row in faq_data.iterrows()])

def find_answer_in_faq(user_question):
    for question, answer in zip(faq_data['pergunta'], faq_data['resposta']):
        if user_question.lower() in question.lower():
            return answer
    return None

def chatbot(user_input):
    if user_input.lower() == 'sair':
        return "Obrigado por conversar! Até logo!"

    faq_answer = find_answer_in_faq(user_input)
    if faq_answer:
        return faq_answer
    else:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"Você é um assistente especializado em cursos técnicos. Aqui estão informações importantes:\n{faq_context}"},
                    {"role": "user", "content": user_input}
                ]
            )
            chatbot_response = response['choices'][0]['message']['content']
            return chatbot_response
        except openai.error.OpenAIError as e:
            return f"Ocorreu um erro ao processar sua solicitação. Detalhes: {e}"
        except Exception as e:
            return f"Um erro inesperado ocorreu. Detalhes: {e}"

interface = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(label="Pergunte ao ChatBot:"),
    outputs=gr.Textbox(label="Resposta do ChatBot:"),
    title="ChatBot dos Cursos Técnicos",
    description="Pergunte sobre os cursos técnicos disponíveis. Digite 'sair' para encerrar."
)

interface.launch(share=True)
