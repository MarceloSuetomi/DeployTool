#!/usr/bin/python
# arquivo: Gitlab.py

import requests
import json


class Gitlab:
    def __init__(self):
        self.token = "y5BAhu9Tdmi84XjSY2yR"
        self.servidor = "192.168.0.3"
        self.headers = {"Content-Type":"application/json"}


    def _post(self, recurso, data):
        response = requests.post("http://{0}/api/v3/{1}?private_token={2}"
                            .format(self.servidor, recurso, self.token)
                            ,data=json.dumps(data),headers=self.headers)
        return response


    def _get(self, recurso):
        response = requests.get("http://{0}/api/v3/{1}?private_token={2}"
                            .format(self.servidor, recurso, self.token)
                            ,headers=self.headers)
        return response


    def criar_usuario(self):
        recurso = "users"
        data = {"username":"teste05","email":"teste05@teste.com",
                "name":"Teste05","password":"4linux123"}
        response = self._post(recurso,data)

        if response.status_code == 201:
            print "Usuario criado com sucessoo"
        else:
            print "Falhou ao criar usuario",response.content


    def criar_projeto(self):
        recurso = "projects"
        data = {"name":"Projeto02"}
        
        response = self._post(recurso,data)
        if response.status_code == 201:
            print "Projeto criado com sucesso"
        else:
            print "Falhou ao criar o Projeto", response.content


    def adicionar_webhook(self,nome,url):
        projetos = self.listar_projetos()
        projeto = [ p for p in projetos if p.get("name") == nome]
#        for p in projetos:    #esse for foi substituido pela linha acima
#            if p.get("name") == nome:
#                pid = p.get("id")
#                print "Projeto ID: ",pid
#                break
#        else:
#            print "Projeto nao encontrado"

        if projeto:
            pid = projeto[0].get("id")
            data = {"name":nome,"url":url}
            recurso = "projects/%s/hooks"%pid
            response = self._post(recurso,data)
            if response.status_code == 201:
                print "Webhook cadastrada com sucesso"
            else:
                print "Falhou ao cadastrar: ", response.content
        else:
            print "Projeto nao encontrado"


    def adicionar_desenvolvedor(self, nome_proj, email):
        projetos = self.listar_projetos()
        projeto = [ p for p in projetos if p.get("name") == nome_proj]

        usuarios = self.listar_usuarios()
        usuario = [ u for u in usuarios if u.get("email") == email]
        if usuario and projeto:
            pid = projeto[0].get("id")
            uid = usuarios[0].get("id")

            data = {"id":pid,"user_id":uid,"access_level":30}
            recurso = "projects/{0}/members".format(pid)
            response = self._post(recurso,data)
            if response.status_code == 201:
                print pid, uid
                print "Desenvolvedor incluido com sucesso"
            else:
                print "Falhou ao incluir desenvolvedor: ", response.content
        else:
            print "Usuario ou Projeto nao encotrado"


    def listar_projetos(self):
        recurso = "projects"

        response = self._get(recurso)
        projetos = json.loads(response.content)

        return projetos
#        for i, p in enumerate(projetos):
#            print i, " - ", p.get("id"), " - ", p.get("name")

    def listar_usuarios(self):
        recurso = "users"

        response = self._get(recurso)
        usuarios = json.loads(response.content)
        return usuarios


if __name__=='__main__':
    g = Gitlab()
#    g.criar_usuario()
    #g.criar_projeto()
#    g.listar_projetos()
#    g.adicionar_webhook("Projeto01","http://jenkins.com.br")
#    g.listar_usuarios()
    g.adicionar_desenvolvedor("Projeto01","teste04@teste.com")

