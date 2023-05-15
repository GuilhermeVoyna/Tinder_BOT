import sys
sys.path.append('./tinder_api')
from tinder_api_sms import *
from tinder_api_sms import *
import datetime
from datetime import datetime
import bot
import re
import os
import time as t
import update

def remove_caracteres_especiais_inicio(string):
    padrao = re.compile(r'^[^\w\s!]*')
    return padrao.sub('', string)

def remove_caracteres_especiais_final(string):
    padrao = re.compile(r'[^\w\s?!]+$')
    return padrao.sub('', string)

print('INICIANDO....')
#todo ------------------------------------
with open('time.txt', 'r') as f:
    time=f.read()
me=get_self()
selfId = me["_id"];
time = '2023-05-15T03:20:18.799747Z'
#todo try/wile------------------------------
now = datetime.utcnow()  # get current UTC time
formatted_time = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')  # format the time string
print(formatted_time)


print('topo')
    #* novas mensagens
news=get_updates(time)
update.get_update(news,selfId)

print('updated')
recs=get_recommendations()

print(me['bio'])

quazmo = '62401030088f0a0100eaf05c'
guerra = '5b3c66c9226c1e3e29dfa189'
matchID="5b3c66c9226c1e3e29dfa18962401030088f0a0100eaf05c" #! s2 lindao


count = "80";
match_dict = all_matches(count);

matches=match_dict['data']['matches']

#todo: Responde novas mensagems
for user in matches:

    userId = user['_id'];
    if user['messages']:

        lastMessage = user['messages'][-1];
        
        if lastMessage['from'] != selfId: #? Fui eu que enviei a ultima mensagem?
        
            matchID=user['messages'][-1]['match_id']
            personId=user['messages'][0]['from']
            folder_path = 'conversations' 
            file_name=f'{matchID}.json'
            path=f'{folder_path}/{file_name}'
            try:
                with open(path) as f:
                    data = json.load(f)
                messages_list=data
            except FileNotFoundError:
                print('Erro no historico substitua a variavel -- time -- por '+'2020-05-14T23:35:37.375779Z')

            person_name=user['person']['name']
            try:
                bio = user['person']['bio'] #todo: pega bio do match
            except KeyError:
                bio = None

            response = bot.generate_message(matchID,person_name,bio) 
        else:
            continue
    else: #? matches sem mensagems
        print(user['person']['name'])
        personId=user['participants'][0]
        matchID=user['_id']
        person_name=user['person']['name']
        bio = user['person']['bio'] 
        response = bot.generate_intro(person_name,bio) 


    response = re.sub(r'\b[Bb][Oo][Tt]\b', 'Gui', response)
    if response.startswith("Gui"):
        print('slice')
        print(response)
        print('slice')
        response = response.split(":")[1:]
        response = "".join(response)

    response=remove_caracteres_especiais_inicio(response)
    response=remove_caracteres_especiais_final(response)
    send_msg(matchID,response)
    print('-------------------')
    print(f'Pessoa:{person_name}')
    print(response)
    print('-------------------')
print(me['bio'])

now = datetime.utcnow()  # get current UTC time
time = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ') 
print('fundo')
print(time)
t.sleep(30)

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
