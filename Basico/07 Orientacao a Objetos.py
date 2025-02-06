## Orientação a Objetos
'''
Você foi contratado para criar um programa de folha de pagamento. Este programa precisa executar:
- Cadastro do funcionário
- Contratação do funcionário
- Cálculo da folha de pagamento
- Demissão de funcionário


  O    Classe Funcionário
/ | \  Propriedades: Nome, Data de Nascimento, Salario, Cargo
/  \   Métodos: Cadastrar, contratar, CalcularSalario, Demitir

'''

## Propriedades de objetos
class Teste:
    pass

minha_classe = Teste()
print(type(minha_classe)) #<class '_main_.Teste'>

'''Uma classe pode pode ter um construtor que é um método padrão que vai ser executado quando a classe é
instanciada'''

class NossaClasse:
    def__init__(self): #método de inicialização (executa toda vez que a classe é chamada)
        print("Eu existo")

'''Quando eu instancio a nossa classe, este método "Eu existo" é executado'''
var = NossaClasse()
print(var)

''' Nome é uma propriedade da classe, então quando eu instanciar a classe, eu vou poder acessar
essa propriedade'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print("Peddoa com nome %s e idade %d criada" % (nome,idade))

pessoa1 = Pessoa('Rodrigo', 34)
pessoa2 = Pessoa('Lucas', 21)

print((pessoa1.nome)) #Rodrigo

## Funções de objetos
Class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def print_nome(self):
        print("Meu nome é %s" % (self.nome))
pessoa1 = Pessoa('Rodrigo', 34)
pessoa2 = Pessoa('Maria', 22)

''' Uma função pode executar a própria função'''
    def print_string(self, nome):
        print("Meu nome é %s" % (nome))


## Classes com uma classe como atributo
''' Uma classe pode possuir como atributo uma outra classe. Quando você a instancia, você passa como parametro
um outro tipo para ela, uma outra classe e você consegue ler p atributo de outra classe'''

class Tipo1:
    def __init__(self, outra_classe):
        self.outra = outra_classe

class Tipo2:
    numero = 10

classe2 = Tipo2()
classe1 = Tipo1(classe2)

print(classe1.outra.numero)

''' Também podemos colocar uma lista de classes '''


## Herança
''' É quando uma classe pai tem atributos e métodos e classes filhas podem herdar esses atributos e métodos'''

class FormaGeometrica:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

class Quadrado (FormaGeometrica):
    pass
class Triangulo (FormaGeometrica):
    pass

quadrado = Quadrado(100,50)
triangulo = Triangulo(100,50)

print (quadrado.altura)


## Sobreposição de Funções
class ClassePai:
    def __init__(self):
        print("Sou a classe pai")

class ClasseFilha1(ClassePai):
    def __init__(self):
        print("sou a classe filha 1")

class ClasseFilha2(ClassePai):
    def __init__(self):
        print("sou a classe filha 1")

pai = ClassePai() #Sou a classe pai
filha1 = ClasseFilha1() #Sou a classe filha 1
filha2 = ClasseFilha2() #Sou a classe filha 2

'''Aqui temos uma sobreposição de um método da classe pai, caso você precise sobrescrever, você
precisa ter o que o método foi sobrescrito tem.'''


## HERANÇA MULTIPLA
''' Quando uma classe filho herda de mais de uma classe '''

class Base1:
    def __init__(self,atributo1):
        self.atributo1 = atributo1
    def Base1_print(self):
        print("Base1")

class Base2:
    def __init__(self,atributo1):
        self.atributo2 = atributo1
    def Base2_print(self):
        print("Base2")

class MinhaClasse(Base1,Base2):
    def __init__(self):
        Base1.__init__(self,10)
        Base2.__init__(self, 20)

var = MinhaClasse()
print(var.atributo1)
print(var.atributo2)
var.Base1_print()
var.Base2_print()


## MODIFICADORES DE ACESSO
''' Controla os acessos e garante a seguranã correta dos dados. Eles podem ter níveis de acesso por
padrão.
>> Público: Das instancias da classe, todos os atributos e todas as funções podem ser acesadas
>> Privado: Se você tem um atributo ou uma função privada, significa que essas funções e esses atributos
só podem ser acessados de dentro da própria classe. Uma variável da classe não pode manipular esses atributos
>> Protected: Só herda por convenção. Não usa
'''

class Segredo:
    def __init__(self):
        self.__segredo = 'Senha123' # o usuario pode testar se a senha está certa, mas não ver a senha

seg = Segredo()
print(seg.__segredo) # Retorna que o atributo segredo não existe. Para deixar publico, remover um _

#Funções privadas
'''Dentro da classe Segredo'''
    def __printa_segredo(self):
    print(self.__segredo)

    def printa_segredo(self):
    self.__printa_segredo() #Senha123

#Funções protected

class Base:
    def __base__privada(self):
        print('Pertençõ somente a base')
    def _baseprotegida(self):
        print("Pertenço a Base e a quem herdar")

Class Filha(Base):
    def acessa_protegida(self):
        self.baseprotegida()

filha = Filha()
filha.acessa_protegida() #Pertenco a base e a quem me herdar
filha.baseprotegida() #Pertenco a base e a quem me herdar



## PROTEGENDO ATRIBUTOS COM PROPERTY
'''Podemos usar uma função property para ler uma propriedade e também para alterar uma propriedade. Ela
vai fazer uma chamada de uma função e definir para alterar aquela propriedade'''

class Pessoa:
    def __init__(self,nome):
        self.__nome = nome

    def get_nome(self):
        print("pegando nome")
        return self.__nome

    def set_nome(self,nome):
        if len(nome)>0:
            print("Setando nome")
            self.__nome = nome

    nome = property(get_nome)

instancia = Pessoa("Maria")
print(instancia.nome)
instancia.nome = "Marcos"


##Protegendo Atributos com Decorators
'''Outra forma de proteger atributos são pelos decoradores. Uma propriedade que vai acida de uma chamada de função
com o @'''

class Natural:
    def __init__(self,numero):
        self.__numero = numero

    @property
    def numero(self):
        print("pegando numero")
        return self.__numero

    @numero.setter
    def numero(self, value):
        if value >= 0:
            self.__numero = value
            print("setando numero para", value)

numero = Natural(10)
numero.numero = 20
print(numero.numero)


## Métodos Estáticos
'''Atributo que não pertence a instancia da classe, mas a própria classe, então você não precisa de uma instancia
pra ler aquele atributo'''

class Teste:
    def __init__(self, gasolina):
        pass

    @classmethod
    def class_method(cls):
        print(cls)
    @staticmethod
    def static_method():
        print("static method"

    Teste.class_method()
    Teste.static_method()

    testando = Teste("aditivada")
    testando.class_method()

    class Veiculo:
        def __init__(self, nome, gasolina, potencia):
            self.nome = nome
            self.gasolina = gasolina
            self.potencia = potencia
        @classmethod
        def cria_carro(cls):
            return cls('carro', 'comum', 200)
        @classmethod
        def cria_trator(cls):
            return cls('trator', 'comum', 200)


## OBJETOS POR VALOR E REFERENCIA
''' As vezes fazemos cópia de variaveis ou objetos, e como o python vai tratar, pode variar o tipo do objeto
Acopla-se por
Valor: Um novo objeto é criado
Por Referencia: Apontam para o mesmo local em memória
'''
'''
Por valor é imutável:
Se você copiar ela, ela vai ser copiada por valor, porque é imutável, então é feita outra cópia é imutável

Por referencia, quando ele pode ser mutável 

No Python Objetos como classes e lista são mutaveis, portanto copiados por referencia
Tipos primitivos são imutaveis, portanto copiados por valor

delta = 10
delta = 20
'''

## Exemplos de Valor e Referência

lst1 = 10
lst2 = lst1
lst2 = 20
print(lst1) #10

lst1 = [1,2,3]
lst2 = lst1
lst2.append(10)
print(lst1) #[1,2,3,10]

## Deletando objetos

numero = 10
del numero #Objeto não existe mais


## Testando tipos e objetos
'''Como ver se um objeto pertence a uma determinada classe
se eu quero ver se o objeto é inteiro, se cria uma variavel para armazenar o resultado e ai se passa o
 objeto ou o valor e a classe ou o tipo de objeto que se quer testar'''


e_inteiro = isinstance(5, int) #True
e_inteiro = isinstance(5, (int, float, str)) #True
