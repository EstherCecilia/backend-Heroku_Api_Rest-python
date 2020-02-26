# -*- coding: cp1252 -*-
from flask import Flask, request
from flask_restful import Resource, Api
import json
from models import *

app = Flask(__name__)
api = Api(app)



class Sintoma(Resource):
    def get(self, nome):
        sintoma = Sintomas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : sintoma.nome,
                'id' : sintoma.id

                }

        except AttributeError:
            response = {'status': 'Error', 'mensagem':'Nome não encontrado'}
            
        return response
    def put(self, nome):
        sintoma = Sintomas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            sintoma.nome = dados['nome']

        sintoma.save()

        response = {
            'id' : sintoma.id,
            'nome' : sintoma.nome
            }

        return response
    
    def delete(self, nome):
        sintoma = Sintomas.query.filter_by(nome=nome).first()
        sintoma.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_sintomas(Resource):
    def get(self):
        sintoma = Sintomas.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in sintoma]
        return response
    
    def post(self):
        dados = request.json
        sintoma = Sintomas(nome=dados['nome'])
        sintoma.save()
        response = {
            'id' : sintoma.id,
            'nome' : sintoma.nome
            }

        return response


class Prevencao(Resource):
    def get(self, nome):
        prevencao = Prevencoes.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : prevencao.nome,
                'id' : prevencao.id

                }

        except AttributeError:
            response = {'status': 'Error', 'mensagem':'Nome não encontrado'}
            
        return response
    def put(self, nome):
        prevencao = Prevencoes.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            prevencao.nome = dados['nome']

        prevencao.save()

        response = {
            'id' : prevencao.id,
            'nome' : prevencao.nome
            }

        return response
    
    def delete(self, nome):
        prevencao = Prevencoes.query.filter_by(nome=nome).first()
        prevencao.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_prevencoes(Resource):
    def get(self):
        prevencao = Prevencoes.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in prevencao]
        return response
    
    def post(self):
        dados = request.json
        prevencao = Prevencoes(nome=dados['nome'])
        prevencao.save()
        response = {
            'id' : prevencao.id,
            'nome' : prevencao.nome
            }

        return response

class Sala(Resource):
    def get(self, nome):
        sala = Salas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome' : sala.nome,
                'senha' : sala.senha,
                'publica' : sala.publica,
                'id' : sala.id

                }

        except AttributeError:
            response = {'status': 'Error', 'mensagem':'Nome não encontrado'}
            
        return response
    
    def put(self, nome):
        sala = Salas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            sala.nome = dados['nome']
            
        if 'senha' in dados:
            sala.senha = dados['senha']

        sala.save()

        response = {
                'nome' : sala.nome,
                'senha' : sala.senha,
                'publica' : sala.publica,
                'id' : sala.id

                }

        return response
    
    def delete(self, nome):
        sala = Salas.query.filter_by(nome=nome).first()
        sala.delete()

        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Lista_salas(Resource):
    def get(self):
        sala = Salas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'publica':i.publica, 'senha':i.senha} for i in sala]
        return response
    
    def post(self):
        dados = request.json
        sala = Salas(nome=dados['nome'], senha=dados['senha'])
        sala.save()
        response = {
                'nome' : sala.nome,
                'senha' : sala.senha,
                'publica' : sala.publica,
                'id' : sala.id

            }

        return response





class Lista_doencas(Resource):
    def get(self):
        doencas = Doencas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'sintoma': i.sintoma.nome, 'prevencao': i.prevencao.nome} for i in doencas]
        return response
    

    def post(self):
        dados = request.json
        sintoma = Sintomas.query.filter_by(nome=dados['sintoma']).first()
        prevencao = Prevencoes.query.filter_by(nome=dados['prevencao']).first()
        doenca = Doencas(nome=dados['nome'], sintoma=sintoma, prevencao=prevencao)
        doenca.save()
        response = {
            'nome' : doenca.nome,
            'sintoma': doenca.sintoma.nome,
            'prevencao': doenca.prevencao.nome,
            'id':doenca.id
        }
        return response
        


class Lista_sessoes(Resource):
    def get(self):
        sessao = Sessoes.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'doenca': i.doenca.nome, 'sala': i.sala.nome} for i in sessao]
        return response
    

    def post(self):
        dados = request.json
        sala = Salas.query.filter_by(nome=dados['sala']).first()
        doenca = Doencas.query.filter_by(nome=dados['doenca']).first()
        sessao = Sessoes(nome=dados['nome'], doenca=doenca, sala=sala)
        sessao.save()
        response = {
            'nome' : sessao.nome,
            'sala': sessao.sala.nome,
            'doenca': sessao.doenca.nome,
            'id':sessao.id
        }
        return response
        
 
    

api.add_resource(Sintoma, '/sintoma/<string:nome>')
api.add_resource(Lista_sintomas, '/sintoma')

api.add_resource(Prevencao, '/prevencao/<string:nome>')
api.add_resource(Lista_prevencoes, '/prevencao')

api.add_resource(Sala, '/sala/<string:nome>')
api.add_resource(Lista_salas, '/sala')

api.add_resource(Lista_doencas, '/doenca')

api.add_resource(Lista_sessoes, '/sessao')

if __name__ == '__main__':
    app.run(debug=True)

    
#debug=true
