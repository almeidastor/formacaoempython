## FUNÇÕES
'''Blocos automatizados de códigos

def nome(parametros) :
    ...
    ...
    return

- Os parametros são opcionais. São informações necessárias dentro da função
'''

## FUNÇÕES NO PYTHON

def func():
    num=10
    print("uma função %d" %(num))
func() #uma função 10

def func():
    pass
func()

def print_var(numero):
    print(numero)

print_var(2)
print("Maça")

def print_soma(num1, num2):
    print(num1 + num2)

print_soma(1,2) #3
print_soma(3.3, 1.1) #4.4
print_soma("olá", "mundo") #olá mundo

def func(*args):
    print(type(args))
    print("Argumentos são:", args)

func(1,2,3)
func()
func("Olá", True, [1,2,3])

def print_sub(num1,num2):
    print(num1-num2)
print_sub(num2=2, num1=10) #8


## ARGUMENTOS ARBITRÁRIOS
'''
As funções podem ter parametros, e os parametros podem ser dinamicos que são transformados atraves de uma tupla,
mas acontece que as vezes que a gente vê que o parametro tem um valor padrão e que o usuário pode informar o
valor, caso não informe a função vai utilizar o valor padrão
'''

def func(valor, nome = "teste"):
    print(nome,valor)

func(3) #Teste 3
func(3,"outro") #Outro 3

def executa_func(fun,x):
    func(x)

minha_funcao  = printa
print(type(minha_funcao))

executa_func(minha_funcao,10)


## FUNÇÕES COM RETORNO DE VALORES

def subtrai(num1,num2):
    valor = num1 - num2
    return valor

subtracao = subtrai(10,3)
print (subtracao)

def len_int(numero):
    numero_em_texto = str(numero)
    return len(numero_em_texto)

num1 = 10
num2 = 1230

tamanho1 = len_int(num1)
tamanho2 = len_int(num2)

print("O numero %d tem %d digitos" % (num1, tamanho1)) #O numero 10 tem 2 digitos
print("O numero %d tem %d digitos" % (num2, tamanho2)) #O numero 1230 tem 4 digitos


def retorna_multiplo():
    return 1,2

valor = retorna_multiplo()
print(valor)
print(type(valor))

## FUNÇÕES LAMBDA
'''Funções Lambda é uma função anonima mais simples, diferente de uma função normal, ela não
tem nome. Ela pode receber qualquer numero de parametro, mas ela só tem uma expressão'''

faz_soma = lambda x : x + 10


## FUNÇÕES LAMBDA NA PRÁTICA

faz_soma = lambda x : x + 10
valor = faz_soma(2)
print(valor) #12

multiplica = lambda x,y : x * y
valor = multiplica(2,10)
print(valor) #20

def multiplica(y):
    return lambda x : x * y

valor = multiplica(2)
resultado = valor (10)
print(resultado)


## FUNÇÕES RECURSIVAS
'''Existe problemas de programação que a gente resolve com uma função recursiva
A função recursiva é semelhante a um laço, a diferença é que ela vai retornar um valor toda vez
que ela for executada, e ela executa a si mesmo. Precisa ter uma condição de parada'''

def print_num(num):
    print(num)
    if num >=10:
        return
    print_num(num+1)

print_num(0)

def print_str(texto, indice):
    if indice == len(texto):
        return
    print (texto[indice])
    print_str(texto,indice + 1)

print_str("Python", 0)

def fatorial(num):
    if(num == 1):
        return 1
    return num + fatorial(num-1)

print(fatorial(10)) #3628800


## FUNÇÕES ANINHADAS
'''É quando você tem uma segunda função declarada dentro de outra função. E a função "filho" só pode ser declarada 
dentro da função pai'''

def pai():
    def filho():
        print("Sou filho")


def calculadora(num1, num2, op):
    def soma(a,b):
        return a + b
    def subtrai(a,b):
        return a - b
    if (op == '+'):
        return soma(num1,num2)
    elif(op=='+'):
        return subtrai(num1,num2)

## DECORATORS
'''São uma forma mais moderna de criar ou executar funções de forma alinhada'''


def DeixaMaiusculo(func):
    def inner_func():
        return func().upper()
    return inner_func
@DeixaMaiusculo
def retorna_string():
    return "string de teste"

