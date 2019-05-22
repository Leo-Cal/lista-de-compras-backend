from dao import db,Base
from datetime import datetime
from lista.models.instrutor_model import InstrutorModel


class VooModel(Base):

    __tablename__ = 'voos'
    id = db.Column(db.Integer, primary_key=True)
    #matricula = db.Column(db.Integer, unique = True)
    duracao = db.Column(db.String(200))
    data = db.Column(db.DateTime)
    parecer = db.Column(db.Integer)
    aluno_nome = db.Column(db.Integer, db.ForeignKey('alunos.nome'))
    instrutor_nome = db.Column(db.Integer , db.ForeignKey('instrutores.nome'))
    voo_aluno = db.relationship("AlunoModel")
    voo_instrutor = db.relationship("InstrutorModel")


    def __init__(self, duracao, parecer, aluno_nome, instrutor_nome):
        self.duracao = duracao
        self.parecer = parecer
        self.aluno_nome = aluno_nome
        self.instrutor_nome = instrutor_nome

    def adicionar(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def encontrar_pelo_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def listar(cls):
        return cls.query.all()

    def remover(self):
        db.session.delete(self)
        db.session.commit()