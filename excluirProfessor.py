import mysql.connector
import conexao
import this

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def excluir(email):
    try:
        sql = "delete from Professor where email = '{}'".format(email)
        con.execute(sql)
        db_connection.commit()
        return "{} Excluido!".format(con.rowcount)
    except Exception as erro:
        return erro