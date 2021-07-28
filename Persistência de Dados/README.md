# AV3 - Persistência de Dados

O diretório atual conta com os elementos desenvolvidos para apresentação na disciplina de Programação Orientada a Objetos II para a avaliação de número três com o enfoque em persistência de dados

## Especificação do Trabalho

Terceira avaliação (AV3) - código com 5 classes (definição e testes), herança, agregação/composição, diagrama UML de classes, reusabilidade, bibliotecas e persistência de dados. Todas as 5 classes devem estar relacionadas.

## Ideia Geral e o Desenvolvimento do Trabalho

O intuito geral do trabalho era permitir que o aluno apresentasse o seu conhecimento no tópico de persistência de dados, bem como outros aspectos já estudados anteriormente em aula.

Uma vez observado isso, pretendia inicialmente desenvolver um conjunto de classes relacionadas com grande potencial de reúso de software, e que tivessem como característica principal a implementação dos mecanismos básicos de persistência de dados via ORM.

Todavia, encontrei certa dificuldade em modelar uma biblioteca com tais características. Julgo que o principal motivo está relacionado com o aspecto do domínio em que as classes podem ser reutilizadas. 

Ao tratar de persistência de dados, é possível notar um grande vínculo com o elemento domínio, uma vez que a organização de dados e a sua persistência muitas vezes dependem do contexto em que estão inseridos. Por exemplo, construir bibliotecas reutilizáveis com elementos matemáticos é muito mais fácil que construir uma biblioteca para persistir dados relacionados a um contexto específico.

Tendo percebido tal fato, optou-se para o desenvolvimento de um conjunto de classes que, mesmo não sendo possível (ou apenas uma tarefa mais árdua) de implementar todo o conjunto reutilizável, ainda possibilitaria que certos elementos atendessem aos requisitos de reusabilidade da avaliação.

Para o desenvolvimento das classes escolheu-se focar no contexto de registro de aluguel de carros genérico, onde os clientes (que podem ser tanto pessoa física quanto jurídica) escolhem planos de aluguel e algum veículo disponível naquele plano para realizar a locação. Ainda tentou-se agregar elementos extras para encorporar a biblioteca de classes, sendo exemplos a adição de cupons de desconto e parcelamento do aluguel.

Como é possível observar no diagrama de classes do projeto, tem-se ao total cerca de 9 classes para a modelagem desse cenário. Cada classes é utilizada para persistir os dados em um banco de dados sqllite através da linguagem Python e do framework SQLAlchemy (Mais detalhes na seção de Como Executar). A título de especificação, logo abaixo é possível observar uma pequena explicação do propósito de cada classe conforme elas foram pensadas e modeladas.

- __Cliente:__ Classe utilizada para representar e persistir os dados básicos de um cliente que deseja alugar um veículo;

- __PessoaFísica e PessoaJurídica:__ No contexto de aluguel de veículos, é comum possuirmos tanto pessoas físicas quanto jurídicas como clientes. Sendo assim foi decidido trazer esse aspecto para o modelo implementado;

- __Veiculo:__ Classe utilizada para representar e persistir os dados básicos de um veículo que pode ser alugado;

- __Plano:__ Classe utilizada para representar as limitações e características básicas de um aluguel;

- __VeiculoPlano:__ Classe utilizada para relacionar as classes Veiculo e Plano. Foi criada objetivando especificar quais veiculos podem ser alugados em quais planos. Como exemplo em um contexto real, uma empresa que deseja alugar carros para sua frota não poderá escolher entre todos os tipos de veículos, mas sim aqueles que a locadora especificou para esse propósito;

- __CupomDesconto:__ Essa classe foi modelada buscando adicionar um elemento extra ao contexto de aluguel de veículos. Considera-se que a empresa que utiliza esse modelo permite o cadastro e uso de cupões para seus clientes terem vantagens nos alugueis realizados;

- __Aluguel:__ Classe principal do sistema modelado, uma vez que unifica todos os elementos discutidos anteriormente e representa os aspecto principal do contexto trabalhado nessa avaliação;

- __Parcela:__ Utilizado para representar o aspecto financeiro de um aluguel, onde cada locação pode ser parcelada;

