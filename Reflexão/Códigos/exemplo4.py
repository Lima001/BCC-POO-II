'''
    Exemplo criado para demonstrar como é possível criar classes na linguagem
    Python usando uma síntaxe utilizada pela própria estrutura da linguagem
'''

if __name__ == "__main__":
    # Criação de uma classe chamada NomeClasse, que herda de object e possui
    # o atributo atr1 definido como 10, e o método func() retornando 10.
    
    # Observe que usamos type() para criar essa classe. 
    # Isso ocorre, pois as classes em python devem herdar da metaclasse type.
    # Essa é a síntaxe usada internamente pela linguagem quando criamos uma classe
    # da maneira usual. Todavia observe que esse exemplo é bem simplificado para
    # um fácil entendimento
    classe1 = type("NomeClasse", (object,), {"atr1": 10, "func": lambda f: 10})
    
    # Criação de um objeto da classe NomeClasse, cuja referência pode ser acessada via variável classe1
    obj1 = classe1()
    
    # Exibição de atributos, invocação de métodos e acesso a metadados
    print(obj1.atr1)
    print(obj1.func())
    print(obj1.__class__.__name__)
    print(type(obj1))