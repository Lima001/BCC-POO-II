'''
    Exemplo criado para recuperar as informações armazenadas
    no exemplo recuperar_dados.py

    Nesse exemplo, sem conhecer as classes do programa anterior,
    tendo apenas conhecimentos dos dados e do formato que esses estão
    armazenados, vamos recuperar as classes e objetos do programa anterior.

    Esse exemplo mostra como a reflexão poderia ser util para recuperar dados
    de uma fonte externa sem ter que o programador propriamente definir as
    classes usadas para criar os objetos.
'''

from salvar_dados import Classe1, Classe3, lista_salvar, ClasseSalvar

# Contador de objetos recuperados
count_obj = 0

# Vamos percorrer a lista de dados que recuperamos do outro programa
# Onde que cada iteração desse laço principal estaremos trabalhando
# com uma classe específica e os objetos dela que foram armazenados
for i in range(len(lista_salvar)):

    # Recuperação das informações importantes
    nome_classe = lista_salvar[i][0]
    tipos_dados = list(lista_salvar[i][1].values())
    atributos = list(lista_salvar[i][1].keys())
    objetos = lista_salvar[i][2:]

    # String contendo o código do cabeçalho de criação de uma classe em Python
    codigo_classe = f"class {nome_classe}(ClasseSalvar):\n"

    # Criação do método __init__() da classe recuperada da lista
    metodo_init = "\tdef __init__(self"

    # Adição dos atributos na definição do método __init__()
    for chave in atributos:
        metodo_init += f", {chave}"

    # Código de incialização da superclasse
    metodo_init += "):\n\t\tsuper().__init__()\n"

    # Adição das declarações de atributos realizadas no método __init__()
    for chave in atributos:
        metodo_init += f"\t\tself.{chave} = {chave}\n"


    # Caso queira ver a string de código para criação de uma classe, descomente a linha abaixo
    #print(codigo_classe + metodo_init)
    # Execução da string gerada para criação de uma classe recuperada da lista
    exec(codigo_classe + metodo_init)

    # Iteração para pegar as informações de cada objeto da classe que acabou de ser criada.
    # Os dados desses objetos são advindos da lista de dados recuperada do outro programa
    for obj in objetos:

        # Definição de uma string para criação de uma variável que contera
        # um objeto da classe criada anteriormente
        criar_objeto = f"obj{count_obj} = {nome_classe}("
        
        # Dados necessários para recuperar os dados do objeto a ser criado
        tamanho = len(obj.values())
        valores = list(obj.values())[1:]
        
        # Percorrer os dados recuperados da lista sobre aquele objeto a ser criado
        for j in range(tamanho-1):
            # Adicionar os dados dos atributos do objeto, já realizando a sua conversão
            # usando a informação de tipo resgatada também da lista de dados
            criar_objeto += f"tipos_dados[{j}](valores[{j}])"

            if j == tamanho-2:
                criar_objeto += ")"
            else:
                criar_objeto += ", "

        # Descomente a linha abaixo para ver como fica a string de criação de um objeto
        #print(criar_objeto)

        # Somar 1 a quantidade de objetos - Essa informação é relevante, pois
        # cada objeto estará associado a uma variável. Para tornar uma variável
        # única e não ter conflito de nomes, usamos esse valor para componente do
        # seu nome.
        count_obj += 1

        # Execução da string que cria um objeto
        exec(criar_objeto)

# Exibição dos objetos recuperados da lista advinda do outro programa. 
# Dica: Para deixar a exibição melhor, você pode reflexivamente implementar
# o método __str__() para as classes recuperadas e os dados de seus atributos
# armazenados na lista_salvar
print(obj0.atr1, obj0.atr2, obj0.atr3)
print(obj1.atr1, obj1.atr2, obj1.atr3)
print(obj2.atr1, obj2.atr2, obj2.atr3)
print(obj3.atr1, obj3.atr2, obj3.atr3)
print(obj4.atr1, obj4.atr2, obj4.atr3)
print(obj5.atr1, obj5.atr2, obj5.atr3)
print(obj6.atr1)
print(obj7.atr1)

# Criação de um novo objeto sem ter a definição da classe escrita ou importada pelo desenvolvedor no programa
obj8 = Classe3("A")

# Exibição do novo objeto
print(obj8.atr1)