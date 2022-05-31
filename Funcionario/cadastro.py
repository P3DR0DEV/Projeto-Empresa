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

    add_funcionarios = {}

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
        add_funcionarios = Funcionario.add_funcionarios


        add_funcionarios['Nome'] = str(input('Nome: '))
        add_funcionarios['CPF'] = str(input('CPF: '))
        add_funcionarios['Senha'] = str(input('Crie uma senha: '))
        add_funcionarios['Salario'] = str(input('Salario: '))
        self._nome = add_funcionarios['Nome']  
        self._cpf = add_funcionarios['CPF'] 
        self._salario = add_funcionarios['Salario']
        self._senha = add_funcionarios['Senha']

        return 

    def add_funcionarios_lista():
        del Funcionario.add_funcionarios['Senha']
        show_employes.append(Funcionario.add_funcionarios)

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
        for item in show_employes:
            if login_cpf == item['cpf']:
                print(item)
            



