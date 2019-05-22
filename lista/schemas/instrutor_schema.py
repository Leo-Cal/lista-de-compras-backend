 #-*- coding: utf-8 -*-
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from lista.schemas.lista_schema import ListaSchema
from lista.models.aluno_model import AlunoModel
from lista.models.instrutor_model import InstrutorModel

class InstrutorSchema(ModelSchema):
    voos = fields.Nested("VooSchema", many = True, exclude=('instrutor_id','aluno_id'))
    class Meta:
        model = InstrutorModel