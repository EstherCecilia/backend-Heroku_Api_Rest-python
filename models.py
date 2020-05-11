# -*- coding: cp1252 -*-
from sqlalchemy import Table, create_engine, Column, Integer, Float, String, ForeignKey, Boolean 
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


conecteds = Table('conecteds',Base.metadata, 
               Column('id_doenca', Integer, ForeignKey('doencas.id')),
               Column('id_transmicao', Integer, ForeignKey('transmicaos.id'))
    )

conectedSintomaSessaos = Table('conectedSintomaSessaos',Base.metadata, 
               Column('id_sessao', Integer, ForeignKey('dicas.id')),
               Column('id_sintoma', Integer, ForeignKey('sintomas.id'))
    )

conectedTransmicaoSessaos = Table('conectedTransmicaoSessaos',Base.metadata, 
               Column('id_sessao', Integer, ForeignKey('dicas.id')),
               Column('id_transmicao', Integer, ForeignKey('transmicaos.id'))
    )

conectedPrevencaoSessaos = Table('conectedPrevencaoSessaos',Base.metadata, 
               Column('id_sessao', Integer, ForeignKey('dicas.id')),
               Column('id_prevencao', Integer, ForeignKey('prevencoes.id'))
    )



sessaoconect = Table('sessaoconect',Base.metadata, 
               Column('id_sessao', Integer, ForeignKey('sessoes.id')),
               Column('id_doenca', Integer, ForeignKey('doencas.id'))
    )


class Dicas(Base):
    __tablename__='dicas'
    id = Column(Integer, primary_key=True)
    id_sessao = Column(Integer())
    sintoma = relationship('Sintomas', secondary=conectedSintomaSessaos, cascade='all,delete-orphan', single_parent=True, backref=backref('conectedSintomasSessaos', lazy='dynamic', cascade="all"))
    prevencao = relationship("Prevencoes", secondary=conectedPrevencaoSessaos, cascade='all,delete-orphan', single_parent=True, backref=backref('conectedPrevencaosSessaos', lazy='dynamic', cascade="all"))
    transmicao = relationship("Transmicaos", secondary=conectedTransmicaoSessaos, cascade='all,delete-orphan', single_parent=True,backref=backref('conectedTransmicaosSessaos', lazy='dynamic', cascade="all"))
    
    def __repr__(self):
        return '"{}"'.format(self.id)

    def finaliza():
        Sessao.__table__.drop(engine)
        Sessao.__table__.create(engine)


    def commit(self):
        db_session.commit()
        
    def save(self):
        db_session.add(self)
        try:
            db_session.commit()
        except:
            db_session.rollback()
            raise
        
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Transmicaos(Base):
    __tablename__='transmicaos'
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
    transmicao = relationship("Transmicaos", secondary=conecteds, backref=backref('conectedses', lazy='dynamic'))
    tipo = Column(String(40))
    agente = Column(String(40))

    def __repr__(self):
        return '{}'.format(self.sintomas)


    def save(self):
        db_session.add(self)
        db_session.commit()

    
    def finaliza():
        Doencas.__table__.drop(engine)
        Doencas.__table__.create(engine)


    def delete(self):
        db_session.delete(self)
        db_session.commit()




        

class Salas(Base):
    __tablename__='salas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    senha = Column(String(40))
    


    def __repr__(self):
        return '<sala: {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Ranking(Base):
    __tablename__='ranking'
    id = Column(Integer, primary_key=True)
    ordem = Column(Integer())
    id_sessao = Column(Integer())
    nome = Column(String(40))
    adivinhador = Column(Boolean())
    pontuacao = Column(Float())
    rodada = Column(Integer())
    


    def __repr__(self):
        return '<Ranking: {}>'.format(self.nome)

    def get_pontuacao(self):
        return self.pontuacao

    def finaliza():
        Ranking.__table__.drop(engine)
        Ranking.__table__.create(engine)


    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()




class Sessao(Base):
    __tablename__='sessoes'
    id = Column(Integer, primary_key=True)
    id_sessao = Column(Integer())
    rodada = Column(Integer())
    doencas = relationship("Doencas", secondary=sessaoconect, cascade='all,delete-orphan', single_parent=True, backref=backref('sessaoconects', lazy='dynamic', cascade="all"))
    
    def __repr__(self):
        return '<Sessao: {}>'.format(self.id_sessao)


    def finaliza():
        Sessao.__table__.drop(engine)
        Sessao.__table__.create(engine)



    def save(self):
        db_session.add(self)
        try:
            db_session.commit()
        except:
            db_session.rollback()
            raise
        
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()




        

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()

    
