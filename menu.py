import atualizarSenha
import atuzalizarNome
import cadastrarProfessor
import consultarProfessor
import excluirData
import login
import this
import calendario

this.opcao = -2
this.codigo = 0


def mostrarMenu1():
    print('Escolha uma das opçôes abaixo: ' +
          '\n\n\n1. Calendário' +
          '\n2. Login Professor' +
          '\n3. Login Administrador' +
          '\n4. Sair')

    this.opcao = int(input())

def menu1():
    while this.opcao != 4:
        mostrarMenu1()
        if this.opcao == 1:
            calendario.consultar()
        elif this.opcao == 2:
            login.loginProfessor()
        elif this.opcao == 3:
            login.loginAdm()
        elif this.opcao == 4:
            print("Obrigado!")
        else:
            print('Opção inválida! Tente novamente')

def mostrarMenu2():
    print('Escolha uma das opçôes abaixo: ' +
          '\n\n\n1. Agendar Aulas' +
          '\n2. Desmarcar Aula' +
          '\n3. Atualizar Nome' +
          '\n4. Atualizar Senha' +
          '\n5. Sair')

    this.opcao = int(input())


def menu2():
    while this.opcao != 5:
        mostrarMenu2()
        if this.opcao == 1:
            calendario.coletar()
        elif this.opcao == 2:
            calendario.coletarExcluir()
        elif this.opcao == 3:
            atuzalizarNome.novoNome(this.email, this.nome)
        elif this.opcao == 4:
            atualizarSenha.atualizarSenha(this.email, this.senha)
        elif this.opcao == 5:
            print("Obrigado")
        else:
            print('Opção inválida! Tente novamente')

def mostrarMenu3():
    print('Escolha uma das opçôes abaixo: ' +
          '\n\n\n1. Cadastrar Professor' +
          '\n2. Atualizar Nome(Professor)' +
          '\n3. Atualizar Senha(Professor)' +
          '\n4. Sair')

    this.opcao = int(input())


def menu3():
    while this.opcao != 4:
        mostrarMenu3()
        if this.opcao == 1:
            cadastrarProfessor.coletarDados()
        elif this.opcao == 2:
            atuzalizarNome.novoNome(this.email, this.nome)
        elif this.opcao == 3:
            atualizarSenha.atualizarSenha(this.email, this.senha)
        elif this.opcao == 4:
            print("Obrigado!")
        else:
            print('Opção inválida! Tente novamente')

