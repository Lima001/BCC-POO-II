# Importação dos frameworks reponsáveis pela persistência
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Importação
import os

app = Flask(__name__)

# Definição do endereço do arquivo do banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'testes.db')

# Configuração básica para a criação do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Objeto reponsável por permitir, manipular e gerenciar a persistência de dados
db = SQLAlchemy(app)