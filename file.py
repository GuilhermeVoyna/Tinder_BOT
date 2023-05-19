import sys
sys.path.append('./tinder_api')
from tinder_api_sms import get_updates
import conversation
import os
import json

def save(message_list,matchID=None):
    
    if matchID==None:
        matchID=message_list[0]
    else:
        message_list=[f'Guilherme fala: {message_list}']
        print(message_list)

    folder_path = 'conversations' 
    file_name=f'{matchID}.json'
    path=f'{folder_path}/{file_name}'

    if os.path.exists(path):   
        data = conversation.get_file(matchID)
        new_update=message_list[1:]
        with open(path, "w") as f:
            json.dump(new_update, f,ensure_ascii=False)

    elif matchID == 48:
        # O arquivo não existe, então vamos criá-lo com algum conteúdo inicial
        data=message_list
        with open(path, "w") as f:
            json.dump(data, f,ensure_ascii=False)
    else:
        print('ERROR: matchID não encontrado')

def get_all(update,selfId):
    
    match=None
    for messages in update['matches']:#? messages = list

        message_list=['matchId']
        if 'person' in messages: #* se o nome for conhecido
            name=[messages['person']['name']]
            message_list.insert(1,name)
            name=name[0]
            search=False
        else:                #* se o nome for desconhecido
            search=True
            name='ERROR'
#todo-----------------------------------------------------------------------------------------------------------------
        for message in messages['messages']: 
#todo-----------------------------------------------------------------------------------------------------------------
            personName= name

            matchID=    message['match_id']

            finalName='ERROR' 

            if match != matchID: #* se o matchId mudar
                match=matchID
                del message_list[0]
                message_list.insert(0,matchID)
    
            if search: #* se o nome for desconhecido procura o nome
                personId=conversation.get_person(matchID,selfId)
                personName=[get_name(personId)]               
                search=False#* para de procurar por nome
                message_list.insert(1,personName)
                name=personName[0]
                personName=name
            finalName=personName#* colocamos o nome da pessoa

            if (message['from']) == selfId: #* se a mensagem for do bot
               finalName='BOT'
            message=message['message']

            #*  CONVERTER personId para nome
            message_list.append(f'{finalName} fala: {message}')
        save(message_list)#* salva as mensagens em um json