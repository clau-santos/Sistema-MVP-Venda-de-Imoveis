from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
import json
from flask_restplus import Api, Resource, fields
from flask_cors import CORS, cross_origin 

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
CORS(app)
cross_origin(app=app, methods=['GET', 'POST', 'PUT', 'DELETE'])

app_ = Api(app = app, 
		  version = "1.0", 
		  title = "Venda de Imóveis", 
		  description = "Sistema MVP 0 de venda de imóveis")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/imobiliaria'

db = SQLAlchemy(app)

from Classes.classePessoa import pessoas
from Classes.classeBanco import bancos
from Classes.classeImovel import imovel
from Classes.classeCliente import clientes
from Classes.classeCompras import compras
from Classes.classeDespesas import despesas
from Model.model import *

db.create.all()

#MÉTODO GET E POST
@people.route('/pessoas')
class MainClassPessoas(Resource):

    @app_.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def get(self):
            try:
                allpessoas = pessoas.query.all()
                output= []
                for pessoa in allpessoas:
                    currpessoa = {}
                    currpessoa['id'] = pessoa.id_pessoa
                    currpessoa['nome'] = pessoa.nome
                    currpessoa['data_nascimento'] = pessoa.data_nascimento
                    currpessoa['cpf'] = pessoa.cpf
                    currpessoa['rg'] = pessoa.rg
                    currpessoa['telefone'] = pessoa.telefone
                    currpessoa['estado_civil'] = pessoa.estado_civil
                    currpessoa['profissao'] = pessoa.profissao
                    output.append(currpessoa)
                return jsonify(output)
            except KeyError as e:
                people.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
            except Exception as e:
                people.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

 # @people.route('/pessoa/adicionar', methods=['POST'])
    @app_.expect(modelPeople)
 # class MainClass(Resource):
    def post(self):

        body = request.get_json()
        nova_pessoa = pessoas(nome=body["nome"],data_nascimento=body["data_nascimento"],cpf=body["cpf"],rg=body["rg"], telefone=body["telefone"],estado_civil=body["estado_civil"],profissao=body["profissao"])
        db.session.add(nova_pessoa)
        db.session.commit()
        return jsonify(body)

#MÉTODO DELETE
@people.route('/pessoa/<int:id_pessoa>', methods=['DELETE'])
@app_.doc(params={'id_pessoa': 'ID referente a pessoa que deseja excluir'})
class MainClassPessoas(Resource):
    def delete(self, id_pessoa):
        dado_pessoa = pessoas.query.filter(pessoas.id_pessoa==id_pessoa).delete()
        db.session.commit()
        return jsonify(dado_pessoa)

#MÉTODO PUT
@people_put.route('/<int:id_pessoa>', methods=['PUT'])
class MainClassPessoas(Resource):
    @app_.doc(params={'id_pessoa': 'ID referente a pessoa que deseja atualizar'})
    def get(self, id_pessoa):
        id_pessoa = id_pessoa
        allpessoas = pessoas.query.all()
        output= []
        for pessoa in allpessoas:
            currpessoa = {}
            currpessoa['id'] = pessoa.id_pessoa
            currpessoa['nome'] = pessoa.nome
            currpessoa['data_nascimento'] = pessoa.data_nascimento
            currpessoa['cpf'] = pessoa.cpf
            currpessoa['rg'] = pessoa.rg
            currpessoa['telefone'] = pessoa.telefone
            currpessoa['estado_civil'] = pessoa.estado_civil
            currpessoa['profissao'] = pessoa.profissao
            output.append(currpessoa)
        return jsonify(output)


    @app_.expect(modelPeople_put)
    def put(self,id_pessoa):
        pessoa_put = pessoas.query.get(id_pessoa)
        pessoa_put.nome = request.json.get('nome', pessoa_put.nome)
        pessoa_put.data_nascimento = request.json.get('data_nascimento', pessoa_put.data_nascimento)
        pessoa_put.cpf = request.json.get('cpf', pessoa_put.cpf)
        pessoa_put.rg = request.json.get('rg', pessoa_put.rg)
        pessoa_put.telefone = request.json.get('telefone', pessoa_put.telefone)
        pessoa_put.estado_civil = request.json.get('estado_civil', pessoa_put.estado_civil)
        pessoa_put.profissao = request.json.get('profissao', pessoa_put.profissao)

        db.session.commit()
        return jsonify ({'nome': pessoa_put.nome})


