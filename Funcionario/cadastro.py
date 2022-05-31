from time import sleep


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

    add_funcionario = {}

    @staticmethod
    def generate_id():
        pass

    def __init__(self, nome, cpf, senha, salario) -> None:
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
        self._salario = salario
        


    def cadastra_funcionario(self):
        print('--'*20)
        add_funcionario = Funcionario.add_funcionario

        add_funcionario['Nome'] = str(input('Nome: '))
        add_funcionario['CPF'] = str(input('CPF: '))
        add_funcionario['Senha'] = str(input('Crie uma senha: '))
        add_funcionario['Salario'] = str(input('Salario: '))
        self._nome = add_funcionario['Nome']  
        self._cpf = add_funcionario['CPF'] 
        self._salario = add_funcionario['Salario']
        self._senha = add_funcionario['Senha']
        return

    def list_funcionario():
            del Funcionario.add_funcionario['Senha']
            teste = Funcionario.add_funcionario
            show_employes.append(teste)
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
        Funcionario.add_funcionarios_lista()
        print(show_employes)
        
    def usuario_unico():
        Funcionario.add_funcionarios_lista()
        for key in Funcionario.add_funcionarios:
            print(f'{key} : {Funcionario.add_funcionarios[key]}')
        sleep(1)



