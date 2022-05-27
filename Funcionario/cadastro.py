from random import randint
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um número válido.')
        else:
            return n



class Funcionario:

    funcionarios = {}

    @staticmethod
    def generate_id():
        pass

    def __init__(self, nome, cpf, senha, salario) -> None:
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
        self._salario = salario
        #self._id 
        


    def cadastra_funcionario(self):
        self._nome = str(input('Nome: '))
        self._cpf = str(input('CPF: '))
        self._senha = str(input('Crie uma senha: '))
        self._salario = str(input('Salario: '))
        Funcionario.funcionarios['Nome'] = self._nome
        Funcionario.funcionarios['CPF'] = self._cpf
        Funcionario.funcionarios['Salario'] = self._salario
        return 



    @staticmethod    
    def menu(*args):
        print('--'*20)
        print('Menu de Principal'.center(40))
        print('--'*20)
        c = 1
        for item in args:
            print(f'{c} - {item}')
            c += 1
        print('--'*20)
        opc = leiaint('Sua Opção: ')
        return opc


    @classmethod
    def show_funcionarios(cls):
        print(cls.funcionarios)

class Administrador(Funcionario):
    def __init__(self) -> None:
        super().__init__()
        pass


