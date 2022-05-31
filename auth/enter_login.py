from Funcionario import cadastro
from time import sleep


Funcionario = cadastro.Funcionario


def login(admin = False):
    if admin:
        while True:
            opc = Funcionario.menu('Menu de administrador', 'Ver meus dados', 'Dados de um usuário', 'Todos os dados', 'Sair')
            if opc == 1:
                Funcionario.usuario_unico()
            elif opc == 2:
                pass
            elif opc == 3:
                Funcionario.show_funcionarios()
                sleep(2)
            elif opc == 4:
                print('\033[31mVocê escolheu sair.\033[m')
                break
    else:
        while True:
            escolha = Funcionario.menu('Menu de Funcionario', 'Ver meus dados', 'Sair')
            if escolha == 1:
                pass # mostrar dados
            elif escolha == 2:
                print('\033[31mVocê escolheu sair.\033[m')
                break        

