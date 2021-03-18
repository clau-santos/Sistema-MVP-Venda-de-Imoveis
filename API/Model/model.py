from api import  app_, fields


people = app_.namespace('imobiliaria', description='Gerencia pessoas')
modelPeople = app_.model('Pessoas Model', {
                            'nome':fields.String(required = True, 
    					  				description="Nome da pessoa", 
    					  				help="Campo não aceita nulo"),
                            'data_nascimento':fields.Date(required = True, 
    					  				description="Data de nascimento da pessoa", 
    					  				help="Campo não aceita nulo"),      
                            'cpf':fields.String(required = True, 
    					  				description="CPF da pessoa", 
    					  				help="Campo não aceita nulo"),
                            'rg':fields.String(required = True, 
    					  				description="RG da pessoa", 
    					  				help="Campo não aceita nulo"),
                            'telefone':fields.String(required = True, 
    					  				description="Telefone da pessoa", 
    					  				help="Campo não aceita nulo"),
                            'estado_civil':fields.String(required = True, 
    					  				description="Estado Civil da pessoa", 
    					  				help="Campo não aceita nulo"),
                            'profissao':fields.String(required = True, 
    					  				description="Profissão da pessoa", 
    					  				help="Campo não aceita nulo")                               
                                        })

people_put = app_.namespace('imobiliaria', description='Atualiza pessoas')
modelPeople_put = app_.model('Pessoas Model', {
                            'nome':fields.String(description="Nome da pessoa"),
                            'data_nascimento':fields.Date(description="Data de nascimento da pessoa"),      
                            'cpf':fields.String(description="CPF da pessoa"),
                            'rg':fields.String(	description="RG da pessoa"),
                            'telefone':fields.String(description="Telefone da pessoa"),
                            'estado_civil':fields.String(description="Estado Civil da pessoa"),
                            'profissao':fields.String(description="Profissão da pessoa")                               
                                        })


bank = app_.namespace('imobiliaria', description='Gerencia bancos')
modelBank = app_.model('Bancos Model', {
                            'nome':fields.String(required = True, 
    					  			description="Nome do banco", 
    					  			help="Campo não aceita nulo")
                                    })


imoveis = app_.namespace('imobiliaria', description='Gerencia imóveis')
modelImoveis = app_.model('Imoveis Model', {
                            'tipo_imovel':fields.String(required = True, 
    					  				description="Tipo de imóvel", 
    					  				help="Campo não aceita nulo"),
                            'endereco':fields.Date(required = True, 
    					  				description="Endereço do imóvel", 
    					  				help="Campo não aceita nulo"),      
                            'complemento':fields.String(required = True, 
    					  				description="Complemento do imóvel", 
    					  				help="Campo não aceita nulo"),
                            'cep':fields.String(required = True, 
    					  				description="CEP do imóvel", 
    					  				help="Campo não aceita nulo"),
                            'cidade':fields.String(required = True, 
    					  				description="Cidade do imóvel", 
    					  				help="Campo não aceita nulo"),
                            'estado':fields.String(required = True, 
    					  				description="Estado do imóvel", 
    					  				help="Campo não aceita nulo"),
                            'id_pessoa':fields.Integer(required = True, 
    					  				description="Proprietário do imóvel", 
    					  				help="Campo não aceita nulo"),
                            'adquirido_em':fields.Date(required = True, 
    					  				description="Quando o ímovel foi adquirido", 
    					  				help="Campo não aceita nulo")                                
                                        })

imoveis_put = app_.namespace('imobiliaria', description='Atualiza imóveis')
modelImoveis_put = app_.model('Imoveis Model', {
                            'tipo_imovel':fields.String(description="Tipo de imóvel"),
                            'endereco':fields.Date(description="Endereço do imóvel"),      
                            'complemento':fields.String( description="Complemento do imóvel"),
                            'cep':fields.String(description="CEP do imóvel"),
                            'cidade':fields.String( description="Cidade do imóvel"),
                            'estado':fields.String(description="Estado do imóvel"),
                            'id_pessoa':fields.Integer(description="Proprietário do imóvel"),
                            'adquirido_em':fields.Date(description="Quando o ímovel foi adquirido")                                
                                        })


