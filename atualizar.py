from flask import Flask, render_template, request
import mysql.connector
import this
import conexao
this.msg = ""


db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()


def atualizarDados(email, campo, novoDado):
    try:
        if novoDado != "":
            sql = "update professor set {} = '{}'where email = '{}'".format(campo, novoDado, email)
            con.execute(sql)
            db_connection.commit()
        return "Atualizado"
    except Exception as erro:
        return erro