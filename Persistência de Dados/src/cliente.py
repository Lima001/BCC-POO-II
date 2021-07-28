from config import *

class Cliente(db.Model):

    # Atributos que serão mapeados para colunas
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    endereco = db.Column(db.String(254))

    # Definição dos elementos utilizados para criação da relação de Herança
    type = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'cliente',
        'polymorphic_on': type
    }

    # Usado para exibição do objeto
    def __str__(self):
        return str(self.json())

    # Retorna o objeto no formato JSON para facilitar a visualização 
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "endereco": self.endereco
        }