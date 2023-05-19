import sys
sys.path.append('./tinder_api')
from tinder_api_sms import *

import datetime
from datetime import datetime
import bot
import re
import os
import time as t
import conversation
import caracteres



print('INICIANDO....')
#todo ------------------------------------
with open('time.txt', 'r') as f:
    time=f.read()
me=get_self()
selfId = me["_id"];
#todo try/wile------------------------------
now = datetime.utcnow()  # get current UTC time
formatted_time = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')  # format the time string
print(formatted_time)
time = formatted_time

time = '2023-05-12T03:15:46.645789Z'
update=get_updates(time)

#* novas mensagens e salva
news=get_updates(time)

recs=get_recommendations()

print(me['bio'])

quazmo = '62401030088f0a0100eaf05c'
guerra = '5b3c66c9226c1e3e29dfa189'
matchID="5b3c66c9226c1e3e29dfa18962401030088f0a0100eaf05c" #! s2 lindão


count = "80";
match_dict = all_matches(count);

matches=match_dict['data']['matches']

#todo: Responde novas mensagens
for user in matches:

    userId = user['_id'];
    if user['messages']:

        lastMessage = user['messages'][-1];
        
        if lastMessage['from'] != selfId: #? Fui eu que enviei a ultima mensagem?
        
            matchID=user['messages'][-1]['match_id']
            personId=user['messages'][0]['from']

            person_name=user['person']['name']
            try:
                bio = user['person']['bio'] #todo: pega bio do match
            except KeyError:
                bio = None
            response = bot.generate_message(matchID=matchID,personName=person_name,selfId=selfId,bio=bio,num=10,updates=update)
        else:
            continue
    else: #? matches sem mensagens
        print(user['person']['name'])
        personId=user['participants'][0]
        matchID=user['_id']
        person_name=user['person']['name']

        try:
            bio = user['person']['bio'] #todo: pega bio do match
        except KeyError:
            bio = None

        response = bot.generate_intro(personName=person_name,bio=bio)

    response = re.sub(r'\b[Bb][Oo][Tt]\b', 'Gui', response)
    if response.startswith("Gui"):
        print('slice')
        print(response)
        print('slice')
        response = response.split(":")[1:]
        response = "".join(response)

    response=caracteres.remove_caracteres_especiais_inicio(response)
    response=caracteres.remove_caracteres_especiais_final(response)
    
    response=conversation.human_response(response)

    strings = response[0]#? lista de strings
    tempos = response[1]#? lista de tempos
    print('-------------------')
    print(f'Resposta final para:{person_name}')
    for texto, tempo in zip(strings, tempos):
        #! URGENTE filtrar
        #! if texto.startswith(person_name):
        
        #!     texto=texto.split(":")[1:]
        #!     texto="".join(texto)
        print(texto)
        send_msg(matchID,texto)
        t.sleep(tempo)
    print('-------------------')

print(me['bio'])

now = datetime.utcnow()  # get current UTC time
time = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ') 
print('fundo')
print(time)


'''except Exception as e:

        print("AN ERROR OCCURRED:", e)
        now = datetime.utcnow()  # get current UTC time
        formatted_time = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')  # format the time string
        print(formatted_time)
        with open('time.txt', 'w') as f:
            f.write(formatted_time)'''

#!
#?
#//
#todo 
#*
