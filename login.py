from flask import Flask, render_template, request
import this
import calendario
import cadastrarProfessor
import conexao
import menu
this.i = 0

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

this.email = ""
this.senha = ""
this.user = ""

def loginAluno(email, password):
    try:
        sql = "select senha from aluno where email = '{}';".format(email, password)
        con.execute(sql)

        for (senha) in con:
            if this.password == senha[this.i]:
                permissao = True
            else:
                permissao = False
            this.i += 1
        return permissao
    except Exception as erro:
        print
                


def loginProfessor():
    print("Informe o seu email: ")
    this.email = input()
    print("Informe a sua senha: ")
    this.senha = input()

    msg = "Acesso negado! Preencha os campos corretamente."

    try:
        sql = "select senha from Professor where email = '{}';".format(this.email)
        con.execute(sql)#Prepara o comando para ser executado

        for (senha) in con:

            if this.senha == senha[0]:
                print("Acesso Liberado")
                menu.menu2()

    except Exception as erro:
      print(erro)

    print(msg)

def loginAdm():
    print("Informe o usuário: ")
    this.user = input()
    print("Informe a sua senha: ")
    this.senha = input()

    msg = "Acesso negado! Preencha os campos corretamente."

    try:
        sql = "select senha from Administrador where usuario = '{}';".format(this.user)
        con.execute(sql)#Prepara o comando para ser executado

        for (senha) in con:
            se = senha[0]
            if this.senha == se:
                print("Acesso Liberado")
                menu.menu3()

    except Exception as erro:
      print(erro)

    print(msg)
