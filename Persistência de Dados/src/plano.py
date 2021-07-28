from config import *

class Plano(db.Model):

    # Atributos que serão mapeados para colunas
    id = db.Column(db.Integer, primary_key=True)
    nomenclatura = db.Column(db.String(254))
    duracao_maxima = db.Column(db.Integer)  # Em dias
    duracao_minima = db.Column(db.Integer)  # Em dias
    limite_kilometragem = db.Column(db.Integer)
    preco_diaria = db.Column(db.Float)
    qtd_max_parcelas = db.Column(db.Integer)

    # Usado para exibição do objeto
    def __str__(self):
        return str(self.json())

    # Retorna o objeto no formato JSON para facilitar a visualização 
    def json(self):
        return {
            "id": self.id,
            "nomenclatura": self.nomenclatura,
            "duracao_maxima": self.duracao_maxima,
            "duracao_minima": self.duracao_minima,
            "preco_diaria": self.preco_diaria,
            "qtd_max_parcelas": self.qtd_max_parcelas
        }

# Teste da Classe
if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # Criação do Banco de Dados e de suas estruturas
    db.create_all()

    # Instanciamento de Planos
    p1 = Plano(nomenclatura="Família I", duracao_maxima=21, limite_kilometragem=10000, preco_diaria=100, qtd_max_parcelas=5)
    p2 = Plano(nomenclatura="Frota Empresarial", duracao_maxima=365, limite_kilometragem=None, preco_diaria=0, qtd_max_parcelas=5)
    p3 = Plano(nomenclatura="Família II", duracao_maxima=21, limite_kilometragem=15000, preco_diaria=200, qtd_max_parcelas=5)
    p4 = Plano(nomenclatura="Luxo", duracao_maxima=7, limite_kilometragem=2000, preco_diaria=350, qtd_max_parcelas=2)
    p5 = Plano(nomenclatura="Trabalho I", duracao_maxima=30, limite_kilometragem=20000, preco_diaria=75, qtd_max_parcelas=10)
    p6 = Plano(nomenclatura="Fideliade I", duracao_maxima=365, limite_kilometragem=None, preco_diaria=30, qtd_max_parcelas=12)

    # Adição dos Planos para persistência
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.add(p6)

    # Confirmação da persistência de dados
    db.session.commit()

    # Exibição dos objetos criados e agora persistidos
    print("Listando os Planos Persistidos...\n")
    print(p1, p2, p3, p4, p5, p6, sep='\n\n')