## FUNÇÕES MATEMÁTICAS
''' Funções Built-in são funções prontas que você vai encontrar no python. Você encontrando essas funções
não precisa desenvolver'''

## Função Absoluto
''' Retorna a soma absoluta dos dois valores (desconsidera sinal)'''

num1 = -10
num2 = 10

print(abs(num1))
print(abs(num2))
print(abs(num1) + abs(num2)) #20

## Maior e menor valor
maior_valor = max(10,20,30)
print(maior_valor) #30

lista = [-20, 1,2.3,3]
print(min(lista)) #-20

## Potencia e raiz quadrada
x=2
y=3
print(pow(x,y))

import math
print(math.sqrt(25)) #5

## Arredondamento de numeros
print(round(2.4566,3)) #2.457
print(floor(2.4566)) #2 - arredonda pra baixo
print(ceil(2.4566)) #3 - arredonda pra cima

## Quociente e resto
print(divmod(10,4))



## CARACTERES PARA NÚMEROS E NÚMEROS PARA CARACTERES
numero = 70
caractere = chr(numero)
print("O numero %d é mapeado para o caractere %s" % (numero,caractere)) #F

for i in range(1,100):
    caractere = chr(i)
    print("%d - %s" % (i,caractere), end = '\n')

caractere = "F"
numero = ord(caractere)
print("O caractere %s é mapeado para o numero %d" % (caractere,numero)) #70


## FUNÇÕES DE TEXTO
texto = "ola, tudo bem?"
print(texto.capitalize()) "Ola, tudo bem?"

texto = "IsTo é EstraNHO"
print(texto.lower()) #isto é estranho
print(texto.upper()) #ISTO É ESTRANHO
print(texto.swapcase()) #iSto É eSTRAnho

texto = "eu sou um ótimo programador python"
print (texto.title()) #Eu Sou Um Ótimo Programador Python


texto = "1234567"
print(texto.center(9)) # 123456789
print(texto.center(14)) #   123456789
print(texto.center(14,'-')) #---123456789----

texto = "Ol@ eu sou @ ful@n@"
novo_texto = texto.replace("@","a")
print(novo_texto) #Ola eu sou fulana


## FUNÇÕES PARA LISTAS
lista = ["a","b","x","ab","d","c"]
lista.sort()
print(lista) #'a', 'ab', 'b', 'c', 'd', 'x'

lista = [5,10,2,1,5,10]
lista.sort(reverse=True)
print(lista) #[10,10,5,5,2,1]

produtos = [['carro','R$100.000'],
            ['cadeira', 'R$1000'],
            ['Moto', 'R$4000'],
            ['geradeira', 'R$20000'],
            ['armario', 'R$150']]
for produto, valor in produtos:
    print(produto,valor)


## FUNÇÕES DE DATA E HORA

import datetime

data_completa = datetime.datetime.now()
data = data_completa.date()
hora = data_completa.time()
print(data_completa) #2022-06-10 22:19:54.138151
print(data) #2022-06-10
print(hora) #22:19:54.138151
print("Dia", data_completa.day)

# y ano
# m mÊs
# d dia
# H hora formato 00-23
# M minuto
# S segundo

atual = datetime.datetime.pow()
current_time = atual.strftime("%d/%m/%Y %H : %M : %S") #22/06/2022 22:19:54 - Formato string

# A dia da semana
# a dia da semana abrev.
# B nom do mês
# b nome do mês abrev.
# I hora no formato 12h
# p AM PM

data = datetime.datetime(2000,9,30,10,30,20)
print(data.strftime("%A - %a")) #Saturday - Sat

from datetime import datetime, timedelta
data_atual = datetime.now()
datafutura1 = data_atual + timedelta(weeks=4)

data_2000 = datetime.datetime(2000,1,1,0,0,0)
data_agora = datetime.datetime.now()
diferenca = data_agora - data_2000

print("Desde o ano 2000 passou", diferenca.days, "dias") #Desde o ano 2000 passou 8196 dias
print("Desde o ano 2000 passou", diferenca.seconds, "segundos") #Desde o ano 2000 passou 84084 segundos
print("Desde o ano 2000 passou", diferenca.microseconds, "microsegundos") #Desde o ano 2000 passou 69495 microssegundos


## LENDO ENTRADA DE DATAS

import datetime
data_txt = input("Digite a data no formato dia/mes/ano:")
datetime = datetime.datetime.strptime(data_txt, "%d/%m/%Y")
print(datetime) #2022-11-01 00:00:00
print(type(datetime)) #formato datetime

