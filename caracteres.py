import re

def remove_caracteres_especiais_inicio(string):
    padrao = re.compile(r'^[^\w\s!]*')
    return padrao.sub('', string)

def remove_caracteres_especiais_final(string):
    padrao = re.compile(r'[^\w\s?!]+$')
    return padrao.sub('', string)
