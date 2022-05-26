class Funcionario:
    def __init__(self) -> None:
        pass

    @staticmethod    
    def menu(*args):
        print('--'*20)
        print('Menu de Principal'.center(40))
        print('--'*20)
        c = 1
        for item in args:
            print(f'{c} - {item}')
            c + 1


class Administrador(Funcionario):
    def __init__(self) -> None:
        super().__init__()
        pass


