#!/usr/bin/python
# arquivo: APIModel.py

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"db":"dexter-api"}

db = MongoEngine(app)

class Usuarios(db.Document):
    nome = db.StringField()
    email = db.StringField(unique=True)
    data_cadastro = db.DateTimeField(default=datetime.now())

class Grupos(db.Document):
    nome = db.StringField(unique=True)
    integrantes = db.ListField()


if __name__ == '__main__':
    pass
    # => criando novo usuario
    #novo = Usuarios()
    #novo.nome = "Marcelo Kiyoshi"
    #novo.email = "marcelo.kiyoshi@teste.com.br"
    #novo.save()
    # -----------------------
    # => traz o primeiro usuario da consulta
    #usuarios = Usuarios.objects(email="marcelo.kiyoshi@teste.com.br").first()
    # -----------------------
    # => deleta o registro
    #usuarios.delete() 
    # -----------------------
    # => Traz todos os usuarios
    #usuarios = Usuarios.objects()
    # -----------------------
    # => traz todos os usuarios da consulta
    #usuarios = Usuarios.objects(email="marcelo.kiyoshi@teste.com.br")
    #for u in usuarios:
    #    print u.nome, u.email  # dados o objeto
    #    print u.to_json()   # transforma em json
    # -----------------------





