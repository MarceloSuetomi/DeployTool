#!/usr/bin/python
# arquivo: aula01.py

import requests
import json


def listar():
    response = requests.get("http://localhost:5000/usuarios/")
    response = json.loads(response.content)

    for u in response.get("usuarios"):
        print u.get("id"), u.get("nome"), u.get("email")

# Atualiza usuario
def atualizar():
    uid = raw_input("Entre com o ID do Usuario para atualizar: ")
    novo = {}
    novo["nome"] = raw_input("Digite o novo usuario: ")
    novo["email"] = raw_input("Digite o novo email: ")

    content_type = {"Content-Type":"application/json"}

    response = requests.put("http://localhost:5000/usuarios/{0}/".format(uid),
                            headers=content_type, data=json.dumps(novo))
    print response.content

# Insere novo usuario
def cadastrar():
    novo = {}
    novo["nome"] = raw_input("Digite o novo usuario: ")
    novo["email"] = raw_input("Digite o novo email: ")

    content_type = {"Content-Type":"application/json"}

    response = requests.post("http://localhost:5000/usuarios/",
                            headers=content_type, data=json.dumps(novo))
    print response.content

#Deleta usuario
def deletar():
    listar()
    uid = raw_input("Entre com o ID do Usuario para deletar: ")

    content_type = {"Content-Type":"application/json"}

    response = requests.delete("http://localhost:5000/usuarios/{0}/".format(uid),
                            headers=content_type)
    print response.content


def cadastrar_lote(linha):
        novo = {}
        novo["nome"] = linha
        novo["email"] = novo.get("nome").lower()
        novo["email"] = novo["email"].replace(" ",".")
        novo["email"] += "@dexter.com.br"

        content_type = {"Content-Type":"application/json"}

        response = requests.post("http://localhost:5000/usuarios/",
                                headers=content_type, data=json.dumps(novo))
        print response.content


if __name__ == '__main__':
    with open("usuarios.txt","r") as f:
        for l in f.readlines():
            cadastrar_lote(l)


