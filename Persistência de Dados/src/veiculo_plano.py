from config import *

# Importação das classes que compõem a classe VeiculoPlano
from plano import Plano
from veiculo import Veiculo

class VeiculoPlano(db.Model):

    # Atributos que serão mapeados para colunas
    id = db.Column(db.Integer, primary_key=True)
    
    # Chaves estrangeira para criação do relacionamento entre as Tabelas
    id_veiculo = db.Column(db.Integer, db.ForeignKey(Veiculo.id), nullable=False)
    id_plano = db.Column(db.Integer, db.ForeignKey(Plano.id), nullable=False)
    
    # Acesso direto aos dados relacionados com o objeto dessa classe
    veiculo =  db.relationship("Veiculo")
    plano =  db.relationship("Plano")

    # Usado para exibição do objeto
    def __str__(self):
        return str(self.json())

    # Retorna o objeto no formato JSON para facilitar a visualização 
    def json(self):
        return {
            "id": self.id,
            "veiculo": self.veiculo.json(),
            "plano": self.plano.json()
        }

# Teste da Classe
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

    # Instanciamento de veículos por planos - Observe o uso dos objetos criados anteriormente
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

    # Exibição dos objetos criados e agora persistidos
    print("Listando os Veículos por Planos Persistidos...\n")
    print(vp1, vp2, vp3, vp4, vp5, vp5, vp7, vp8, vp9, sep="\n\n")