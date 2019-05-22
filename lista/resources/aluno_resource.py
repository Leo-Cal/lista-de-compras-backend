from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.aluno_model import AlunoModel
from lista.models.item_lista_model import ItemLista
from lista.schemas.aluno_schema import AlunoSchema

class AlunoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome',
                        type=str,
                        required=True,
                        help="O nome do aluno não pode estar em branco."
                        )

    def get(self,aluno):
        json = ''
        try:
            aluno = AlunoModel.encontrar_pelo_nome(aluno)
            if aluno:
                schema = AlunoSchema(exclude=['nome'])
                json = schema.dump(aluno).data
            else:
                abort(404, message="Item {} não está na lista".format(aluno))
        except Exception as e:
            print(e)
            abort(404, message="Item {} não está na lista".format(aluno))

        return json,201


    def post(self):
        json = ''
        try:
            data = AlunoResource.parser.parse_args()
            print(data)
            nome = data['nome']
            aluno = AlunoModel.encontrar_pelo_nome(nome)
            if aluno :
                return {"message":"Item {} já está na lista".format(nome)}
            else:
                aluno = AlunoModel(nome=nome)
                aluno.adicionar()
                aluno = AlunoModel.encontrar_pelo_nome(nome)
                schema = AlunoSchema(exclude=['voos'])
                json = schema.dump(aluno).data
        except Exception as e:
            print(e)
            abort(500, message="Erro no POST")
        return json, 201

    # def delete(self,item):
    #     json = []
    #     try:
    #         item = ItemModel.encontrar_pelo_nome(item)
    #         if item:
    #             item.remover()
    #             lista = ItemModel.listar()
    #             schema = ItemSchema(many=True,exclude=['listas'])
    #             json = schema.dump(lista).data
    #         else:
    #             return {"message":"Item {} não está na lista".format(item)},404
    #     except Exception as e:
    #         print(e)
    #     return json, 201

    # def put(self):
    #     json = ''
    #     try:
    #         data = ItemResource.parser.parse_args()
    #         nome = data['item']
    #
    #         item = ItemModel.encontrar_pelo_nome(nome)
    #         if item :
    #             return {"message":"Item {} já está na lista".format(item)},200
    #         else:
    #             item = ItemModel(nome=nome)
    #             item.adicionar()
    #             schema = ItemSchema(many=True)
    #             item = ItemModel.encontrar_pelo_nome(nome)
    #             json = schema.dump(item).data
    #     except Exception as e:
    #         print(e)
    #     return json, 201

class AlunosResource(Resource):
    def get(self):
        json = []
        try:
            alunos = AlunoModel.listar()
            schema = AlunoSchema(many=True)
            json = schema.dump(alunos).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de compras."}, 500
        return json,201