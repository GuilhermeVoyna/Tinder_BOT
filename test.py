import sys
sys.path.append('./tinder_api')
from tinder_api_sms import *;
import pprint
import datetime
import string

import bot
import conversation
printer = pprint.PrettyPrinter(indent=4)

me=get_self()
recs=get_recommendations()
print(me['bio'])

quazmo = '62401030088f0a0100eaf05c'
guerra = '5b3c66c9226c1e3e29dfa189'
matchID="5b3c66c9226c1e3e29dfa18962401030088f0a0100eaf05c"

match_name = 'Guilherme'

#mess=bot.generate_intro(match_name,"Guerra *°7")
#send_msg(matchID,mess)

date = str(datetime.datetime.now()).replace(" ", "");

selfId = me["_id"];
count = "1";
match_dict = all_matches(count);

matches=match_dict['data']['matches']

#todo: Responde novas mensagems
for user in matches:

    userId = user['_id'];
    if user['messages']:
        lastMessage = user['messages'][-1];
        if lastMessage['from'] != selfId:
            personId=lastMessage['from']
            message = lastMessage['message'];
            matchID=user['messages'][-1]['match_id']
            person_name=conversation.get_name(personId)
            print(message)
            response=bot.generate_intro(person_name,'Adoro videogames e sair para praia')

            print(send_msg(matchID,response))

            conversation.save(matchID,personId,message)
            conversation.save(matchID,selfId,response)
        

print(recs)
#!
#?
#//
#todo 
#*
