def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um número válido.')
        else:
            return n


show_employes = []
class Funcionario: 
    global show_employes

    funcionarios = {}

    @staticmethod
    def generate_id():
        pass

    def __init__(self, nome, cpf, senha, salario) -> None:
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
        self._salario = salario
        #self._id = generate_id()
        


    def cadastra_funcionario(self):
        print('--'*20)
        funcionarios = Funcionario.funcionarios


        funcionarios['Nome'] = str(input('Nome: '))
        funcionarios['CPF'] = str(input('CPF: '))
        funcionarios['Senha'] = str(input('Crie uma senha: '))
        funcionarios['Salario'] = str(input('Salario: '))
        self._nome = funcionarios['Nome']  
        self._cpf = funcionarios['CPF'] 
        self._salario = funcionarios['Salario']
        self._senha = funcionarios['Senha']

        values = funcionarios['Nome'], funcionarios['CPF'], funcionarios['Salario']
        show_employes.append(values)
        return 



    @staticmethod    
    def menu(nome , *args):
        print('--'*20)
        print(nome.center(40))
        print('--'*20)
        c = 1
        for item in args:
            print(f'{c} - {item}')
            c += 1
        print('--'*20)
        opc = leiaint('Sua Opção: ')
        return opc


    @staticmethod
    def show_funcionarios():
        print(show_employes)



