from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")# atribui uma nova funcionalidade na função a baixo
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
