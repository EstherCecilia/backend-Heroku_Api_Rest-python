# -*- coding: cp1252 -*-
from sqlalchemy import create_engine, Column,Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividade.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Sintomas(Base):
    __tablename__='sintomas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))

    def __repr__(self):
        return '<sintoma: {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
        

class Prevencoes(Base):
    __tablename__='prevencoes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))

    def __repr__(self):
        return '<prevenção: {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()




class Doencas(Base):
    __tablename__='doencas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    sintoma_id = Column(Integer, ForeignKey('sintomas.id'))
    sintoma = relationship("Sintomas")
    prevencao_id = Column(Integer, ForeignKey('prevencoes.id'))
    prevencao = relationship("Prevencoes")


    def __repr__(self):
        return '<doença: {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Salas(Base):
    __tablename__='salas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    senha = Column(String(40))
    publica = Column(String(10))
    


    def __repr__(self):
        return '<sala: {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()



class Sessoes(Base):
    __tablename__='sessoes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    doenca_id = Column(Integer, ForeignKey('doencas.id'))
    doenca = relationship("Doencas")
    sala_id = Column(Integer, ForeignKey('salas.id'))
    sala = relationship("Salas")


    def __repr__(self):
        return '<doença: {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()



def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':

    init_db()


