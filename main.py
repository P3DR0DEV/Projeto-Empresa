from Funcionario import cadastro
import os
from time import sleep
from Funcionario.login import login


Funcionario= cadastro.Funcionario
while True:
    menu= Funcionario.menu("Menu Principal", "Login","Criar Conta", 'Sair')
    if menu == 1: #Logar conta
        login_nome = str(input('Nome: '))
        login_senha = str(input('Senha: '))

        if login_nome == Funcionario.funcionarios['Nome']:
            if Funcionario.funcionarios['Senha'] == login_senha:
                login(True)
            else:
                print('Senha Inválida.')
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
    
    
    elif menu == 2: #Criar conta a ser definido
        Funcionario.cadastra_funcionario(Funcionario)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')  #clear terminal
    elif menu == 3:
        print('\033[31mFechando Programa.\033[m')
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        break

