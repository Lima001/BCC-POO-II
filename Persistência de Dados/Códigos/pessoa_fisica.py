from config import *
from cliente import Cliente
from datetime import date

class PessoaFisica(Cliente):

    id = db.Column(db.Integer, db.ForeignKey('cliente.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'pessoa_fisica',
    }

    cpf = db.Column(db.String(14))
    data_nascimento = db.Column(db.Date)

    def __str__(self):
        return str(self.json())

    def json(self):
        return {
            "id": self.id,
            "cliente": super().json(),
            "cpf": self.cpf,
            "data_nascimento": self.data_nascimento
        }

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()
    
    pf1 = PessoaFisica(nome="Fulano", email="fulano@gmail.com", endereco="Rua XI de Agosto 2106", cpf="111.111.111-11", data_nascimento=date(2002,6,7))
    pf2 = PessoaFisica(nome="Ciclano", email="ciclano@gmail.com", endereco="Rua Consat d'Aulio 93", cpf="222.222.222-22", data_nascimento=date(1999,6,21))
    pf3 = PessoaFisica(nome="Beltrano", email="beltrano@gmail.com", endereco="Rua Dom Telano 5676", cpf="333.333.333-33", data_nascimento=date(1952,1,4))

    db.session.add(pf1)
    db.session.add(pf2)
    db.session.add(pf3)

    db.session.commit()

    print("Listando os Pessoas Físicas Persistidos...\n")
    print(pf1, pf2, pf3, sep="\n\n")