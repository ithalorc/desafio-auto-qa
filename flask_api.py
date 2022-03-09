# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel
import json

#Indicando que a aplicação usará o flask
server = Flask (__name__)

#Especificação da minha API, chamada de api
api = FlaskPydanticSpec('flask', title = 'Super API no Swagger! :D')

#Classe Qa importando BaseModel da biblioteca Pydantic
class Qa(BaseModel):
    nome: str
    
api.register(server) #Minha especificação será do meu servidor // Vai registrar os endpoints do meu servidor

# Pegar algo do servidor
@server.get('/') #Rota, endpoint
def QA_devs():
    """Informa os QAs que fizeram essa página"""
    return 'Ithalo e Rafael'

@server.post('/')
@api.validate(body=Request(Qa))#, resp=Response(HTTP_201=Qa))
def envia_nome():
    """ Verifica Nome para informar sobrenome"""
    x = request.context.body.dict()
    
    #Não consegui entender bem a sintaxe do body, então converti o json gerado para conseguir validar o nome obtido // Gambi Soluções Corp.
    y = json.dumps(x)
    
    if '"Ithalo"' in y:
        return 'Conceição'
    elif '"Rafael"' in y:
        return 'Amodio'
    else:
        return 'QA Inválido.'

server.run()