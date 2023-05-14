import sys
sys.path.append('./tinder_api')
from tinder_api_sms import get_updates
from conversation import get_file , get_name
import os
import json
def save(message_list,matchID=None):

    if matchID==None and len(message_list)>0:
        matchID=message_list[0]
    else: matchID = 'ERROR'
    

    folder_path = 'conversations' 
    file_name=f'{matchID}.json'
    path=f'{folder_path}/{file_name}'
    if os.path.exists(path):   
        data = get_file(matchID)
        new_update=message_list[1:]
        with open(path, "w") as f:
            json.dump(new_update, f,ensure_ascii=False)
    elif len(matchID)==48:
        # O arquivo não existe, então vamos criá-lo com algum conteúdo inicial
        data=message_list
        with open(path, "w") as f:
            json.dump(data, f,ensure_ascii=False)

def get_update(update,selfId):
    message_list=[]
    match=None
    for messages in update['matches']:#? messages = list
        #//print(message_list)
        #//print()
        message_list=[]
        if 'person' in messages: #* se o nome for conhecido
            name=messages['person']['name']
            search=False
        else:                #* se o nome for desconhecido
            search=True

        for message in messages['messages']: 
            personName=name
            matchID=(message['match_id'])
            personId=(message['from'])
            finalName='ERROR' 

            if match != matchID: #* se o matchId mudar
                match=matchID
                message_list.append(matchID)
                #//print(f'\nINICIO DO MATCH: {matchID}\n-------------------') #printa o matchId


            if personId == selfId:#* se a mensagem for do bot
                finalName='BOT'
            else:
                if search: #* se o nome for desconhecido procura o nome
                    personName=get_name(personId)
                    search=False#* para de procurar por nome

                finalName=personName#* colocamos o nome da pessoa
    
            message=message['message']
            #*  CONVERTER personId para nome
            message_list.append(f'{finalName} falou: {message}')
        save(message_list)#* salva as mensagens em um json

#//test_time='2023-05-10T03:15:46.645789Z'
#//test_update=get_updates(_time)
#//get_update(_update)


        





       
