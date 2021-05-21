'''
    Exemplo criado para mostrar que usando metadados é possível
    acrescentar parcialmente um aspecto de tipagem estática em Python.

    Nesse caso os objetos da classe MinhaClasse devem ser criados usando
    a função criar_objeto(), sendo que essa valida os tipos dos dados
    conforme anotações no método __init__ da classe, impedindo que objetos
    sejam criados caso seus tipos estejam em desacordo com o especificado
    pelas anotações do programador.
'''

# Classe exemplo
class MinhaClasse():

    # Observe as anotações sendo usadas para indicar o tipo ideial de cada atributo para inicializar um objeto
    def __init__(self, atr1: int, atr2: str):
        self.atr1 = atr1
        self.atr2 = atr2

    def __str__(self):
        return f"({self.atr1}, {self.atr2})"


def criar_objeto(atr1, atr2):
    '''
        Função que abstrai a criação de objetos, validando o tipo
        dos dados usados para inicializar um objeto em conformidade
        as anotações do programador no método __init__() 
    '''
    # Acesso as anotações de cada parâmetro da função ___init__()
    # Relemebre que __annotations__ retorna um dicionário contendo o nome
    # do parâmetro como chave, e a anotação como valor. Nesse caso devemos
    # usar síntaxe de dicionário para acessar os valores das anotações via chave
    tipo1 = MinhaClasse.__init__.__annotations__["atr1"]
    tipo2 = MinhaClasse.__init__.__annotations__["atr2"]

    # Verificando se o tipo dos dados informados correspodem ao tipo especificado pelo programador
    if (type(atr1) != tipo1 or type(atr2) != tipo2):
        print("Erro - Tipos de dados Incorretos- Impossível criar objeto!")
        return None

    # Caso tudo esteja em conformidade, o objeto é criado e retornado para ser usado
    return MinhaClasse(atr1, atr2)


if __name__ == "__main__":
    # Processo de criação de objetos testes
    obj1 = criar_objeto(1,2)                # Erro -> atr2 deve ser str
    obj2 = criar_objeto("A",2)              # Erro -> atr1 deve ser int 
    obj3 = criar_objeto(1,"Minha string")   # Ok -> tipos de dados informados corretamente

    # Como obj1 e obj2 não foram criados eles serão apresentados como None (devido ao retorno da função)
    # Já obj3 (que foi criado) irá invocar o método __str__() sobrescrito na classe MinhaClasse
    print(obj1, obj2, obj3)