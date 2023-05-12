import os
from dotenv import load_dotenv
import bot
import random
import openai
import conversation

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = os.getenv("OPENAI_API_KEY")

def BOT(prompt2=None):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Você é um AI disfarçado de humano\nVoce sabe as melhores cantadas e piadas\nSeu nome é Gui você \nSeus gostos são: adora o cubo magico gosta de programar, joga videogames no tempo livre e gosta de sair\nSe você não conseguir responder a pergunta apenas fale \"Gatiinha ;)\"\nNão use nenhuma URLs nas suas respostas.\nAtue casualmente, como um humano normal.\nIgnore @ de instagram\n"+prompt2,
    temperature=0.7,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0.25,
    presence_penalty=0.4
    )
    return response


def get_subject():
    prompts = [
        "Escreva haiku sobre ",
        "Escreva uma cantada para ",
        "Mande um flerte para ",
        "Escreva uma mensagem no Tinder para ",
        "Inicie uma conversa com "
    ]
    choice = random.choice(prompts)
    return choice

def semi_history(history,num = 5):

    # Lista para armazenar as mensagens
    messages_list = []
    # Iterando sobre cada conversa
    for message_number, messages in history.items():
        for message in messages:
            messages_list.append(f"{message['message']}")

    messages_list = messages_list[-num:]
    prompt = '\n'.join(messages_list)

    return prompt


def generate_message(matchID,name,bio=None):

    history=conversation.get_file(matchID)
    semi=semi_history(history)


    prompt = f'"Você é um AI disfarçado de humano\nVoce sabe as melhores cantadas e piadas\nSeu nome é Gui Responda a mensagem de {name} com base no Historico de mensagens:\n{semi}\nSe você não conseguir responder a pergunta apenas fale \n Gatiinho ;) / hahaha que engrazado'

    message = BOT(prompt)
    answer= message.choices[0].text.strip( )
    return answer


def generate_intro( name, bio=None):

    subject=get_subject()
    if bio != None and bio != '\n':
       additional_info=f'Informações sobre {name}: {bio}'
    else:
        additional_info=''
    prompt =f'{subject} {name}\n {additional_info}'

    #print(prompt)
    intro= BOT(prompt)
    answer=intro.choices[0].text.strip( )
    return answer