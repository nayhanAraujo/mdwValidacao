from flask import Flask, render_template, request
from validators import html_validator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validar', methods=['POST'])
def validar():
    tipo = request.form['tipo']
    arquivo = request.files['arquivo']
    conteudo = arquivo.read().decode('utf-8')

    erros = []
    if tipo == 'html':
        erros = html_validator.validar_html(conteudo)

    return render_template('resultado_validacao.html', erros=erros, tipo=tipo, nome=arquivo.filename)

if __name__ == '__main__':
    app.run(debug=True)
