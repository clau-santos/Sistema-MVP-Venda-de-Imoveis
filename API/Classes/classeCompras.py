from api import db, ForeignKey

class compras(db.Model):
    __tablename__ = 'compras'
    id_compras = db.Column('id_compras',db.Integer, primary_key =True)
    id_imovel = db.Column(db.Integer, ForeignKey('imovel.id_imovel'))
    id_cliente = db.Column(db.Integer, ForeignKey('clientes.id_cliente'))
    data_compra = db.Column(db.Date)
    tipo_venda = db.Column(db.String(100), nullable=False)
    valor_imovel = db.Column(db.Integer, nullable=False)
    valor_entrada = db.Column(db.Integer, nullable=False)
    parcelas = db.Column(db.Integer, nullable=False)


    def __init__(self, id_imovel, id_cliente, data_compra, tipo_venda, valor_imovel, valor_entrada, parcelas):
        self.id_imovel = id_imovel
        self.id_cliente = id_cliente
        self.data_compra = data_compra
        self.tipo_venda = tipo_venda
        self.valor_imovel = valor_imovel
        self.valor_entrada = valor_entrada
        self.parcelas = parcelas
