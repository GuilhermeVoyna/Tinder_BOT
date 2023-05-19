import sys
sys.path.append('./tinder_api')
from tinder_api_sms import get_updates
from conversation import get_file , get_name
import os
import json
import conversation

def save(message_list,matchID=None):

    if matchID==None and len(message_list)>0:
        matchID=message_list[0]
    else: 
        print(message_list)
    

    folder_path = 'conversations' 
    file_name=f'{matchID}.json'
    path=f'{folder_path}/{file_name}'
    if os.path.exists(path):   
        data = get_file(matchID)
        new_update=message_list[2:]
        data.extend(new_update)
        with open(path, "w") as f:
            json.dump(data, f,ensure_ascii=False)
    elif len(matchID)==48:
        # O arquivo não existe, então vamos criá-lo com algum conteúdo inicial
        data=message_list
        with open(path, "w") as f:
            json.dump(data, f,ensure_ascii=False)

def get_history(update,matchID,selfId,salvar=False):
    message_list=[  ]    
    for messages in update['matches']:#? messages = list

        if messages['_id']==matchID:   #* se o matchId da pessoa

            
            if 'person' in messages: #* se o nome for conhecido
                name=messages['person']['name']
                message_list.insert(1,name)
                name=name[0]
                search=False
            else:                #* se o nome for desconhecido
                search=True
                name='ERROR'            
            message_list.insert(0,matchID)

            for message in messages['messages']:#* pega as mensagens 
                personName= name
                finalName='ERROR' 

                if search: #* se o nome for desconhecido procura o nome
                    personId=conversation.get_personId(matchID,selfId)
                    personName=get_name(personId)               
                    search=False#* para de procurar por nome
                    message_list.insert(1,personName)
                    name=personName[0]
                    personName=name
                    finalName=personName#* colocamos o nome da pessoa

                if (message['from']) == selfId: #* se a mensagem for do bot
                    finalName='BOT'
                else:
                    finalName=message_list[1]

                message=message['message']
                message_list.append(f'{finalName} fala: {message}')
    if salvar:
        save(message_list)
        
    return message_list   

def test_print(input):
    print(input)



#matchId='5b3c66c9226c1e3e29dfa1895df711009290cc0100ea5c7f'
#selfId='5b3c66c9226c1e3e29dfa189'
#time='2023-05-14T03:15:46.645789Z'
#print(get_history(time,selfId,matchId))










       
