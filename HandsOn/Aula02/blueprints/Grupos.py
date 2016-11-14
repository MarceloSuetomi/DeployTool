#!/usr/bin/python
# arquivo: Grupos.py

from flask import Blueprint, jsonify, request
from Models.APIModel import Grupos as GruposModel
import json

grupo_bp = Blueprint('grupos',__name__)


@grupo_bp.route("/grupos/")
def listar_grupos():
    grupos = GruposModel.objects().to_json()
    retorno = {"grupos":json.loads(grupos)}    
    return jsonify(retorno)

@grupo_bp.route("/grupos/",methods=["POST"])
def cadastrar_grupo():
    novo = request.get_json()
    g = GruposModel()
    g.nome = novo.get("nome")
    g.save()

    retorno = {"message":"Grupo cadastrado com sucesso"}
    return jsonify(retorno)

@grupo_bp.route("/grupos/<id>/",methods=["POST"])
def adicionar_integrante_grupo(id):
    novo = request.get_json()
    g = GruposModel.objects(id=id).first()
    g.integrantes.append(novo.get("nome"))
    g.save()

    retorno = {"message":"Usuario adicionado ao grupo"}
    return jsonify(retorno)

@grupo_bp.route("/grupos/<id>/",methods=["DELETE"])
def deletar_grupo(id):
    grupo = GruposModel.objects(id=id).first()
    grupo.delete()

    retorno = {"message":"Grupo ID {0} removido com sucesso".format(id)}
    return jsonify(retorno)

