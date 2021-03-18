from api import db, ForeignKey

class clientes(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column('id_cliente',db.Integer, primary_key =True)
    id_pessoa = db.Column(db.Integer, ForeignKey('pessoas.id_pessoa'))
    endereco = db.Column(db.String(255), nullable=False)
    complemento = db.Column(db.String(255), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    cidade = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(255), nullable=False)
    id_banco = db.Column(db.Integer, ForeignKey('bancos.id_banco'))


    def __init__(self, id_pessoa, endereco, complemento, cep, cidade, estado, id_banco):
        self.id_pessoa = id_pessoa
        self.endereco = endereco
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.id_banco = id_banco