cli = app_.namespace('imobiliaria', description='Gerencia clientes') 
modelClientes = app_.model('Clientes Model', {
                            'id_pessoa':fields.Integer(required = True, 
    					  				description="ID da pessoa", 
    					  				help="Campo não aceita nulo"),
                            'endereco':fields.String(required = True, 
    					  				description="Endereço do cliente", 
    					  				help="Campo não aceita nulo"),      
                            'complemento':fields.String(required = True, 
    					  				description="Complemento do cliente", 
    					  				help="Campo não aceita nulo"),
                            'cep':fields.String(required = True, 
    					  				description="CEP do cliente", 
    					  				help="Campo não aceita nulo"),
                            'cidade':fields.String(required = True, 
    					  				description="Cidade do cliente", 
    					  				help="Campo não aceita nulo"),
                            'estado':fields.String(required = True, 
    					  				description="Estado do cliente", 
    					  				help="Campo não aceita nulo"),
                            'id_banco':fields.Integer(required = True, 
    					  				description="Banco do cliente", 
    					  				help="Campo não aceita nulo"),
                                        })

cli_put = app_.namespace('imobiliaria', description='Gerencia clientes') 
modelClientes_put = app_.model('Clientes Model', {
                            'id_pessoa':fields.Integer(description="ID da pessoa"),
                            'endereco':fields.String(description="Endereço do cliente"),      
                            'complemento':fields.String( description="Complemento do cliente"),
                            'cep':fields.String( description="CEP do cliente"),
                            'cidade':fields.String(description="Cidade do cliente"),
                            'estado':fields.String(description="Estado do cliente"),
                            'id_banco':fields.Integer(description="Banco do cliente"),
                                        })

compras_namespace = app_.namespace('imobiliaria', description='Gerencia compras de Imóveis') 
compras_namespace_put = app_.namespace('imobiliaria', description='Atualiza compras de Imóveis')


modelCompras = app_.model('Compras Model', {
                            'id_imovel':fields.Integer(required = True, 
    					  				description="ID do imóvel", 
    					  				help="Campo não aceita nulo"),
                            'id_cliente':fields.Integer(required = True, 
    					  				description="ID do cliente", 
    					  				help="Campo não aceita nulo"),      
                            'data_compra':fields.Date(required = True, 
    					  				description="Data da compra do imóvel", 
    					  				help="Campo não aceita nulo"),
                            'tipo_venda':fields.String(required = True, 
    					  				description="Tipo de venda", 
    					  				help="Campo não aceita nulo"),
                            'valor_imovel':fields.Integer(required = True, 
    					  				description="Valor do imóvel", 
    					  				help="Campo não aceita nulo"),
                            'valor_entrada':fields.Integer(required = True, 
    					  				description="Valor da entrada", 
    					  				help="Campo não aceita nulo"),
                            'parcelas':fields.Integer(required = True, 
    					  				description="Parcelas ", 
    					  				help="Campo não aceita nulo"),
                                        })

modelCompras_put = app_.model('Compras Model', {
                            'id_imovel':fields.Integer(description="ID do imóvel"),
                            'id_cliente':fields.Integer(description="ID do cliente"),      
                            'data_compra':fields.Date(description="Data da compra do imóvel"),
                            'tipo_venda':fields.String(description="Tipo de venda"),
                            'valor_imovel':fields.Integer(description="Valor do imóvel"),
                            'valor_entrada':fields.Integer(description="Valor da entrada"),
                            'parcelas':fields.Integer(description="Parcelas "),
                                        })

despesas_namespace = app_.namespace('imobiliaria', description='Gerencia despesas do imóvel') 
despesas_namespace_put = app_.namespace('imobiliaria', description='Atualiza as despesas do imóvel')

modelDespesas = app_.model('Despesas Model', {
                            'id_imovel':fields.Integer(required = True, 
    					  				description="ID do imóvel", 
    					  				help="Campo não aceita nulo"),
                            'energia':fields.Integer(required = False, 
    					  				description="Valor da conta de energia", 
    					  				help="Campo aceita nulo"),      
                            'agua':fields.Integer(required = False, 
    					  				description="Valor da conta de água do imóvel", 
    					  				help="Campo aceita nulo"),
                            'condominio':fields.Integer(required = False, 
    					  				description="Valor da conta de condomínio do imóvel", 
    					  				help="Campo aceita nulo"),
                            'propaganda':fields.Integer(required = False, 
    					  				description="Valor da propagando do período de pré venda do imóvel", 
    					  				help="Campo aceita nulo"),
                                        })

modelDespesas_put = app_.model('Despesas Model', {
                            'id_imovel':fields.Integer(required = True, 
    					  				description="ID do imóvel"),
                            'energia':fields.Integer(required = False, 
    					  				description="Valor da conta de energia"),      
                            'agua':fields.Integer(required = False, 
    					  				description="Valor da conta de água do imóvel"),
                            'condominio':fields.Integer(required = False, 
    					  				description="Valor da conta de condomínio do imóvel"),
                            'propaganda':fields.Integer(required = False, 
    					  				description="Valor da propagando do período de pré venda do imóvel")
                                        })