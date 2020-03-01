# -*- coding: cp1252 -*-
from sqlalchemy import Table, create_engine, Column, Integer, String, ForeignKey, Boolean 
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividade.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

conect = Table('conect',Base.metadata, 
               Column('id_doenca', Integer, ForeignKey('doencas.id')),
               Column('id_sintoma', Integer, ForeignKey('sintomas.id'))
    )

conected = Table('conected',Base.metadata, 
               Column('id_doenca', Integer, ForeignKey('doencas.id')),
               Column('id_prevencao', Integer, ForeignKey('prevencoes.id'))
    )

class Sintomas(Base):
    __tablename__='sintomas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))

    def __repr__(self):
        return '"{}"'.format(self.nome)

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
        return '"{}"'.format(self.nome)

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
    sintomas = relationship('Sintomas', secondary=conect, backref=backref('conects', lazy='dynamic'))
    prevencao = relationship("Prevencoes", secondary=conected, backref=backref('conecteds', lazy='dynamic'))
    tipo = Column(String(40))
    agente = Column(String(40))

    def __repr__(self):
        return '{}'.format(self.sintomas)


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
    publica = Column(Boolean)
    


    def __repr__(self):
        return '<sala: {}>'.format(self.nome)

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


