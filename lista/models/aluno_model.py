from dao import db,Base
from datetime import datetime
from lista.models.voo_model import VooModel

class AlunoModel(Base):

    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.Integer, unique = True)
    nome = db.Column(db.String(200), unique=True)
    #data_criacao = db.Column(db.DateTime)
    voos = db.relationship("VooModel", lazy = 'dynamic')

    def __init__(self, nome, matricula):
        self.nome = nome
        # self.data_criacao = datetime.now()

    def adicionar(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def encontrar_pela_matricula(cls, _matricula):
        return cls.query.filter_by(matricula=_matricula).first()

    @classmethod
    def encontrar_pelo_nome(cls, _nome):
        return cls.query.filter_by(nome=_nome).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        db.session.delete(self)
        db.session.commit()