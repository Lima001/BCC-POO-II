from config import *
from cliente import Cliente # Importação da classe Pai

class PessoaJuridica(Cliente):

    id = db.Column(db.Integer, db.ForeignKey("cliente.id"), primary_key=True)

    # Definição da identidade polimórifca para a relação de herança
    __mapper_args__ = {
        'polymorphic_identity': 'pessoa_juridica'
    }

    # Atributos diferenciadores - Extras a classe Pai
    cnpj = db.Column(db.String(20))
    descricao_atuacao = db.Column(db.Text)

    # Usado para exibição do objeto
    def __str__(self):
        return str(self.json())

    # Retorna o objeto no formato JSON para facilitar a visualização 
    def json(self):
        return {
            "id": self.id,
            "cliente": super().json(),
            "cnpj": self.cnpj,
            "descricao_atuacao": self.descricao_atuacao
        }

# Teste da Classe
if __name__ == "__main__":
    
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # Criação do Banco de Dados e de suas estruturas
    db.create_all()

    # Instanciamento de pessoas jurídicas
    pj1 = PessoaJuridica(nome="Indústrias Star", email="Star.Industry@gmail.com", endereco="Rua Supers H 3006", cnpj="11.111.111/0001-11", descricao_atuacao="Empresa do Ramo de Tecnologia focada em construção e aprimoramento de equipamentos para produção e controle de energia renovável e sustentável")
    pj2 = PessoaJuridica(nome="WLLL", email="wll.contato@gmail.com", endereco="Rua ABC 9672", cnpj="22.222.222/0001-22", descricao_atuacao="Empresa especializada em planejamento e gestão de transportes")

    # Adição das pessoas jurídicas para persistência
    db.session.add(pj1)
    db.session.add(pj2)

    # Confirmação da persistência de dados
    db.session.commit()

    # Exibição dos objetos criados e agora persistidos
    print("Listando os Pessoas Jurídicas Persistidos...\n")
    print(pj1, pj2, sep="\n\n")