## Atendimento dos Requisitos

Em seguida estão elencados como cada requisito da avaliação foi atendido pela modelagem criada e comentada anteriormente.

- __Código com 5 classes (definição e teste):__ Foram criadas 9 classes, cada uma sendo definida individualmente em seu próprio arquivo. Os testes foram realizados de maneira simples no mesmo arquivo de definição, onde são instanciados alguns objetos para que possam ser persistidos no Banco de Dados;
      
- __Herança:__ Esse requisito foi implementado nas classes Cliente, PessoaFisica e PessoaJuridica. Toda PF e PJ podem ser clientes de uma locação de veículo, todavia cada um traz consigo informações próprias adicionais às contidas em um cliente;
      
- __Agregação:__ Implementado na relação entre CupomDesconto e Aluguel, visto que cada aluguel pode ou não possuir um cupom de desconto, CupomDesconto agrega informações a classe Aluguel;
      
- __Composição:__ Esse requisito é mais fácil de observar no diagrama de classes do projeto, uma vez que tirando as relações entre CupomDesconto/Aluguel e a relação de herança da classe Cliente, todas as relações são de composição. Isso ocorre, pois as classes são muito dependentes de informações de outras classes. Não existe um Aluguel sem cliente, sem veículo e plano, e da mesma forma uma parcela só existe se existir um aluguel que para referir-se;
      
- __Diagrama UML de Classes:__ Disponível nesse diretório como o arquivo “Digrama de Classes.png" para visualização. Como esse diagrama foi criado usando a ferramenta dia, deixo junto o arquivo .dia para aqueles que desejarem utilizar esse diagrama como base para aprimoramentos dos elementos do projeto;
      
- __Persistência de Dados:__ Cada classe foi implementada utilizando-se o framework SQLAlchemy para permitir a persistência de dados via ORM, onde mapeamos os objetos dessas classes para registros em tabelas de uma banco de dados. Em específico optou-se pelo uso do Banco de Dados sqllite por simplicidade;
      
- __Bibliotecas:__ Cada classe foi implementada em um arquivo separado, podendo ser considerado um módulo único que compõem um conjunto de classes para persistência de dados que podem ser importados (individualmente ou em conjunto) para o uso em aplicações. Como exemplo, no próprio projeto foi necessário importar classes de outros arquivos para compor as definições, como é o caso de aluguel.py que importa cliente, cupom_desconto e veiculo_plano. Nesse caso foi possível implementar um biblioteca Orientada a Objetos para persistência de Dados relacionados a aluguel de veículos, mas que pode ser explorada para outros contextos; 

- __Reusabilidade:__ Além do próprio reúso garantido pelo paradigma orientado a objetos onde pode-se reutilizar a estrutura das classes e criar diversos objetos (como é o caso observado nos testes), pode-se citar também:

    - Herança: A herança é um recurso de OO que permite a reusabilidade por diferenciação, onde podemos utilizar uma classe para criar novos elementos de código apenas implementado aquilo que possuem de diferente. No projeto é possível observar o reúso da classe Cliente para definição das classes PessoaFisica e PessoaJuridica;

    - Organização em Módulos e Biblioteca: Como cada classe foi implementada individualmente, é possível que cada módulo seja importado e utilizado nas aplicações. O interessante é que isso não limita-se ao domínio do projeto. Algumas classes como Cliente, PessoaFisica, PessoaJuridica e Veiculo podem ser importadas e aprimoradas em outras aplicações;

    - Caso deseje considerar ainda o mesmo domínio de aplicação, podemos pensar em uma empresa de aluguel de veículos separa em setores. As classes implementadas até o momento permitem o registro de um aluguel, porém o setor financeiro pode utilizar a classe Parcela para recuperar dados financeiros e realizar seus afazeres. Um setor de mecânica próprio da locadora hipotética pode utilizar a classe Veiculo para recuperar dados necessários para as atividades do setor;

## Como executar

Em seguida são especificados os requisitos e passos necessários para executar os programas presentes no diretório Códigos;

