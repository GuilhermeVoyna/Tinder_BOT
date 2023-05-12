import sys
sys.path.append('./tinder_api')
from tinder_api_sms import get_person
import json
import os


def get_name(_id):
    name=get_person(_id)['results']['name']
    return name

def get_bio(_id):
    try:
        bio=get_person(_id)['results']['bio']
        return bio
    except:
        return None
#//default='{"num_message":[{"message":"message","from": "name"}]}'
def count_messages(matchID):
    data=get_file(matchID)
    counter=len(data.items())
    return counter




def save(matchID,personId,message,selfId):
    name = get_name(personId)
    folder_path = 'conversations' 
    file_name=f'{matchID}.json'
    path=f'{folder_path}/{file_name}'
    if personId == selfId:
        name = 'Guilherme'
    
    if os.path.exists(path):
        
        data = get_file(matchID)
        counter=len(data.items())+1
        new_message=[{"message":message,"from": name,"_id": personId,"matchID":matchID}]
        data[counter]=new_message
        with open(path, "w") as f:
            json.dump(data, f,ensure_ascii=False)
        
    else:
        # O arquivo não existe, então vamos criá-lo com algum conteúdo inicial
        data = {"1": [{"message":message,"from": name,"_id": personId,"matchID":matchID}]}
        with open(path, "w") as f:
            json.dump(data, f,ensure_ascii=False)





def get_file(matchID):
    try:

        folder_path = 'conversations' 
        file_name=f'{matchID}.json'
        path=f'{folder_path}/{file_name}'

        with open(path, "r") as f:
           return json.load(f)
    except FileNotFoundError:
        print(f"Error: file '{file_name}' not found.")
