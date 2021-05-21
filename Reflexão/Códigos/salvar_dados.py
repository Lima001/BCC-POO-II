'''
    Exemplo criado para mostrar como podemos aplicar os conceitos
    de reflexão em um problema real.

    O exemplo hipotético segue: 
    
        Existem diversas classes com diversos objetos criados em seu programa.
        Você deseja salvar todas essas classes em um BD com um simples procedimento,
        sem ter que se preocupar com a quantidade de classes criadas, as estrutura 
        dessas classes e nem com os objetos.

        Por meio de reflexão o seu programa sabe todas as classes criadas por você
        e todos os objetos dessas classes. Tendo acesso a essa informação seu programa
        armazena os dados em um formato que pode ser armazenado  utilizado posteriormente

    O exemplo criado segue:

        Criamos algumas classes e objetos para simular essa ideia de persistir
        dados do sistema. Todavia invés de usar um banco de dados, vamos apenas
        armazenar esses dados em uma lista - Na vida real poderia ser no BD, ou até
        em outros formatos como JSON, mas para simplificar o código o exemplo usa
        elementos nativos Python.
'''

# Classe criada para conseguirmos identificar quais Classes
# do programa devem ter seus objetos armazenados na lista.
# Toda classe que herdar de ClasseSalvar terá seus objetos
# salvos
class ClasseSalvar:

    def __init__(self, classe_salvar: int = True):
        self.classe_salvar = classe_salvar

# Criação das classes que devem ter seus objetos salvos.
# Atente-se na realização de anotação dos tipos dos atributos no método __init__().
# Esses dados serão importantes em um outro exemplo!
class Classe1(ClasseSalvar):

    def __init__(self, atr1: int, atr2: int, atr3: int):
        super().__init__()
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3


class Classe2(ClasseSalvar):

    def __init__(self, atr1: int, atr2: str, atr3: float):
        super().__init__()
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3


class Classe3(ClasseSalvar):

    def __init__(self, atr1: str):
        super().__init__()
        self.atr1 = atr1


#Criação de alguns objetos de cada classe - seguindo os tipos de dados especificados pelas anotações
obj0 = Classe1(1,2,3)
obj1 = Classe1(3,5,7)
obj2 = Classe1(8,10,15)

obj3 = Classe2(1, "Dado1", 7.6)
obj4 = Classe2(2, "Dado2", 8.9)
obj5 = Classe2(3, "Dado3", 5.6)

obj6 = Classe3("I")
obj7 = Classe3("J")

# dados gerais é uma lista de todas os nomes globais criados pelo programa Python
# É nessa lista que encontraremos referências para as classes e objetos que desejamos
dados_gerais = list(globals().values())[:]

# Lista onde iremos salvar os dados dos objetos. Em outros contextos aqui poderia entrar o BD e JSON
# A título de especificação os dados serão armazenados da seguinte forma:
# [
#   [Nome da classe 1, seus atributos e tipos de dados de cada atributo, dados do objeto1 ... dados do objeton]],
#   ...
#   [Nome da classe N, seus atributos e tipos de dados de cada atributo, dados do objeto1 ... dados do objeton]],
# ]
#
lista_salvar = []

# Percorrer os nomes globais em procura das classes e objetos que queremos guardar
for i in dados_gerais:
    
    # Verificamos se o tipo do dado é do mesmo tipo que type, pois assim
    # conseguimos verificar se um dado nessa lista representa uma classe.
    # O tipo de uma classe é o mesmo tipo que type!
    #
    # Além disso fazemos outra verificação, pois podem existir classes que não
    # foram criadas pelo programador e que não devem ter seus objetos armazenados.
    # Sendo assim verificamos se a classe herda de ClasseSalvar (recurso criado especificamente
    # para esse propósito) acessando o metadado __bases__[0].__name__ (Nome da primeira superclasse)
    if type(i) == type(type) and "ClasseSalvar" == i.__bases__[0].__name__:
        # Pegamamos o nome da classe que queremos ter os objetos salvos e a anotação do método __init__()
        nome_classe = i.__name__
        atributos = i.__init__.__annotations__

        # Guardamos os dados anteriores seguindo o padrão especificado anteriormente
        lista_salvar.append([nome_classe, atributos])

    # Caso o dado não seja de uma classe, vamos ver se ele é de um objeto de alguma classe
    # que queremos salvar.
    else:
        # Verificamos se o objeto tem o atributo herdado de ClasseSalvar
        # cujo propósito é justamente identificar quais objetos de quais classes queremos guardar
        if hasattr(i, "classe_salvar"):
            # Pegamos o nome da classe a qual esse objeto é instância
            nome_classe = i.__class__.__name__

            # Procuramos na lista onde estamos salvando os objetos dessa classe
            for j in lista_salvar:
                if j[0] == nome_classe:
                    # Salvamos os atributos do objeto no local adequado seguindo o pdraõ
                    # de representação citado anteriormente
                    j.append(i.__dict__)

# Execução apenas para mostrar os dados que foram "salvos/persistidos" na lista_salvar 
if __name__ == "__main__":
    for i in lista_salvar:
        # Exibir o nome da classe, seus atributos e tipos
        print(i[0], i[1])
        
        # Exibir os objetos salvos dessa classe
        for j in i[2:]:
            print(j)
        
        print()