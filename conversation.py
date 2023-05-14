import sys
sys.path.append('./tinder_api')
from tinder_api_sms import *
import json


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

def get_file(matchID):
    try:

        folder_path = 'conversations' 
        file_name=f'{matchID}.json'
        path=f'{folder_path}/{file_name}'

        with open(path, "r") as f:
           return json.load(f)
    except FileNotFoundError:
        print(f"Error: file '{file_name}' not found.")

