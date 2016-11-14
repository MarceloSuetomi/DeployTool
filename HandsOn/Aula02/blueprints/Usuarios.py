#!/usr/bin/python
# arquivo: Usuarios.py

from flask import Blueprint, jsonify, request
from Models.APIModel import Usuarios as UsuariosModel
import json

usuario_bp = Blueprint('usuarios',__name__)


@usuario_bp.route("/usuarios/")
def listar_usuarios():
    usuarios = UsuariosModel.objects().to_json()
    retorno = {"usuarios":json.loads(usuarios)}
    return jsonify(retorno)

@usuario_bp.route("/usuarios/",methods=["POST"])
def cadastrar_usuario():
    novo = request.get_json()
    u = UsuariosModel()
    u.nome = novo.get("nome")
    u.email = novo.get("email")
    u.save()

    retorno = {"message":"Usuario cadastrado com sucesso"}
    return jsonify(retorno)

@usuario_bp.route("/usuarios/<id>/",methods=["PUT"])
def atualizar_usuario(id):
    novo = request.get_json()
    usuario = UsuariosModel.objects(id=id).first()
    usuario.nome = novo.get("nome")
    usuario.email = novo.get("email")
    usuario.save()

    retorno = {"message":"Usuarios ID {0} atualizado com sucesso".format(id)}
    return jsonify(retorno)

@usuario_bp.route("/usuarios/<id>/",methods=["DELETE"])
def deletar_usuario(id):
    usuario = UsuariosModel.objects(id=id).first()
    usuario.delete()

    retorno = {"message":"Usuario ID {0} removido com sucesso".format(id)}
    return jsonify(retorno)




