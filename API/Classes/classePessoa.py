from api import db

class pessoas(db.Model):
    __tablename__ = 'pessoas'
    id_pessoa = db.Column('id_pessoa',db.Integer, primary_key =True, autoincrement = True, unique = True)
    nome = db.Column(db.String(255), nullable=False)
    data_nascimento = db.Column(db.Date)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    rg =  db.Column(db.String(15), unique=True, nullable=False)
    telefone = db.Column(db.String(11),  nullable=False) 
    estado_civil =  db.Column(db.String(255), nullable=False)
    profissao = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, data_nascimento, cpf, rg, telefone, estado_civil, profissao):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone
        self.estado_civil = estado_civil
        self.profissao = profissao