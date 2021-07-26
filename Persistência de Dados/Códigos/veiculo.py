from config import *

class Veiculo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    marca_modelo = db.Column(db.String(254))
    ano = db.Column(db.Integer)
    cor = db.Column(db.String(254))
    kilometragem = db.Column(db.String(254))
    cambio_manual = db.Column(db.Boolean)
    disponivel = db.Column(db.Boolean)

    def __str__(self):
        return str(self.json())

    def json(self):
        return {
            "id": self.id,
            "marca_modelo": self.marca_modelo,
            "ano": self.ano,
            "cor": self.cor,
            "kilometragem": self.kilometragem,
            "cambio_manual": self.cambio_manual,
            "disponivel": self.disponivel
        }

if __name__ == "__main__":
    
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

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

    print("Listando os Veículos Persistidos...\n")
    print(v1, v2, v3, v4, v5, sep='\n\n')