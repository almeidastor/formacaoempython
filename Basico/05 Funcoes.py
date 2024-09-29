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