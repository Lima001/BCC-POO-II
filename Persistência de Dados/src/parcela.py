from datetime import date

from config import *

# Importação da classe (e suas dependências) que agrega Parcela
from aluguel import Aluguel, PessoaJuridica, PessoaFisica, VeiculoPlano, Plano, Veiculo, CupomDesconto

class Parcela(db.Model):

    # Atributos que serão mapeados para colunas
    id = db.Column(db.Integer, primary_key=True)
    data_registro = db.Column(db.Date)
    data_vencimento = db.Column(db.Date)
    valor_fatura = db.Column(db.Float)
    quitado = db.Column(db.Boolean)

    # Chave estrangeira para criação do relacionamento entre as Tabelas
    aluguel_referente = db.Column(db.Integer, db.ForeignKey(Aluguel.id), nullable=False)
    
    # Acesso direto aos dados relacionados com o objeto dessa classe
    aluguel = db.relationship("Aluguel")

    # Usado para exibição do objeto
    def __str__(self):
        return str(self.json())

    # Retorna o objeto no formato JSON para facilitar a visualização
    def json(self):
        return {
            "id": self.id,
            "data_registro": f"{self.data_registro.day}/{self.data_registro.month}/{self.data_registro.year}",
            "data_vencimento": f"{self.data_vencimento.day}/{self.data_vencimento.month}/{self.data_vencimento.year}",
            "valor_fatura": self.valor_fatura,
            "quitado": self.quitado,
            "aluguel": self.aluguel.json()
        }

