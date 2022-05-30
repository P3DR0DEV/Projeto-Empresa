from cadastro import Funcionario


def login(admin = False):
    if admin:
        while True:
            opc = Funcionario.menu('Menu de administrador', 'Ver meus dados', 'Dados de um usuário', 'Todos os dados', 'Sair')
            if opc == 1:
                pass
            elif opc == 2:
                pass
            elif opc == 3:
                pass
            elif opc == 4:
                Funcionario.show_funcionarios()
            elif opc == 5:
                break
            




