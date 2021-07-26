from config import *

class CupomDesconto(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254))
    descricao = db.Column(db.Text)
    desconto = db.Column(db.Integer)

    def __str__(self):
        return str(self.json())

    def json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "desconto": self.desconto
        }

if __name__ == "__main__":
    
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

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

    print("Listando os Cupons de Desconto Persistidos...\n")
    print(cd1, cd2, cd3, cd4, sep='\n\n')