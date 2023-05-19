import sys
sys.path.append('./tinder_api')
from tinder_api_sms import *
import json

import random


def get_name(_id):
    try:
        name=get_person(_id)['results']['name']
        return name
    except:
        return 'BAN'

def get_bio(_id):
    try:
        bio=get_person(_id)['results']['bio']
        return bio
    except:
        return None
#//default='{"num_message":[{"message":"message","from": "name"}]}'
def get_personId(matchId,selfId):
    return matchId.replace(selfId, "")

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
        return[]
        print(f"Error: file '{file_name}' not found.")

def human_response(string):
    caracteres_especiais = "!.?"
    string_list = []
    delay_list = []
    message = ''

    for i, char in enumerate(string):
        message += char
        if char in caracteres_especiais and i < len(string) - 1:
            if string[i+1] not in caracteres_especiais:
                string_list.append(message)
                delay=len(message)*200*random.random()/1000
                delay_list.append(delay)
                message = ''
        elif i == len(string) - 1:
            string_list.append(message)
            delay=len(message)*200*random.random()/1000
            delay_list.append(delay)
    string_list =  [s.lstrip() for s in string_list]
    return string_list , delay_list     
