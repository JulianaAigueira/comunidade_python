from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SECRET_KEY'] = '78be893bf8a80da4ad549bae099aee49'

#--------------------------------------------------------------
#               CRIANDO O BANCO DE DADOS
#--------------------------------------------------------------

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
#--------------------------------------------------------------
#para rodar os link e tem que ser no final pq os routes precisando do app criados
from comunidadepython import routes