# Teste da classe
if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # Criação do Banco de Dados e de suas estruturas
    db.create_all()

    # Instanciamento de planos utilizados para compor VeiculoPlano
    p1 = Plano(nomenclatura="Família I", duracao_maxima=21, limite_kilometragem=10000, preco_diaria=100, qtd_max_parcelas=5)
    p2 = Plano(nomenclatura="Frota Empresarial", duracao_maxima=365, limite_kilometragem=None, preco_diaria=0, qtd_max_parcelas=5)
    p3 = Plano(nomenclatura="Família II", duracao_maxima=21, limite_kilometragem=15000, preco_diaria=200, qtd_max_parcelas=5)
    p4 = Plano(nomenclatura="Luxo", duracao_maxima=7, limite_kilometragem=2000, preco_diaria=350, qtd_max_parcelas=2)
    p5 = Plano(nomenclatura="Trabalho I", duracao_maxima=30, limite_kilometragem=20000, preco_diaria=75, qtd_max_parcelas=10)
    p6 = Plano(nomenclatura="Fideliade I", duracao_maxima=365, limite_kilometragem=None, preco_diaria=30, qtd_max_parcelas=12)
    
    # Adição dos dados para persistência
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.add(p6)

    # Confirmação da persistência
    db.session.commit()

    # Instanciamento de veiculos utilizados para compor VeiculoPlano
    v1 = Veiculo(marca_modelo="Honda Fit LX", ano=2018, cor="Branco", kilometragem=60000, cambio_manual=False, disponivel=True)
    v2 = Veiculo(marca_modelo="BMW 328i", ano=2018, cor="Preto", kilometragem=22000, cambio_manual=False, disponivel=False)
    v3 = Veiculo(marca_modelo="Volkswagen Saveiro Robust", ano=2020, cor="Branco", kilometragem=50000, cambio_manual=True, disponivel=False)
    v4 = Veiculo(marca_modelo="Fiat Argo Drive", ano=2020, cor="Prata", kilometragem=67523, cambio_manual=True, disponivel=False)
    v5 = Veiculo(marca_modelo="Jeep Compass Trailhawk", ano=2021, cor="Preto", kilometragem=25000, cambio_manual=False, disponivel=True)

    # Adição dos dados para persistência
    db.session.add(v1)
    db.session.add(v2)
    db.session.add(v3)
    db.session.add(v4)
    db.session.add(v5)

    # Confirmação da persistência
    db.session.commit()

    # Instanciamento de veículos por planos - Observe o uso dos objetos criados anteriormente - para compor Aluguel
    vp1 = VeiculoPlano(plano=p1, veiculo=v1)
    vp2 = VeiculoPlano(plano=p2, veiculo=v3)
    vp3 = VeiculoPlano(plano=p3, veiculo=v5)
    vp4 = VeiculoPlano(plano=p4, veiculo=v2)
    vp5 = VeiculoPlano(plano=p5, veiculo=v3)
    vp6 = VeiculoPlano(plano=p6, veiculo=v5)
    vp7 = VeiculoPlano(plano=p2, veiculo=v4)
    vp8 = VeiculoPlano(plano=p2, veiculo=v1)
    vp9 = VeiculoPlano(plano=p1, veiculo=v4)
    
    # Adição dos dados para persistência
    db.session.add(vp1)
    db.session.add(vp2)
    db.session.add(vp3)
    db.session.add(vp4)
    db.session.add(vp5)
    db.session.add(vp6)
    db.session.add(vp7)
    db.session.add(vp8)
    db.session.add(vp9)

    # Confirmação da persistência de dados
    db.session.commit()

    # Criação de pessoas físicas para compor o Aluguel
    pf1 = PessoaFisica(nome="Fulano", email="fulano@gmail.com", endereco="Rua XI de Agosto 2106", cpf="111.111.111-11", data_nascimento=date(2002,6,7))
    pf2 = PessoaFisica(nome="Ciclano", email="ciclano@gmail.com", endereco="Rua Consat d'Aulio 93", cpf="222.222.222-22", data_nascimento=date(1999,6,21))
    pf3 = PessoaFisica(nome="Beltrano", email="beltrano@gmail.com", endereco="Rua Dom Telano 5676", cpf="333.333.333-33", data_nascimento=date(1952,1,4))

    # Adição dos dados para persistência
    db.session.add(pf1)
    db.session.add(pf2)
    db.session.add(pf3)

    # Confirmação da persistência de dados
    db.session.commit()

    # Criação de pessoas jurídicas para compor o Aluguel
    pj1 = PessoaJuridica(nome="Indústrias Star", email="Star.Industry@gmail.com", endereco="Rua Supers H 3006", cnpj="11.111.111/0001-11", descricao_atuacao="Empresa do Ramo de Tecnologia focada em construção e aprimoramento de equipamentos para produção e controle de energia renovável e sustentável")
    pj2 = PessoaJuridica(nome="WLLL", email="wll.contato@gmail.com", endereco="Rua ABC 9672", cnpj="22.222.222/0001-22", descricao_atuacao="Empresa especializada em planejamento e gestão de transportes")

    # Adição dos dados para persistência
    db.session.add(pj1)
    db.session.add(pj2)

    # Confirmação da persistência de dados
    db.session.commit()

    # Instanciamento de cupons de desconto
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

    # Adição dos dados para persistência
    db.session.add(cd1)
    db.session.add(cd2)
    db.session.add(cd3)
    db.session.add(cd4)

    # Confirmação da persistência de dados
    db.session.commit()

    # Instanciamento de alugueis - Observe o uso dos objetos criados anteriormente
    al1 = Aluguel(cliente=pf3, veiculo_plano=vp4, cupom_desconto=cd3, data_inicio=date(2021,7,20), data_termino=date(2021,7,25))
    al2 = Aluguel(cliente=pj1, veiculo_plano=vp2, cupom_desconto=cd2, data_inicio=date(2022,1,1), data_termino=date(2022,7,1))
    al3 = Aluguel(cliente=pf2, veiculo_plano=vp6, data_inicio=date(2021,8,10), data_termino=date(2021,8,14))

    # Adição dos dados para persistência
    db.session.add(al1)
    db.session.add(al2)
    db.session.add(al3)

    # Confirmação da persistência de dados
    db.session.commit()

    # Instanciamento de alugueis - Observe o uso dos objetos criados anteriormente. Além disso
    # note o uso de atributos de outros objetos para o cálculo do valor da parcela
    par1 = Parcela(data_registro=date(2021,7,18), data_vencimento=date(2021,8,10), valor_fatura=(5*al1.veiculo_plano.plano.preco_diaria - (5*al1.veiculo_plano.plano.preco_diaria * (al1.cupom_desconto.desconto)/100))/2, quitado=False, aluguel=al1)
    par2 = Parcela(data_registro=date(2021,7,18), data_vencimento=date(2021,9,10), valor_fatura=(5*al1.veiculo_plano.plano.preco_diaria - (5*al1.veiculo_plano.plano.preco_diaria * (al1.cupom_desconto.desconto)/100))/2, quitado=False, aluguel=al1)
    par3 = Parcela(data_registro=date(2021,8,1), data_vencimento=date(2021,9,10), valor_fatura=(4*al2.veiculo_plano.plano.preco_diaria - (4*al2.veiculo_plano.plano.preco_diaria * (al2.cupom_desconto.desconto)/100)), quitado=True, aluguel=al2)
    par4 = Parcela(data_registro=date(2021,10,9), data_vencimento=date(2022,2,1), valor_fatura=(180*al2.veiculo_plano.plano.preco_diaria)/2, quitado=False, aluguel=al3)
    par5 = Parcela(data_registro=date(2021,10,9), data_vencimento=date(2022,6,1), valor_fatura=(180*al2.veiculo_plano.plano.preco_diaria)/2, quitado=False, aluguel=al3)

    # Adição dos dados para persistência
    db.session.add(par1)
    db.session.add(par2)
    db.session.add(par3)
    db.session.add(par4)
    db.session.add(par5)

    # Confirmação da persistência de dados
    db.session.commit()

    # Exibição dos objetos instância de Parcela criados e agora persistidos
    # Observe que trazemos as informações do outros objetos relacioandos a cada parcela.
    # Em um contexto de negócio, talvez trazer toda informação não é necessário, porém
    # como esse é um exemplo utilizando todas as classes do projeto decidiu-se exibir
    # os dados o mais completo possível
    print("Listando as Parcelas Persistidos...\n")
    print(par1, par2, par3, par4, par5, sep="\n\n")