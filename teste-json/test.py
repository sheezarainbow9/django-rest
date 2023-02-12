import requests
import json

 
def buscar_dados():
    request = requests.get("https://610f-168-194-12-61.sa.ngrok.io/alunoapi/aluno/")
    dados = json.loads(request.content)
    print(dados)
    #print(dados[0]['nome'])
    print()

def colocar_dados():
    play = {"nome": "carlos", "description": "teste", "telefone": 8134444564, "email": "carlos@gmail.com", "data_nasc": "1988-03-23", "user": 2}
    url = "https://610f-168-194-12-61.sa.ngrok.io/alunoapi/aluno/" 
    request = requests.get(url, data=play)
    print() 

def deletar_dados():
    request = requests.delete("https://8ec3-168-194-12-61.sa.ngrok.io/alunoapi/aluno/1")
    print()


buscar_dados()
colocar_dados()
#deletar_dados()
