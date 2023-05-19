import sys
sys.path.append('./tinder_api')
from tinder_api_sms import *

import os
from dotenv import load_dotenv
import random
import openai
import update


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = os.getenv("OPENAI_API_KEY")

def BOT(prompt2):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Guilherme é um homem solteiro 21 anos que mora em São Paulo, mais especificamente em Liberdade. Ele é um estudante de engenharia de software e recentemente comprou algumas plantas, mas não sabe muito bem como cuidar delas. Um dos seus maiores sonhos é resolver o cubo de Rubik que está em sua mesa. Ele adora séries e videogames FPS.\nGuilherme tem muito senso de humor. Ele é muito curioso e sempre faz muitas perguntas.\nEle é gentil e sempre quer saber mais sobre as outras pessoas.\n"+prompt2, 
    temperature=0.7,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0.25,
    presence_penalty=0.4
    )
    return response


def semi_hist(history,num = 10):

    history=history[2:]
    messages_list = history[-num:]
    print('---------BOT INFO--------')
    message = '\n'.join(map(str, messages_list))
    print(messages_list)
    return message

def generate_message(matchID,personName,selfId,updates,bio=None,num=10):

    history=update.get_history(updates,matchID,selfId)
    
    semi_history=semi_hist(history,num)

    prompt_extra=f'Ele está usando um aplicativo de namoro e está conversando com uma garota chamada {personName}.\n\n{semi_history} responde de forma informal com muito humor e curiosidade, ele pode até fazer uma pergunta também de forma informal:'
    print('---------BOT PROMPT--------')
    print(prompt_extra)

    message = BOT(prompt_extra)
    answer= message.choices[0].text.strip( )
    return answer

def get_subject():
    prompts = [
        "Escreva haiku sobre ",
        "Escreva uma cantada para ",
        "Mande um flerte para ",
        "Escreva uma mensagem no Tinder para ",
        "Inicie uma conversa com ",
        "Pergunte de musica para "
    ]
    choice = random.choice(prompts)
    return choice

def generate_intro( personName, bio=None):

    subject=get_subject()
    if bio != None and bio != '\n':
       additional_info=f'Ele está usando um aplicativo de namoro e está conversando com uma garota chamada {personName}.\n {personName} gosta de {bio}'
    else:
        additional_info=f'Ele está usando um aplicativo de namoro e está conversando com uma garota chamada {personName}.'
    prompt =f'{additional_info} \n{subject} {personName}\n'
    #print(prompt)
    intro= BOT(prompt)
    answer=str(intro.choices[0].text.strip( ))

    return answer