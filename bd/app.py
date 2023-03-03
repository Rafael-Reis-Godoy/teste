import hashlib
from getpass import getpass

def criar_usuario():
    nome=input('Qual é seu nome?')
    idade=input('Qual é a sua idade')
    senha=getpass('Qual sua senha')
    crip_senha(senha, nome, idade)


def crip_senha(senha, nome, idade):
    # Converter a senha em bytes
    senha_bytes = senha.encode('utf-8')

    # Criptografar a senha usando SHA-256
    senha_hash = hashlib.sha256(senha_bytes)

    # Retornar a senha criptografada em formato hexadecimal
    with open('lista.txt', 'w') as arquivo:
    # Escrever as strings no arquivo
       # arquivo.write(nome +'\n')
       # arquivo.write(idade +'\n')
        arquivo.write(senha_hash.hexdigest())
        
def login():
    senha=getpass('Qual sua senha')
    senha_bytes = senha.encode('utf-8')
    senha_hash = hashlib.sha256(senha_bytes)

    with open('lista.txt', 'r') as file:
        senha2 = file.read().strip()
        print(senha2)
    if senha_hash.hexdigest() == senha2 :
        print('senha correta')
    else:
        print(senha_hash.hexdigest() +'/n' + senha2 + '/n errada')



        
   
    
criar_usuario()
login()






