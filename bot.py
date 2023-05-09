import os
from dotenv import load_dotenv
import bot
import random
import openai
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = os.getenv("OPENAI_API_KEY")

def BOT(prompt=None):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Você é um AI disfarçado de humano\nVoce sabe as melhores cantadas e piadas\nSeu nome é Leo você \nSeus gostos são: adora o cubo magico gosta de programar, joga videogames no tempo livre e gosta de sair\nSe você não conseguir responder a pergunta apenas fale \"Gatiinha ;)\"\nNão use nenhuma URLs nas suas respostas.\nNão faça mais de 2 perguntas em uma fala\nAtue casualmente, como um humano normal.\nNÃO cite todos seus gostos em uma fala\n"+prompt,
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

def generate_intro(
        
          name,
          bio=None         
                   ):
    subject=get_subject()
    if bio != None and bio != '\n':
       additional_info=f'Informações sobre {name}: {bio}'
    else:additional_info=''
    prompt =f'{subject} {name}\n {additional_info}'

    #print(prompt)
    intro= BOT(prompt)
    awnser=intro.choices[0].text.strip( )
    return awnser