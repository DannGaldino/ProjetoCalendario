from __future__ import annotations
from urllib.request import Request
from flask import Flask, render_template, request
import this
import login
import conexao
import menu
import calendario
import cadastrarProfessor
import atualizar
import excluirProfessor
this.msg = ""
this.dados = ""
codigo = ""
dia = 0
mes = 0
ano = 0

siteFlask = Flask(__name__) #Representando uma variável do tipo flask

@siteFlask.route('/', methods=['GET','POST'])
def menu():
    return render_template('index.html', titulo='Página Principal')

@siteFlask.route('/loginAluno.html', methods=['GET','POST'])
def loginAluno():
        if request.method == 'POST':
            this.user = request.form['user']
            this.password = request.form['password']
            this.dados = login.loginAluno(this.email, this.password)
        return render_template('loginAluno.html', titulo='Página Principal', resultado=this.dados)

@siteFlask.route('/calendario.html', methods=['GET','POST'])
def calendar():        
        if request.method == 'POST':
            this.data = request.form['data']
            this.turno1 = request.form['turno']
            this.msg = calendario.consultar(this.data, this.turno1)
        return render_template('calendario.html', titulo='Calendário de Aulas', resultado=this.msg)

@siteFlask.route('/cadastrar.html', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        this.email = request.form['tNovoEmail']
        this.senha = request.form['tNovaSenha']
        this.nome = request.form['tNovoNome']
        this.dados = cadastrarProfessor.inserir(this.email, this.senha, this.nome)
    return render_template('/cadastrar.html', titulo='Cadastrar', logar=this.dados)

@siteFlask.route('/atualizar.html', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        this.email = request.form['tEmail']
        this.campo = request.form['tCampo']
        this.nDado = request.form['tDado']
        this.dados = atualizar.atualizarDados(this.email, this.campo, this.nDado)
    return render_template('atualizar.html', titulo='Atualizar', resultado=this.dados)


@siteFlask.route('/excluir.html', methods=['GET', 'POST'])
def excluirDados():
    if request.method == 'POST':
        this.email = request.form['tEmail']
        this.dados = excluirProfessor.excluir(this.email)
    return render_template('excluir.html', titulo='Excluir', resultado=this.dados)

@siteFlask.route('/agendar.html', methods=['GET','POST'])
def agenda():
    dia = 0
    mes = 0
    ano = 0
    if request.method == 'POST':
        codigo = ""
        this.data = request.form['data']
        this.turno = request.form['turno']
        this.professor = request.form['prof']
        this.materia = request.form['materia']
        if this.data != "":
            codigo = this.data + "(" + this.turno + ")"
            separado = this.data.split('-')
            ano = separado[0]
            mes = separado[1]
            dia = separado[2]
        this.dados = calendario.inserir(codigo, dia, mes, ano, this.turno, this.materia, this.professor)
    return render_template('agendar.html', titulo='Agendar Aula', resultado=this.dados)


if __name__ == '__main__':
    siteFlask.run(debug=True, port=5000)

