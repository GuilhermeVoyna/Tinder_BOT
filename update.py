import sys
sys.path.append('./tinder_api')
from tinder_api_sms import get_updates
from conversation import get_file , get_name
import os
import json

def save(message_list,matchID=None):

    if matchID==None and len(message_list)>0:
        matchID=message_list[0]
    else: 
        print(message_list)
        matchID = 'ERROR'
    

    folder_path = 'conversations' 
    file_name=f'{matchID}.json'
    path=f'{folder_path}/{file_name}'
    if os.path.exists(path):   
        data = get_file(matchID)
        new_update=message_list[2:]
        data.append(new_update)
        with open(path, "w") as f:
            json.dump(data, f,ensure_ascii=False)
    elif len(matchID)==48:
        # O arquivo não existe, então vamos criá-lo com algum conteúdo inicial
        data=message_list
        with open(path, "w") as f:
            json.dump(data, f,ensure_ascii=False)

    
def get_personId(matchId,selfId):
    return matchId.replace(selfId, "")

def get_update(update,selfId):

    match=None
    for messages in update['matches']:#? messages = list
        #//print(message_list)
        message_list=['matchId']
        if 'person' in messages: #* se o nome for conhecido
            name=[messages['person']['name']]
            message_list.insert(1,name)
            name=name[0]
            search=False
        else:                #* se o nome for desconhecido
            search=True

        for message in messages['messages']: 

            personName=name
            matchID=(message['match_id'])
            finalName='ERROR' 

            if match != matchID: #* se o matchId mudar
                match=matchID
                del message_list[0]
                message_list.insert(0,matchID)
    
            if search: #* se o nome for desconhecido procura o nome
                personId=get_personId(matchID,selfId)
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
            message_list.append([f'{finalName} fala: {message}'])
        save(message_list)#* salva as mensagens em um json

#//test_selfId='5b3c66c9226c1e3e29dfa189'
#//test_time='2023-05-14T03:15:46.645789Z'
#//test_update=get_updates(#//test_time)
#get_update(#//test_update,selfId=#//test_selfId)










       
