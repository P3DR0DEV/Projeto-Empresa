from Funcionario.cadastro import Funcionario

Cliente = Funcionario("Pedro", '00000001', 123, 1000)
menu= Funcionario.menu("Login","Criar Conta", 'Sair')
while True:
    
    if menu == 1: #Logar conta
        pass
    elif menu == 2: #Criar conta a ser definido
        pass
    elif menu == 3:
        print('\033[31mFechando Programa.\033[m')
        break