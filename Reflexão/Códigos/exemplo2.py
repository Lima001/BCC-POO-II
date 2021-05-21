'''
    Exemplo criado para demonstrar o acesso a metadados disponibilizados
    pelas classes e objetos em Python
'''

from exemplo1 import *

if __name__ == "__main__":
    # Acesso aos metadados de classes diretamente
    print(Exemplo.__init__.__annotations__)     # Anotações do método __init__()
    print(Exemplo.__eq__.__doc__)               # Documentação do método __eq__()
    print(Exemplo.__bases__)                    # Superclasses de Exemplo
    print()
    print(obj1.__dict__)                        # Dicionário de atributos do objeto obj1
    print(obj2.__dict__)                        # Dicionário de atributos do objeto obj2
    print()
    print(type(obj1), type(obj2), type(obj3), type(Exemplo))    # Tipo dos objetos usando a função type()
    print(id(obj1), id(obj2), id(obj3))                         # id dos objetos usando a função id()