### Ferramentas necessárias
- Linguagem Python - Versão utilizada: 3.8.10;
- Frameworks Flask – Versão utilizada: 2.0.1;
- Framework Flask-SQLAlchemy – Versão utilizada: 2.5.1;

### Passo a Passo

- Instalando os frameworks: Utilize a ferramente pip do Python.
```
pip install flask
pip install flask_sqlalchemy
```
ou
```
pip install -r requiriments.txt
```

- Executando o código: Entre no diretório src e digite python nome_programa.py.
```
cd src/

python parcela.py 
```

- Observando o retorno: O retorno dado será a exibição dos dados objetos da classe implementada naquele arquivo em formato JSON.
```
# Retorno da execução de python parcela.py

{'id': 1, 'data_registro': '18/7/2021', 'data_vencimento': '10/8/2021', 'valor_fatura': 743.75, 'quitado': False, 'aluguel': {'id': 1, 'cliente': {'id': 3, 'cliente': {'id': 3, 'nome': 'Beltrano', 'email': 'beltrano@gmail.com', 'endereco': 'Rua Dom Telano 5676'}, 'cpf': '333.333.333-33', 'data_nascimento': '4/1/1952'}, 'veiculo_plano': {'id': 4, 'veiculo': {'id': 2, 'marca_modelo': 'BMW 328i', 'ano': 2018, 'cor': 'Preto', 'kilometragem': '22000', 'cambio_manual': False, 'disponivel': False}, 'plano': {'id': 4, 'nomenclatura': 'Luxo', 'duracao_maxima': 7, 'duracao_minima': None, 'preco_diaria': 350.0, 'qtd_max_parcelas': 2}}, 'data_inicio': '20/7/2021', 'data_termino': '25/7/2021', 'cupom_desconto': {'id': 3, 'titulo': 'Na melhor Idade', 'descricao': 'Voltado para clientes com idade superior a 60 e que estão contratando o serviço.Pode ser usado apenas uma vez por cliente', 'desconto': 15}}}

{'id': 2, 'data_registro': '18/7/2021', 'data_vencimento': '10/9/2021', 'valor_fatura': 743.75, 'quitado': False, 'aluguel': {'id': 1, 'cliente': {'id': 3, 'cliente': {'id': 3, 'nome': 'Beltrano', 'email': 'beltrano@gmail.com', 'endereco': 'Rua Dom Telano 5676'}, 'cpf': '333.333.333-33', 'data_nascimento': '4/1/1952'}, 'veiculo_plano': {'id': 4, 'veiculo': {'id': 2, 'marca_modelo': 'BMW 328i', 'ano': 2018, 'cor': 'Preto', 'kilometragem': '22000', 'cambio_manual': False, 'disponivel': False}, 'plano': {'id': 4, 'nomenclatura': 'Luxo', 'duracao_maxima': 7, 'duracao_minima': None, 'preco_diaria': 350.0, 'qtd_max_parcelas': 2}}, 'data_inicio': '20/7/2021', 'data_termino': '25/7/2021', 'cupom_desconto': {'id': 3, 'titulo': 'Na melhor Idade', 'descricao': 'Voltado para clientes com idade superior a 60 e que estão contratando o serviço.Pode ser usado apenas uma vez por cliente', 'desconto': 15}}}

{'id': 3, 'data_registro': '1/8/2021', 'data_vencimento': '10/9/2021', 'valor_fatura': 0.0, 'quitado': True, 'aluguel': {'id': 2, 'cliente': {'id': 4, 'cliente': {'id': 4, 'nome': 'Indústrias Star', 'email': 'Star.Industry@gmail.com', 'endereco': 'Rua Supers H 3006'}, 'cnpj': '11.111.111/0001-11', 'descricao_atuacao': 'Empresa do Ramo de Tecnologia focada em construção e aprimoramento de equipamentos para produção e controle de energia renovável e sustentável'}, 'veiculo_plano': {'id': 2, 'veiculo': {'id': 3, 'marca_modelo': 'Volkswagen Saveiro Robust', 'ano': 2020, 'cor': 'Branco', 'kilometragem': '50000', 'cambio_manual': True, 'disponivel': False}, 'plano': {'id': 2, 'nomenclatura': 'Frota Empresarial', 'duracao_maxima': 365, 'duracao_minima': None, 'preco_diaria': 0.0, 'qtd_max_parcelas': 5}}, 'data_inicio': '1/1/2022', 'data_termino': '1/7/2022', 'cupom_desconto': {'id': 2, 'titulo': 'Empresa Sustentável', 'descricao': 'Voltado para empresas que comprovem preocupação com aspectos ambientais e sustentáveis', 'desconto': 30}}}

{'id': 4, 'data_registro': '9/10/2021', 'data_vencimento': '1/2/2022', 'valor_fatura': 0.0, 'quitado': False, 'aluguel': {'id': 3, 'cliente': {'id': 2, 'cliente': {'id': 2, 'nome': 'Ciclano', 'email': 'ciclano@gmail.com', 'endereco': "Rua Consat d'Aulio 93"}, 'cpf': '222.222.222-22', 'data_nascimento': '21/6/1999'}, 'veiculo_plano': {'id': 6, 'veiculo': {'id': 5, 'marca_modelo': 'Jeep Compass Trailhawk', 'ano': 2021, 'cor': 'Preto', 'kilometragem': '25000', 'cambio_manual': False, 'disponivel': True}, 'plano': {'id': 6, 'nomenclatura': 'Fideliade I', 'duracao_maxima': 365, 'duracao_minima': None, 'preco_diaria': 30.0, 'qtd_max_parcelas': 12}}, 'data_inicio': '10/8/2021', 'data_termino': '14/8/2021'}}

{'id': 5, 'data_registro': '9/10/2021', 'data_vencimento': '1/6/2022', 'valor_fatura': 0.0, 'quitado': False, 'aluguel': {'id': 3, 'cliente': {'id': 2, 'cliente': {'id': 2, 'nome': 'Ciclano', 'email': 'ciclano@gmail.com', 'endereco': "Rua Consat d'Aulio 93"}, 'cpf': '222.222.222-22', 'data_nascimento': '21/6/1999'}, 'veiculo_plano': {'id': 6, 'veiculo': {'id': 5, 'marca_modelo': 'Jeep Compass Trailhawk', 'ano': 2021, 'cor': 'Preto', 'kilometragem': '25000', 'cambio_manual': False, 'disponivel': True}, 'plano': {'id': 6, 'nomenclatura': 'Fideliade I', 'duracao_maxima': 365, 'duracao_minima': None, 'preco_diaria': 30.0, 'qtd_max_parcelas': 12}}, 'data_inicio': '10/8/2021', 'data_termino': '14/8/2021'}}
```
- Você pode visualizar a saída de uma maneira melhor simplesmente a copiando no site https://jsonformatter.curiousconcept.com/

