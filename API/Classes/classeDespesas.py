from api import db, ForeignKey

class despesas(db.Model):
    __tablename__ = 'despesas'
    id_despesa = db.Column('id_despesa',db.Integer, primary_key =True)
    id_imovel = db.Column(db.Integer, ForeignKey('imovel.id_imovel'))
    energia = db.Column(db.Integer)
    agua = db.Column(db.Integer)
    condominio = db.Column(db.Integer)
    propaganda = db.Column(db.Integer)

    def __init__(self, id_imovel, energia, agua, condominio, propaganda):
        self.id_imovel = id_imovel
        self.energia = energia
        self.agua = agua
        self.condominio = condominio
        self.propaganda = propaganda