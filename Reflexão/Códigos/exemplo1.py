'''
    Exemplo criado para demonstrar como podemos rescrever métodos
    implementados pelas metaclasses em Python para alterar o comportamento
    dos nossos objetos

    Além disso, são apresentadas alguns metadados que podemos usar em Python
'''

class Exemplo:

    # Método __init__ é usado para inicializar um objeto. 
    # É invocado após a metaclasse invocar o método __new__()
    def __init__(self, atr1: int, atr2: int):
        self.atr1 = atr1
        self.atr2 = atr2

    # Método chamado quando usamos o operador ==
    def __eq__(self, obj):
        '''
            Usado para verificar se dois objetos da classe Exemplo são iguais.
            Verifica se os respectivos atributos dos objetos são iguais, retornando
            verdadeiro se for o caso, e falso caso contrário.
        '''
        return (self.atr1 == obj.atr1 and self.atr2 == obj.atr2)

    # Método chamado quando queremos representar um objeto em formato de string
    def __str__(self):
        return f"at1: {self.atr1} at2: {self.atr2}"

    # Método invocado quando realizamos uma chamada ao objeto usando nome_objeto()
    def __call__(self):
        return self.atr1 + self.atr2


# Criação de objetos simples para o exemplo
obj1 = Exemplo(1,2)
obj2 = Exemplo(1,4)
obj3 = Exemplo(1,4)

# Uso do metadado __name__ para saber se o pacote que estamos usando é o padrão (chamado __main__)
# Quando importamos uma biblioteca em Python, o seu nome é diferente de __main__, e o código abaixo
# não seria executado. Esse recurso é interessante, pois permite que executemos códigos apenas quando
# queremos testar alguma coisa do próprio módulo
if __name__ == "__main__":
    # Uso dos métodos sobrescritos na classe Exemplo 
    print(obj1 == obj2)
    print(obj2 == obj3)
    print(obj1, obj2, obj3, sep="\n")
    print(obj1(), obj2(), sep="\n")