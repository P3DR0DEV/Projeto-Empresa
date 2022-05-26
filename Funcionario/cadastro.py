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
        Funcionario.funcionarios['Nome'] = self._nome
        Funcionario.funcionarios['CPF'] = self._cpf
        Funcionario.funcionarios['Salario'] = self._salario
        

    def show_funcionarios(cls):
        return cls.funcionarios


    def set_cpf(self, cpf=''):
        if cpf.isnumeric():
            return self._cpf 
        else:
            print('Digite um Número de cpf válido.')


    def cadastrar_funcionario():
        pass


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

class Administrador(Funcionario):
    def __init__(self) -> None:
        super().__init__()
        pass


