from datetime import date

from config import *
from cliente import Cliente
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica
from veiculo_plano import VeiculoPlano, Plano, Veiculo
from cupom_desconto import CupomDesconto

class Aluguel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    
    id_cliente = db.Column(db.Integer, db.ForeignKey(Cliente.id), nullable=False)
    id_veiculo_plano = db.Column(db.Integer, db.ForeignKey(VeiculoPlano.id), nullable=False)
    id_cupom_desconto = db.Column(db.Integer, db.ForeignKey(CupomDesconto.id))

    cliente = db.relationship('Cliente')
    veiculo_plano = db.relationship('VeiculoPlano')
    cupom_desconto = db.relationship('CupomDesconto')
    
    data_inicio = db.Column(db.Date)
    data_termino = db.Column(db.Date)

    def __str__(self):
        return str(self.json())

    def json(self):
        r = {
            "id": self.id,
            "cliente": self.cliente.json(),
            "veiculo_plano": self.veiculo_plano.json(),
            "data_inicio": f"{self.data_inicio.day}/{self.data_inicio.month}/{self.data_inicio.year}",
            "data_termino": f"{self.data_termino.day}/{self.data_termino.month}/{self.data_termino.year}"
        }

        if self.cupom_desconto:
            r["cupom_desconto"] = self.cupom_desconto.json()

        return r
        

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    p1 = Plano(nomenclatura="Família I", duracao_maxima=21, limite_kilometragem=10000, preco_diaria=100, qtd_max_parcelas=5)
    p2 = Plano(nomenclatura="Frota Empresarial", duracao_maxima=365, limite_kilometragem=None, preco_diaria=0, qtd_max_parcelas=5)
    p3 = Plano(nomenclatura="Família II", duracao_maxima=21, limite_kilometragem=15000, preco_diaria=200, qtd_max_parcelas=5)
    p4 = Plano(nomenclatura="Luxo", duracao_maxima=7, limite_kilometragem=2000, preco_diaria=350, qtd_max_parcelas=2)
    p5 = Plano(nomenclatura="Trabalho I", duracao_maxima=30, limite_kilometragem=20000, preco_diaria=75, qtd_max_parcelas=10)
    p6 = Plano(nomenclatura="Fideliade I", duracao_maxima=365, limite_kilometragem=None, preco_diaria=30, qtd_max_parcelas=12)
    
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.add(p6)

    db.session.commit()

    v1 = Veiculo(marca_modelo="Honda Fit LX", ano=2018, cor="Branco", kilometragem=60000, cambio_manual=False, disponivel=True)
    v2 = Veiculo(marca_modelo="BMW 328i", ano=2018, cor="Preto", kilometragem=22000, cambio_manual=False, disponivel=False)
    v3 = Veiculo(marca_modelo="Volkswagen Saveiro Robust", ano=2020, cor="Branco", kilometragem=50000, cambio_manual=True, disponivel=False)
    v4 = Veiculo(marca_modelo="Fiat Argo Drive", ano=2020, cor="Prata", kilometragem=67523, cambio_manual=True, disponivel=False)
    v5 = Veiculo(marca_modelo="Jeep Compass Trailhawk", ano=2021, cor="Preto", kilometragem=25000, cambio_manual=False, disponivel=True)

    db.session.add(v1)
    db.session.add(v2)
    db.session.add(v3)
    db.session.add(v4)
    db.session.add(v5)

    db.session.commit()

    vp1 = VeiculoPlano(plano=p1, veiculo=v1)
    vp2 = VeiculoPlano(plano=p2, veiculo=v3)
    vp3 = VeiculoPlano(plano=p3, veiculo=v5)
    vp4 = VeiculoPlano(plano=p4, veiculo=v2)
    vp5 = VeiculoPlano(plano=p5, veiculo=v3)
    vp6 = VeiculoPlano(plano=p6, veiculo=v5)
    vp7 = VeiculoPlano(plano=p2, veiculo=v4)
    vp8 = VeiculoPlano(plano=p2, veiculo=v1)
    vp9 = VeiculoPlano(plano=p1, veiculo=v4)
    
    db.session.add(vp1)
    db.session.add(vp2)
    db.session.add(vp3)
    db.session.add(vp4)
    db.session.add(vp5)
    db.session.add(vp6)
    db.session.add(vp7)
    db.session.add(vp8)
    db.session.add(vp9)

    db.session.commit()

    pf1 = PessoaFisica(nome="Fulano", email="fulano@gmail.com", endereco="Rua XI de Agosto 2106", cpf="111.111.111-11", data_nascimento=date(2002,6,7))
    pf2 = PessoaFisica(nome="Ciclano", email="ciclano@gmail.com", endereco="Rua Consat d'Aulio 93", cpf="222.222.222-22", data_nascimento=date(1999,6,21))
    pf3 = PessoaFisica(nome="Beltrano", email="beltrano@gmail.com", endereco="Rua Dom Telano 5676", cpf="333.333.333-33", data_nascimento=date(1952,1,4))

    db.session.add(pf1)
    db.session.add(pf2)
    db.session.add(pf3)

    db.session.commit()

    pj1 = PessoaJuridica(nome="Indústrias Star", email="Star.Industry@gmail.com", endereco="Rua Supers H 3006", cnpj="11.111.111/0001-11", descricao_atuacao="Empresa do Ramo de Tecnologia focada em construção e aprimoramento de equipamentos para produção e controle de energia renovável e sustentável")
    pj2 = PessoaJuridica(nome="WLLL", email="wll.contato@gmail.com", endereco="Rua ABC 9672", cnpj="22.222.222/0001-22", descricao_atuacao="Empresa especializada em planejamento e gestão de transportes")

    db.session.add(pj1)
    db.session.add(pj2)

    db.session.commit()

    cd1 = CupomDesconto(titulo="Cliente Bis", 
                        descricao="Voltado para clientes que contratarem nossos serviços pela segunda vez", 
                        desconto=12)

    cd2 = CupomDesconto(titulo="Empresa Sustentável", 
                        descricao="Voltado para empresas que comprovem preocupação com aspectos ambientais e sustentáveis", 
                        desconto=30)

    cd3 = CupomDesconto(titulo="Na melhor Idade", 
                        descricao="Voltado para clientes com idade superior a 60 e que estão contratando o serviço." +\
                                    "Pode ser usado apenas uma vez por cliente",
                        desconto=15)

    cd4 = CupomDesconto(titulo="Cliente da Casa",
                        descricao="Voltado para clientes que tiverem ao menos 3 registros no Plano de Fidelidade." +\
                                    "Pode ser usado apenas uma vez por cliente. Deve ser aplicado em planos com duração máxima de 30 dias",
                        desconto=70)

    db.session.add(cd1)
    db.session.add(cd2)
    db.session.add(cd3)
    db.session.add(cd4)

    db.session.commit()

    al1 = Aluguel(cliente=pf3, veiculo_plano=vp4, cupom_desconto=cd3, data_inicio=date(2021,7,20), data_termino=date(2021,7,25))
    al2 = Aluguel(cliente=pj1, veiculo_plano=vp2, cupom_desconto=cd2, data_inicio=date(2022,1,1), data_termino=date(2022,7,1))
    al3 = Aluguel(cliente=pf2, veiculo_plano=vp6, data_inicio=date(2021,8,10), data_termino=date(2021,8,14))

    db.session.add(al1)
    db.session.add(al2)
    db.session.add(al3)

    db.session.commit()

    print("Listando os Alugueis Persistidos...\n")
    print(al1, al2, al3, sep="\n\n")