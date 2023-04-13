from flask import Flask, render_template, url_for
from forms import FormLogin, FormcriarConta

app = Flask(__name__)

lista_usuarios = ['Lira', 'João', 'Maria', 'Juliana', 'Lucas', 'Julia']

app.config['SECRET_KEY'] = '78be893bf8a80da4ad549bae099aee49'

@app.route("/")# atribui uma nova funcionalidade na função a baixo
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login')
def login():
    form_login = FormLogin()
    form_criarconta = FormcriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)
