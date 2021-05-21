'''
    Exemplo criado para demonstrar como podemos alterar o código em tempo
    de execução do programa, criando novas variáveis usando um nome informado
    pelo próprio usuário.

    Além disso, nesse código modificamos a estrutura de objetos através da manipulação
    de metadados que controlam seus atributos. Nesse caso estamos acrescentando
    atributos que antes não eram definidos pela sua classe. Como medida de segurança,
    a classe original não é alterada pelo Python, mas o objeto contará com o novo atributo
    em sua estrutura.
'''

from exemplo1 import *

if __name__ == "__main__":
    # Solicitar o nome para uma variável
    nome_novo_atributo = input("Digite um nome para um novo atributo do obj1: ")
    
    # Uma string contendo uma expressão matemática
    valor = "(2+2) * 5"
    
    # Avaliamos a expressão numérica, fazendo com que valor seja 20
    valor = eval(valor)
    
    # Criamos um atributo para o obj1 com o nome de variável informado pelo usuário,
    # e com o valor referente a avaliação da expressão valor vista anteriormente
    exec(f"obj1.{nome_novo_atributo} = {valor}")
    
    # Modificamos diretamente um metadado do objeto responsável pelo controle dos 
    # atributos e de seus valores. Nesse caso estamos acrescentando um atributo atr0
    # cujo valor será 11
    obj1.__dict__["atr0"] = 11

    # Imprimindo os atributos do objeto usando metadados
    print(obj1.__dict__)

    # Imprimindo o atributo adicionando via manipulação de metadados
    # Nesse caso podemos observar que existe causalidade entre os aspectos
    # reflexivos e não reflexivos da linguagem
    print(obj1.atr0)