@bank.route('/banco')
class MainClassBanco(Resource):

    @app_.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    def get(self):
            try:
                allbancos = bancos.query.all()
                output= []
                for banco in allbancos:
                    currbanco = {}
                    currbanco['id_banco'] = banco.id_banco
                    currbanco['banco'] = banco.nome
                    output.append(currbanco)
                return jsonify(output)
            except KeyError as e:
                people.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
            except Exception as e:
                people.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

    @app_.expect(modelBank)
    def post(self):

        banco = request.get_json()
        novo_banco = bancos(nome=banco["nome"])
        db.session.add(novo_banco)
        db.session.commit()
        return jsonify(banco)


#MÉTODO GET
@imoveis.route('/imovel')
class MainClassImovel(Resource):     
    @app_.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })   

    def get(self):
            try: 
                allimoveis = imovel.query.all()
                output= []
                for imvl in allimoveis:
                    currimvl = {}
                    currimvl['id'] = imvl.id_imovel
                    currimvl['tipo_imovel'] = imvl.tipo_imovel
                    currimvl['endereco'] = imvl.endereco
                    currimvl['complemento'] = imvl.complemento
                    currimvl['cep'] = imvl.cep
                    currimvl['cidade'] = imvl.cidade
                    currimvl['estado'] = imvl.estado
                    currimvl['id_pessoa'] = imvl.id_pessoa
                    currimvl['adquirido_em'] = imvl.adquirido_em
                    output.append(currimvl)
                return jsonify(output)
            except KeyError as e:
                people.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
            except Exception as e:
                people.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")


    @app_.expect(modelImoveis)
    def post(self):
        imo = request.get_json()
        novo_imovel = imovel(tipo_imovel=imo["tipo_imovel"],endereco=imo["endereco"],complemento=imo["complemento"],cep=imo["cep"], cidade=imo["cidade"],estado=imo["estado"],id_pessoa=imo["id_pessoa"], 
        adquirido_em=imo["adquirido_em"])
        db.session.add(novo_imovel)
        db.session.commit()
        return jsonify(imo)

# METODO DELETE
@imoveis.route('/imovel/<int:id_imovel>', methods=['DELETE'])
@app_.expect(modelImoveis)
@app_.doc(params={'id_imovel': 'ID referente ao que deseja excluir'})
class MainClass(Resource):
    def delete(self, id_imovel):
        dado_imovel = imovel.query.filter(imovel.id_imovel==id_imovel).delete()
        db.session.commit()
        return jsonify(dado_pessoa)

#MÉTODO PUT
@imoveis_put.route('/<int:id_imovel>', methods=['PUT'])
class MainClass(Resource):
    @app_.doc(params={'id_imovel': 'ID referente ao imovel que deseja atualizar'})
    def get(self, id_imovel):
        id_imovel = id_imovel
        allimoveis = imovel.query.all()
        output= []
        for imvl in allimoveis:
            currimvl = {}
            currimvl['id'] = imvl.id_imovel
            currimvl['tipo_imovel'] = imvl.tipo_imovel
            currimvl['endereco'] = imvl.endereco
            currimvl['complemento'] = imvl.complemento
            currimvl['cep'] = imvl.cep
            currimvl['cidade'] = imvl.cidade
            currimvl['estado'] = imvl.estado
            currimvl['id_pessoa'] = imvl.id_pessoa
            currimvl['adquirido em'] = imvl.adquirido_em
            output.append(currimvl)
        return jsonify(output)


    @app_.expect(modelImoveis_put)
    def put(self, id_imovel):
        imovel_put = imovel.query.get(id_imovel)
        imovel_put.tipo_imovel = request.json.get('tipo_imovel', imovel_put.tipo_imovel)
        imovel_put.endereco = request.json.get('endereco', imovel_put.endereco)
        imovel_put.complemento = request.json.get('complemento', imovel_put.complemento)
        imovel_put.cep = request.json.get('cep', imovel_put.cep)
        imovel_put.cidade = request.json.get('cidade', imovel_put.cidade)
        imovel_put.estado = request.json.get('estado', imovel_put.estado)
        imovel_put.adquirido_em = request.json.get('adquirido_em', imovel_put.adquirido_em)
        db.session.commit()
        return jsonify ({'imovel': imovel_put.id_imovel})



