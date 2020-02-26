# -*- coding: cp1252 -*-
from models import Sintomas


def insere():
    sintoma = Sintomas(nome="Mal estar")
    print(sintoma)
    sintoma.save()

def consulta():
    sintoma = Sintomas.query.all()
    print(sintoma)


def altera():
    sintoma = Sintomas.query.filter_by(nome='').first()
    sintoma.nome = ''
    sintoma.save()


def deleta():
    sintoma = Sintomas.query.filter_by(nome='').first()
    sintoma.delete()


if __name__ == '__main__':
        #insere()
        consulta()
