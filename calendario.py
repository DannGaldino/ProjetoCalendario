import this
import conexao
import excluirData

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

this.data = ""
this.turno = ""
this.materia = ""
this.professor = ""
this.horario = ""

def meses():
    this.janeiro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.fevereiro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.marco = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.abril = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.maio = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.junho = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.julho = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.agosto = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.setembro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.outubro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.novembro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    this.dezembro = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

def convertDate(texto):
    separate = texto.split('/')
    day = separate[0]
    month = separate[1]
    year = separate[2]
    return '{}-{}-{}'.format(year, month, day)

def coletarExcluir():
    print("Informe a data da aula que você deseja desmarcar: (xx/xx/xxxx)")
    this.data = input()
    print("Informe oturno da aula que você deseja desmarcar: ")
    print("1. Manhã")
    print("2. Tarde")
    print("3. Noite")
    this.turno = input()
    codigo = (convertDate(this.data) + "(" + this.turno + ")")
    excluirData.excluir(codigo)

def coletar():
    print("Agendar Aula")
    print("Informe a data da aula: (dia/mês/ano)")
    this.data = input()

    print("Informe o turno: ")
    print("1. Manhã")
    print("2. Tarde")
    print("3. Noite")
    this.turno = input()

    print("Informe a matéria: ")
    this.materia = input()

    print("Informe o nome do professor: ")
    this.professor = input()

    codigo = (convertDate(this.data) + "(" + this.turno + ")")

    separado = this.data.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]



    inserir(codigo, dia, mes, ano, this.turno, this.materia, this.professor)


def inserir(codigo, dia, mes, ano, turno, materia, professor):
    try:
        if (codigo != "") and (dia != 0) and (mes != 0) and (ano != 0) and (turno != "") and (materia != "") and (professor != ""):
            sql = "insert into calendario(codigo, dia, mes, ano, turno, materia, professor) values('{}','{}','{}','{}','{}','{}','{}')".format(codigo, dia, mes, ano, turno, materia, professor)
            con.execute(sql)#Prepara o comando para ser executado
            db_connection.commit()  # Executa o comando no banco de dados
            return "Aula agendada!"
    except Exception as erro:
      return(erro)


def consultarTudo():
    try:
        sql = "select * from calendario"
        con.execute(sql)

        this.msg = ""
        for(codigo, dia, mes, ano, turno, materia, professor) in con:
            this.msg += "Data: {}/{}/{}, Turno: {}, Matéria: {}, Professor: {}   |   ".format(dia, mes, ano, turno, materia, professor)
        return this.msg

    except Exception as erro:
        return erro

def consultar(data, turno1):
    try:
        cod = (data + "(" + str(turno1) + ")")

        sql = "select * from calendario where codigo = '{}'".format(cod)
        con.execute(sql)  # Prepara o comando para ser executado

        msg = "Nenhuma aula Agendada!"

        for (codigo, dia, mes, ano , turno, materia, professor) in con:
            if turno == '1':
               this.horario = "Manhã"
            elif turno == '2':
               this.horario = "Tarde"
            elif turno == '3':
                this.horario = "Noite"
            if cod == codigo:
                msg = "Data: " + str(dia) + "/" + str(mes) + "/" + str(ano) + "\nTurno: " + str(this.horario) + "\nMatéria: " + materia  + "\nProfessor: " + professor
        return msg

    except Exception as erro:
        print(str(erro) + "\nPor favor, tente novamente!")
