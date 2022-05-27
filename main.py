from Funcionario.cadastro import Funcionario


while True:
    menu= Funcionario.menu("Login","Criar Conta", 'Sair')
    if menu == 1: #Logar conta
        pass
    elif menu == 2: #Criar conta a ser definido
        Funcionario.cadastra_funcionario(Funcionario)
    elif menu == 3:
        print('\033[31mFechando Programa.\033[m')

    elif menu == 4:
        Funcionario.show_funcionarios()
        break