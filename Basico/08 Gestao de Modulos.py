## INTRODUÇÃO A MÓDULOS
'''
* Bibliotecas empacotadas
* Trazem funções prontas
  - Ler arquivo
  - Ciencia de Dados
  - Conectar com Banco de Daods
  - Interagir com Serviços na Nuvem
  - etc
* Você pode criar seus módulos!
* Módulos podem já vir instalados, você só precisa importar
  - Depende do ambiente Python que você usa
'''

## Uso básico de Módulos
import datetime
print(type(datetime))
data = datetime.datetime(2022,5,15,10,4,5)
print(data)

import random
print(random.randrange(10,100)) #22
from random import randrange
print(randrange(10,100)) #94
from random import randrange as num_aleatorio
print(num_aleatorio(10,100))
from random import * #usa todas as funções de random

## Explorando um Módulo
import random
dir(random)
#Gera uma lista de funções, atributos e classes que existem dentro desse modulo
dir(random.randrange)
#Trás detalhes especificamente dessa função
print(random.__name__)
print(random.__file__)
print(random.__doc__)

## PIP
'''Faz o gerenciamento de módulos (mostra os módulos instalados, desinstala módulos, faz atualização da
versão de módulos. Geralmente se usa da linha de comando Shell do SO'''

!pip list #Mostra todos os pacotes que já estão pré instalados no ambiente virtual

!pip install pmdarima
!pip install pmdarima==1.2.1
!pip uninstall pmdarima

## Criando um Módulo
'''Criando um arquivo de texto plano, sem formatação que vai ter extensão py'''

PI = 3.1415
class Teste:
    def __init__(self):
        print('Classe teste')

def MyFunc(num):
    print(num)


import teste
dir(teste)
from teste import MyFunc
MyFunc("Teste")
from teste import PI as NUMERO_PI
print(NUMERO_PI)

## Parâmetros de Execução
'''Quando importamos um módulo, o nome de um módulo sempre pegamos pela propriedade __name__
Se eu quiser saber onde esse módulo está fisicamente é pelo __file__
'''
print(teste.__file__)

## Criando e lendo Ajuda de Módulos

print (print.doc) ##exibe a documentação do print

''' 
Assim começa a criação da documentação de um módulo, dentro das 3 aspas simples, pode ter algum dizersobre
este é o arquivo principal ocntendo uma variavel chamada euler e uma função chamada soma. Essa é uma
documentação especifica do módulo
'''

euler = 2.71828

def soma (num1, num2):
    '''Função que soma dois numeros recebidos por entrada, essa é uma documentação especifica da função'''
    return num1 + num2
print(__doc__) #Le a documentação do módulo
print(soma.__doc__) #Le a documentação da função
help(soma) #trás ajuda sobre o módulo