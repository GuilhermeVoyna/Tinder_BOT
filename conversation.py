import sys
sys.path.append('./tinder_api')
from tinder_api_sms import get_person

def get_name(id):
    name=get_person(id)['results']['name']
    return name



def save(matchID,personId,message):
    name = get_name(personId)
    folder_path = 'conversations' 
    file_name=f'{matchID}.txt'
    path=f'{folder_path}/{file_name}'
    with open(path, 'a') as file:
        file.write(f'{name}: {message}\n')

    if cont_lines(path)>=14:
        with open(path, "r") as f:
            lines = f.readlines()

        with open(path, "w") as f:
            f.writelines(lines[1:])
        
def cont_lines(path):
    with open(path, "r") as arquivo:
        lines = 1
        for line in arquivo:
            lines += 1
    return lines

def get(matchID):
    try:
        folder_path = 'conversations' 
        file_name=f'{matchID}.txt'
        path=f'{folder_path}/{file_name}'

        with open(path, "r") as f:
            contents = f.read()
            return contents
    except FileNotFoundError:
        print(f"Error: file '{file_name}' not found.")

