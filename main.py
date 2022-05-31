from Funcionario import cadastro
import os
from time import sleep
from auth.enter_login import login


senha_admin = '123456'

Funcionario= cadastro.Funcionario
while True:
    menu= Funcionario.menu("Menu Principal", "Login","Criar Conta", 'Sair')
    if menu == 1: #Logar conta
        login_cpf = str(input('CPF: '))
        login_senha = str(input('Senha: '))

        if login_cpf == Funcionario.add_funcionario['CPF']:
            if Funcionario.add_funcionario['Senha'] == login_senha:
                admin = str(input('Login como administrador? \n[Y/N] '))
                if admin in 'Yy':
                    senha = str(input('Digite a senha de admin: '))
                    if senha == senha_admin:
                        login(True)
                elif admin in 'Nn':
                    login(False)
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