```
{
   "id":5,
   "data_registro":"9/10/2021",
   "data_vencimento":"1/6/2022",
   "valor_fatura":0.0,
   "quitado":false,
   "aluguel":{
      "id":3,
      "cliente":{
         "id":2,
         "cliente":{
            "id":2,
            "nome":"Ciclano",
            "email":"ciclano@gmail.com",
            "endereco":"Rua Consat d'Aulio 93"
         },
         "cpf":"222.222.222-22",
         "data_nascimento":"21/6/1999"
      },
      "veiculo_plano":{
         "id":6,
         "veiculo":{
            "id":5,
            "marca_modelo":"Jeep Compass Trailhawk",
            "ano":2021,
            "cor":"Preto",
            "kilometragem":"25000",
            "cambio_manual":false,
            "disponivel":true
         },
         "plano":{
            "id":6,
            "nomenclatura":"Fideliade I",
            "duracao_maxima":365,
            "duracao_minima":"None",
            "preco_diaria":30.0,
            "qtd_max_parcelas":12
         }
      },
      "data_inicio":"10/8/2021",
      "data_termino":"14/8/2021"
   }
}
```

- Visualização do BD: Toda execução irá criar um arquivo .db que contém os dados criados no teste executado armazenados em banco sqllite. Caso deseje visualizar as estruturas do banco, você pode fazer o upload do arquivo no site https://inloop.github.io/sqlite-viewer/;