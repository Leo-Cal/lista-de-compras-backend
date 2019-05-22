 #-*- coding: utf-8 -*-
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from lista.schemas.lista_schema import ListaSchema
from lista.models.aluno_model import AlunoModel
from lista.models.voo_model import VooModel

class VooSchema(ModelSchema):
    voo_aluno= fields.Nested("AlunoSchema", many = True)
    voo_instrutor = fields.Nested("InstrutorSchema", many=True)
    class Meta:
        model = VooModel