from config import *
from cliente import Cliente

class PessoaJuridica(Cliente):

    id = db.Column(db.Integer, db.ForeignKey("cliente.id"), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'pessoa_juridica'
    }

    cnpj = db.Column(db.String(20))
    descricao_atuacao = db.Column(db.Text)

    def __str__(self):
        return str(self.json())

    def json(self):
        return {
            "id": self.id,
            "cliente": super().json(),
            "cnpj": self.cnpj,
            "descricao_atuacao": self.descricao_atuacao
        }

if __name__ == "__main__":
    
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    pj1 = PessoaJuridica(nome="Indústrias Star", email="Star.Industry@gmail.com", endereco="Rua Supers H 3006", cnpj="11.111.111/0001-11", descricao_atuacao="Empresa do Ramo de Tecnologia focada em construção e aprimoramento de equipamentos para produção e controle de energia renovável e sustentável")
    pj2 = PessoaJuridica(nome="WLLL", email="wll.contato@gmail.com", endereco="Rua ABC 9672", cnpj="22.222.222/0001-22", descricao_atuacao="Empresa especializada em planejamento e gestão de transportes")

    db.session.add(pj1)
    db.session.add(pj2)

    db.session.commit()

    print("Listando os Pessoas Jurídicas Persistidos...\n")
    print(pj1, pj2, sep="\n\n")