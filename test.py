import sys
sys.path.append('./tinder_api')
from tinder_api_sms import *;
import datetime
from datetime import datetime
import bot
import conversation
import os
import time as t
print('INICIANDO....')
#todo ------------------------------------
with open('time.txt', 'r') as f:
    time=f.read()
me=get_self()
selfId = me["_id"];
update=get_updates(time)

#todo try/wile------------------------------

print('topo')
print(time)
    #pega mensagens antes do update
for messages in update['matches']:#? messages = list
    for message in messages['messages']: #? message = dic
        matchID=(message['match_id'])
        personId=(message['from'])
        message=(message['message'])
        conversation.save(matchID,personId,message,selfId)

recs=get_recommendations()


print(me['bio'])

quazmo = '62401030088f0a0100eaf05c'
guerra = '5b3c66c9226c1e3e29dfa189'
matchID="5b3c66c9226c1e3e29dfa18962401030088f0a0100eaf05c"


#mess=bot.generate_intro(match_name,"Guerra *°7")
#send_msg(matchID,mess)


count = "80";
match_dict = all_matches(count);

matches=match_dict['data']['matches']


#todo: Responde novas mensagems
for user in matches:
    userId = user['_id'];

    if user['messages']:
        lastMessage = user['messages'][-1];

        if lastMessage['from'] != selfId: #? Respondendo mensagens
            
            personId=lastMessage['from']
            message = lastMessage['message'];
            matchID=user['messages'][-1]['match_id']
            person_name=conversation.get_name(personId)
            bio = conversation.get_bio(personId)

            folder_path = 'conversations' 
            file_name=f'{matchID}.json'
            path=f'{folder_path}/{file_name}'
    
            if os.path.exists(path):
    
                response = bot.generate_message(matchID,person_name,bio) #!deve ser criada
                conversation.save(matchID,selfId,response,selfId)
                print(response)

            else:
                response = bot.generate_intro(person_name,bio) 
                conversation.save(matchID,selfId,response,selfId)
            print(response)
            send_msg(matchID,response)

    else: #? matches sem mensagems
        personId=user['participants'][0]
        matchID=user['_id']
        person_name=conversation.get_name(personId)
        bio = conversation.get_bio(personId)
        response = bot.generate_intro(person_name,bio) 
        conversation.save(matchID,selfId,response,selfId)
        send_msg(matchID,response)
        print(response)
        

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
