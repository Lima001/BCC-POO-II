from datetime import date

from config import *
from cliente import Cliente # Importação da classe Pai

class PessoaFisica(Cliente):

    id = db.Column(db.Integer, db.ForeignKey('cliente.id'), primary_key=True)
    
    # Definição da identidade polimórifca para a relação de herança
    __mapper_args__ = {
        'polymorphic_identity': 'pessoa_fisica',
    }

     # Atributos diferenciadores - Extras a classe Pai
    cpf = db.Column(db.String(14))
    data_nascimento = db.Column(db.Date)

    # Usado para exibição do objeto
    def __str__(self):
        return str(self.json())

    # Retorna o objeto no formato JSON para facilitar a visualização 
    def json(self):
        return {
            "id": self.id,
            "cliente": super().json(),
            "cpf": self.cpf,
            "data_nascimento": f"{self.data_nascimento.day}/{self.data_nascimento.month}/{self.data_nascimento.year}"
        }

# Teste da Classe
if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # Criação do Banco de Dados e de suas estruturas
    db.create_all()
    
    # Instanciamento de pessoas físicas
    pf1 = PessoaFisica(nome="Fulano", email="fulano@gmail.com", endereco="Rua XI de Agosto 2106", cpf="111.111.111-11", data_nascimento=date(2002,6,7))
    pf2 = PessoaFisica(nome="Ciclano", email="ciclano@gmail.com", endereco="Rua Consat d'Aulio 93", cpf="222.222.222-22", data_nascimento=date(1999,6,21))
    pf3 = PessoaFisica(nome="Beltrano", email="beltrano@gmail.com", endereco="Rua Dom Telano 5676", cpf="333.333.333-33", data_nascimento=date(1952,1,4))

    # Adição das pessoas físicas para persistência
    db.session.add(pf1)
    db.session.add(pf2)
    db.session.add(pf3)

    # Confirmação da persistência de dados
    db.session.commit()

    # Exibição dos objetos criados e agora persistidos
    print("Listando os Pessoas Físicas Persistidos...\n")
    print(pf1, pf2, pf3, sep="\n\n")