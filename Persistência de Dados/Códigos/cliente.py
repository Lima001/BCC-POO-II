from config import *

class Cliente(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    endereco = db.Column(db.String(254))

    type = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'cliente',
        'polymorphic_on': type
    }

    def __str__(self):
        return str(self.json())

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "endereco": self.endereco
        }