#MÉTODO GET
@cli.route('/cliente')
class MainClass(Resource):        
    def get(self):
            try:
                allclientes = clientes.query.all()
                output= []
                for clt in allclientes:
                    currclt = {}
                    currclt['id'] = clt.id_cliente
                    currclt['id_pessoa'] = clt.id_pessoa
                    currclt['endereco'] = clt.endereco
                    currclt['complemento'] = clt.complemento
                    currclt['cep'] = clt.cep
                    currclt['cidade'] = clt.cidade
                    currclt['estado'] = clt.estado
                    currclt['id_banco'] = clt.id_banco
                    output.append(currclt)
                return jsonify(output)
            except KeyError as e:
                people.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
            except Exception as e:
                people.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")



    @app_.expect(modelClientes)
    def post(self):
        clie = request.get_json()
        novo_cliente = clientes(id_pessoa=clie["id_pessoa"], endereco=clie["endereco"], complemento=clie["complemento"], cep=clie["cep"], cidade=clie["cidade"], estado=clie["estado"], id_banco=clie["id_banco"])
        db.session.add(novo_cliente)
        db.session.commit()
        return jsonify(clie)

#MÉTODO DELETE        
@cli.route('/cliente/<int:id_cliente>', methods=['DELETE'])


@cli.route('/<int:id_cliente>', methods=['DELETE'])
@app_.doc(params={'id_cliente': 'ID referente ao cliente que deseja excluir:'})
class MainClass(Resource):
    def delete(self, id_cliente):
        dado_cliente = clientes.query.filter(clientes.id_cliente==id_cliente).delete()
        db.session.commit()
        return jsonify(dado_cliente)

#MÉTODO PUT
@cli_put.route('/cliente/<int:id_compras>', methods=['PUT'])
class MainClass(Resource):
    @app_.doc(params={'id_compras': 'ID referente a compra que deseja atualizar'})
    def get(self, id_compras):
        id_compras = id_compras
        allclientes = clientes.query.all()
        output= []
        for clt in allclientes:
            currclt = {}
            currclt['id'] = clt.id_cliente
            currclt['id_pessoa'] = clt.id_pessoa
            currclt['endereco'] = clt.endereco
            currclt['complemento'] = clt.complemento
            currclt['cep'] = clt.cep
            currclt['cidade'] = clt.cidade
            currclt['estado'] = clt.estado
            currclt['id_banco'] = clt.id_banco
            output.append(currclt)
        return jsonify(output)


    @app_.expect(modelClientes_put)
    def put(self, id_cliente):
        cliente_put = imovel.query.get(id_cliente)
        cliente_put.id_pessoa = request.json.get('id_pessoa', cliente_put.id_pessoa)
        cliente_put.endereco = request.json.get('endereco', cliente_put.endereco)
        cliente_put.complemento = request.json.get('complemento', cliente_put.complemento)
        cliente_put.cep = request.json.get('cep', cliente_put.cep)
        cliente_put.cidade = request.json.get('cidade', cliente_put.cidade)
        cliente_put.estado = request.json.get('estado', cliente_put.estado)
        cliente_put.id_banco = request.json.get('id_banco', cliente_put.id_banco)
        db.session.commit()
        return jsonify ({'compra': cliente_put.id_compra})


#MÉTODO GET
@compras_namespace.route('/compras')
class MainClassCompras(Resource):        

    def get(self):
            try: 
                allcompras = compras.query.all()
                output= []
                for compra in allcompras:
                    currcompra = {}
                    currcompra['id'] = compra.id_compras
                    currcompra['id_imovel'] = compra.id_imovel
                    currcompra['id_cliente'] = compra.id_cliente
                    currcompra['data_compra'] = compra.data_compra
                    currcompra['tipo_venda'] = compra.tipo_venda
                    currcompra['valor_imovel'] = compra.valor_imovel
                    currcompra['valor_entrada'] = compra.valor_entrada
                    currcompra['parcelas'] = compra.parcelas
                    output.append(currcompra)
                return jsonify(output)
            except KeyError as e:
                people.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
            except Exception as e:
                people.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

#MÉTODO POST

    @app_.expect(modelCompras)

    def post(self):
        nova_compra = request.get_json()
        compra = compras(id_imovel=nova_compra["id_imovel"], id_cliente=nova_compra["id_cliente"], data_compra=nova_compra["data_compra"], tipo_venda=nova_compra["tipo_venda"], valor_imovel=nova_compra["valor_imovel"],valor_entrada=nova_compra["valor_entrada"], parcelas=nova_compra["parcelas"])
        db.session.add(compra)
        db.session.commit()
        return jsonify(nova_compra)

#MÉTODO DELETE
@compras_namespace.route('/compras/<int:id_compras>', methods=['DELETE'])
@app_.doc(params={'id_compras': 'ID referente a compra que deseja excluir'})
class MainClass(Resource):

    def delete(self, id_compras):
        dado_compra = compras.query.filter(compras.id_compras==id_compras).delete()
        db.session.commit()
        return jsonify(dado_compra)

