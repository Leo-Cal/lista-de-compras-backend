# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from lista.resources.item_resource import ItemResource, ItensResource
from lista.resources.usuario_resource import UsuarioResource,UsuariosResource
from lista.resources.lista_resource import ListaResource, ListasResource
from lista.resources.aluno_resource import AlunoResource, AlunosResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

app.secret_key = 'secreto'

#fim configurações relativas ao sqlalchemy
api = Api(app)
CORS(app,resources={r"/*": {"origins": "*"}}) #O uso do cors
#cria as tabelas do banco de dados, caso elas não estejam criadas
@app.before_first_request
def create_tables():
    print("criar tabelas")
    db.create_all()
#fim criaçaõ de tabelas

api.add_resource(ItensResource, '/itens')
api.add_resource(ItemResource, '/item', '/item/<string:item>')


api.add_resource(ListasResource, '/listas')
api.add_resource(ListaResource, '/lista','/lista/<string:lista>')
api.add_resource(UsuarioResource,'/usuario','/usuario/<string:nome>')
api.add_resource(UsuariosResource, '/usuarios')
api.add_resource(AlunosResource, '/aluno')

if __name__ == '__main__':
    from dao import db
    db.init_app(app)
    app.run(port=5000,debug=True)
