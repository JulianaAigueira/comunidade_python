from flask import Flask, render_template, url_for, request, flash, redirect
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormcriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success') #exibir msg de login bem sucedido
        return redirect(url_for('home')) #fez login com sucesso
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success') #criou conta com sucesso
        return redirect(url_for('home'))  # fez login com sucesso
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)
