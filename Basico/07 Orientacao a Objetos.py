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