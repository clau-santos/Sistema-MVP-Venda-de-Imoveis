from api import db, ForeignKey

class imovel(db.Model):
    __tablename__ = 'imovel'
    id_imovel = db.Column('id_imovel',db.Integer, primary_key =True)
    tipo_imovel = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    complemento = db.Column(db.String(255), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    cidade = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(255), nullable=False)
    id_pessoa = db.Column(db.Integer, ForeignKey('pessoas.id_pessoa'))
    adquirido_em = db.Column(db.Date)


    def __init__(self, tipo_imovel, endereco, complemento, cep, cidade, estado, id_pessoa, adquirido_em):
        self.tipo_imovel = tipo_imovel
        self.endereco = endereco
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.id_pessoa = id_pessoa
        self.adquirido_em = adquirido_em