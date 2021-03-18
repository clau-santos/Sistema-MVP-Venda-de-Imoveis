from api import db

class bancos(db.Model):
    __tablename__='bancos'
    id_banco = db.Column('id_banco',db.Integer, primary_key =True)
    nome = db.Column(db.String(100), nullable=False)

    def __init__(self, nome):
        self.nome = nome