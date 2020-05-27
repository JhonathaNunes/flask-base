# controllers.py

from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Presenca


@app.route('/')
def index():
    presencas = Presenca.recupera_todos()

    menu = []

    menu.append({'active': True,
                 'href': '/',
                 'texto': 'Presenças'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Cadastrar presença'})
    menu.append({'active': False,
                 'href': '/jhonatha',
                 'texto': 'Jhonatha'})

    context = {'titulo': 'Presenças',
               'menu': menu,
               'presencas': presencas,
               'presencas_num': len(presencas)}

    return render_template('index.html', **context)


@app.route("/presenca")
def presenca():
    menu = []

    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Presenças'})
    menu.append({'active': True,
                 'href': '/presenca',
                 'texto': 'Cadastrar preseça'})
    menu.append({'active': False,
                 'href': '/jhonatha',
                 'texto': 'Jhonatha'})

    context = {'titulo': 'Cadastrar preseça',
               'menu': menu}

    return render_template('presenca.html', **context)


@app.route('/presenca/gravar', methods=['POST'])
def gravar_presenca():
    email = request.form['email']
    presenca = request.form['presenca']
    resposta = request.form['resposta']
    comentarios = request.form['comentarios']

    presenca = Presenca(email, presenca, resposta, comentarios)
    presenca.gravar()
    return redirect('/')


@app.route('/jhonatha')
def jhonatha():
    menu = []

    menu.append({'active': False,
                 'href': '/',
                 'texto': 'Presenças'})
    menu.append({'active': False,
                 'href': '/presenca',
                 'texto': 'Cadastrar preseça'})
    menu.append({'active': True,
                 'href': '/jhonatha',
                 'texto': 'Sobre - Jhonatha'})

    context = {'titulo': 'Sobre - Jhonatha',
               'menu': menu}

    return render_template('jhonatha.html', **context)


app.run()