#MÉTODO PUT
@compras_namespace_put.route('/<int:id_compras>', methods=['PUT'])
class MainClass(Resource):

    @app_.doc(params={'id_compras': 'ID referente a compra que deseja atualizar'})
    def get(self, id_compras):
        id_compras = id_compras
        allcompras = compras.query.all()
        output= []
        for compra in allcompras:
            currcompra = {}
            currcompra['id'] = compra.id_compras
            currcompra['id_imovel'] = compra.id_imovel
            currcompra['id_cliente'] = compra.id_cliente
            currcompra['data_compra'] = compra.data_compra
            currcompra['tipo_venda'] = compra.tipo_venda
            currcompra['valor_imovel'] = compra.valor_imovel
            currcompra['valor_entrada'] = compra.valor_entrada
            currcompra['parcelas'] = compra.parcelas
            output.append(currcompra)
        return jsonify(output)


    @app_.expect(modelCompras_put)
    def put(self, id_compras):
        compra_put = compras.query.get(id_compras)
        compra_put.id_imovel = request.json.get('id_imovel', compra_put.id_imovel)
        compra_put.id_cliente = request.json.get('id_cliente', compra_put.id_cliente)
        compra_put.data_compra = request.json.get('data_compra', compra_put.data_compra)
        compra_put.tipo_venda = request.json.get('tipo_venda', compra_put.tipo_venda)
        compra_put.valor_imovel = request.json.get('valor_imovel', compra_put.valor_imovel)
        compra_put.valor_entrada = request.json.get('valor_entrada', compra_put.valor_entrada)
        compra_put.parcelas = request.json.get('parcelas', compra_put.parcelas)
        db.session.commit()
        return jsonify ({'compra': compra_put.id_compras})


@despesas_namespace.route('/despesas')
class MainClassDespesa(Resource):        

    def get(self):
            try: 
                alldespesas = despesas.query.all()
                output= []
                for despesa in alldespesas:
                    currdespesa = {}
                    currdespesa['id_despesa'] = despesa.id_despesa
                    currdespesa['id_imovel'] = despesa.id_imovel
                    currdespesa['energia'] = despesa.energia
                    currdespesa['agua'] = despesa.agua
                    currdespesa['condominio'] = despesa.condominio
                    currdespesa['propaganda'] = despesa.propaganda
                    output.append(currdespesa)
                return jsonify(output)
            except KeyError as e:
                people.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
            except Exception as e:
                people.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")
            

    @app_.expect(modelDespesas)

    def post(self):
        nova_despesa = request.get_json()
        despesa = despesas(id_imovel=nova_despesa["id_imovel"], energia=nova_despesa["energia"], agua=nova_despesa["agua"], condominio=nova_despesa["condominio"], propaganda=nova_despesa["propaganda"])
        db.session.add(despesa)
        db.session.commit()
        return jsonify(nova_despesa)

@despesas_namespace.route('/<int:id_despesa>', methods=['DELETE'])
@app_.doc(params={'id_despesa': 'ID referente a despesa que deseja excluir:'})
class MainClassDespesa(Resource):
    def delete(self, id_despesa):
        dado_despesa = despesas.query.filter(despesas.id_despesa==id_despesa).delete()
        db.session.commit()
        return jsonify(dado_despesa)

@despesas_namespace_put.route('/despesas/<int:id_despesa>', methods=['PUT'])
class MainClassDespesa(Resource):

    @app_.doc(params={'id_despesa': 'ID referente a despesa que deseja atualizar'})
    def get(self, id_despesa):
        id_despesa = id_despesa
        alldespesas = despesas.query.all()
        output= []
        for despesa in alldespesas:
            currdespesa = {}
            currdespesa['id_despesa'] = despesa.id_despesa
            currdespesa['id_imovel'] = despesa.id_imovel
            currdespesa['energia'] = despesa.energia
            currdespesa['agua'] = despesa.agua
            currdespesa['condominio'] = despesa.condominio
            currdespesa['propaganda'] = despesa.propaganda
            output.append(currdespesa)
        return jsonify(output)

    @app_.expect(modelDespesas_put)
    def put(self, id_despesa):
        despesa_put = despesas.query.get(id_despesa)
        despesa_put.id_imovel = request.json.get('id_imovel', despesa_put.id_imovel)
        despesa_put.energia = request.json.get('energia', despesa_put.energia)
        despesa_put.agua = request.json.get('agua', despesa_put.agua)
        despesa_put.condominio = request.json.get('condominio', despesa_put.condominio)
        despesa_put.propaganda = request.json.get('propaganda', despesa_put.propaganda)
        db.session.commit()
        return jsonify ({'despesa': despesa_put.id_despesa})
