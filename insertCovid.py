# -*- coding: cp1252 -*-

from models import *

doencas = [{"nome":"COVID-19", "agente":"SARS-CoV-2", "tipo":"VIRUS", "sintomas":[2, 3, 5], "prevencao":[16, 17, 18, 19], "transmicao":[3]}]

prevencaos=["Manter distância segura entre as pessoas", "Lavar bem as mãos", "Usar o cotovelo ao tossir", "Não sair de casa, se possivel"]

for nome in prevencaos:
    prevencao = Prevencoes(nome=nome)
    prevencao.save()
    
for d in doencas:
    doenca = Doencas(nome=d['nome'], tipo=d['tipo'], agente=d['agente'], sintomas=[], prevencao=[], transmicao=[])
    doenca.save()
    for s in d['sintomas']:
        sintoma = Sintomas.query.all()
        try:
            doenca.sintomas.append(sintoma[s])
            doenca.save()
        except IndexError:
            print("Error")
    
    for p in d['prevencao']:
        prevencaos = Prevencoes.query.all()
        doenca.prevencao.append(prevencaos[p])
        doenca.save()

    for t in d['transmicao']:
        transmicaos = Transmicaos.query.all()
        doenca.transmicao.append(transmicaos[t])
        doenca.save()


