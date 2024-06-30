##COMENTÁRIOS E MÉTODO PRINT

#Isto é um Comentário (Entre sustenido)

print ("Olá Mundo") #Isto é um comentário

''' Este é um comentário 
de multiplas linhas'''

# O método Print pode exibir qualquer informação como saída:

print ("Olá Mundo")
print (10)
print (20.5)
print ("maça",20, 30.45) #maça 20 30.45
print ("Maça", "Pera", "Uva", sep='-') #Maça-Pera-Uva
print ("Maça", "Pera", "Uva", end='Fim', sep=' ') #Maça Pera UvaFim
print ("Maça", "Pera", sep='\n' ) #separador de linha
print ("A pontuação total de %s foi %s pontos" % ("Fernando","10")) #A pontuação total de Fernando foi 10 pontos
print ("A pontuação total de {} foi {} pontos" .format("Fernando","10")) #A pontuação total de Fernando foi 10 pontos
print ("A pontuação total de " + "Fernando " + "foi " + "10 "+"pontos") #A pontuação total de Fernando foi 10 pontos

# ATIVIDADES
# • 1 - Realize o print do seu nome completo, sua idade e sua altura utilizando um print para cada valor.
print ("Nome " , "Getulio")
print ("Idade " , 10 )
print ("altura " , 1.75 )

# • 2 - Realize o print do seu nome completo, sua idade e sua altura utilizando apenas um print para todos valores.
print ("Meu nome é %s tenho %s anos e tenho %s de altura" % ("Getulio",10, 1.75))

# • 3 - Realize o print de 3 números de sua escolha em um mesmo print, mas separados pelo caractere '-'.
print (1,2,3, sep='-')


## PRINCIPAIS VARIAVEIS
''' 
Tem que começar com letra com caractere underline
Só pode conter letras ou numeros
Letras maiusculas e minusculas (Nome NOME nome) são tratadas como se fossem variaveis diferentes
'''

_numero = 1
Numero = 2
numero = 3
numero123 = 4

print (_numero, Numero, numero, numero123) #1 2 3 4
#O tipo da variavel é definida de forma implicita pelo python

variavel = None #variavel reservada (diferente de 0)
inteiro = 10
decimal = 1.53
texto = "Olá, isto é um texto"
logico = True
var2 = variavel
saldoBancario = 100 # padrão camel case
SaldoBancario = 100 # padrão pascal case
saldo_bancario = 100 # padrão snake case

#1 - Crie uma variável de cada tipo e ponha alguma valor escolhido. Em seguida, printe todos esses valores.
#2 - Cria variáveis para guardar seu nome, CPF e uma que indique se você esta casado, em seguida printe esses valores separadamente, mas não esqueça de printar junto o que eles significam

## TECNICAS DE FORMATAÇÃO DE TEXTO
''' 
%s texto
%d inteiro
%f float
'''

nome = "Carolina"
idade = 23
altura = 1.73
texto = "Meu nome é %s. Tenho %d anos e %f metros de altura" % (nome, idade, altura) #Meu nome é Carolina. Tenho 23 anos e 1.730000 metros de altura

numero_gigante = 1.123456789
print("numero gigante formatado: %.2f" % (numero_gigante)) #numero gigante formatado: 1.12

valor = True
print ("O valor é %s" % (valor)) #O valor é True
print ("O valor é %d" % (valor)) #O valor é 1

decimal = 23.4566
print ("A parte inteira é %d" %(decimal)) #A parte inteira é 23


## FORMATAÇÃO COM CARACTERES ESPECIAIS

texto = "Olá, assim se quebra linha, \n entendeu?"
texto2 = "Assim se faz uma \t tabulação"
texto3 = 'Deixa a \'palavra\' entre aspas' #Deixa a 'palavra' entre aspas
texto4 = "Deixa a 'palavra' entre aspas" #Deixa a 'palavra' entre aspas


# ATIVIDADES
#1: Escreva e formate a data em que você nasceu no formato dia/mês/ano. Não esqueça de criar 3 variaveis para guardar
#2: Escreva e formate a hora e minuto atual
#3: Escreva um programa que contém o numero PI que deve ter o valor exato 3,14159265359 e formate para ter apenas 5 casas decimais

dia = 2
mes = 10
ano = 1993
print ("Eu nasci em %d/%d/%d" %(dia,mes,ano))

from datetime import datetime
data = datetime.now()
hora = data.strftime('%H')
minuto = data.strftime('%M')
print ("Agora são %s horas e %s minutos" %(hora, minuto))

pi= 3.14159265359
print("O Pi é %.5f" % (pi))


## OPERADORES ARITMÉTICOS

# Adição (+) : resultado = a + b
# Subtração (-) : resultado = a - b
# Multiplicação (*) : resultado = a * b
# Divisão (/) : resultado = a / b
# Potenciação (**) : resultado = a ** b
# Resto da divisão (%) : resultado = a % b
# Operador de Divisão inteira (//) : resultado = a // b
# Operador de Negação (-) : resultado = -a


## ORDEM DE PRIORIDADE

# Segue a ordem de Precedencia:
# 1ª Potenciação
# 2ª Multiplicação, Divisão e resto da divisão
# 3ª Adição e Subtração

nume1 = 10 * (2+1) # Será resolvido o que primeiro está dentro do parenteses


# ATIVIDADES
'''1) Crie um programa que possui duas variáveis, uma que recebe o ano em que estamos e uma
que recebe o ano em que você nasceu. Em seguida subtraia ambas para receber uma estimativa
de quantos anos você tem. Mostre esse valor na saída do programa'''

'''2) Crie um programa que faz a média aritmética entre 3 números. Esses números devem ser
salvos em uma variável. Mostre esse valor na saída do programa'''

'''3) Crie um programa que calcule o IMC (indice de massa corporal). O MC é dado pelo peso em KG
dividido pela altura em metros elevado ao quadrado. Salvar esses valores em uma variavel .
. Mostre esse valor na saída do programa'''

'''4) (DESAFIO) Você tem um determinado número de ovos de páscoa para dividir entre um determinado
número de pessoas (duas variaveis iniciais). Determine quantos ovos ficarão por pessoa e quantos ovos
sobrarão pois não puderam ser divididos igualmente. Lembre que o número de ovos por pessoa é
um número inteiro'''


ano = input("Em que ano estamos?")
nasc = input("Em que ano você nasceu?")
idade = int(ano) - int(nasc)
print ("sua idade é: %d" %(idade))

###

num1 = input ("Insira o Primeiro Numero: ")
num2 = input ("Insira o Segundo Numero: ")
num3 = input ("Insira o Terceiro Numero: ")
media = (int(num1) + int(num2) + int(num3))/3
print ("A média dos 3 números é %d" %(media))

###

peso = input ("Insira seu peso: ")
altura = input ("Insira sua altura: ")
imc = float(peso)/(float(altura)**2)
print("O IMC é: %.2f" %(imc))

###

ovos = input ("Quantidade de ovos: ")
pessoas = input ("Quantidade de pessoas: ")
divisao = int(ovos) // int(pessoas)
resto = int(divisao) % int(pessoas)
print ("A divisão resultou em %.0f para cada, restando %.0f ovos" %(divisao,resto))



## OPERADORES LÓGICOS
'''Aplicados a operações lógicas e tem como resultado verdadeiro ou falso'''

#AND: Resulta verdadeiro se todos os valores envolvidos na operação forem verdadeiros, caso contrario resulta em false
'''
True AND False: False
True AND True: True
False AND False: False
'''
#OR: Resulta em verdadeiro se qualquer um dos operadores forem verdadeiros
'''
True OR False: True
True OR True: True
False OR False: False
'''
#NOT: Inverte o resultado lógico
'''
Not(True): False
Not(False): True
'''

## OPERADORES AND E OR
resultado1 = True and False
print(resultado1)

clima_bom = True
estou_disposto = True
vou_ao_mercado = clima_bom and estou_disposto
print ("Vou ao mercado?", vou_ao_mercado) #True

clima_bom = True
estou_disposto = False
vou_ao_mercado = clima_bom or estou_disposto
print ("Vou ao mercado?", vou_ao_mercado) #True

#Prioridade

#NOT, AND, OR

bool1  = True or False and True #True
bool2 = True or not False #True
bool3 = True and not (True or False) #False

'''
1) Crie um programa que diga "Se você precisa ir ao mercado". Você precisa ir ao mercado se 
"faltar comida ou "se for sábado". Mostre na saída do programa o valor lógico, indicando sim ou não

2) Crie um programa que responda "se você pode atravessar a rua" na faixa de pedestres. Você pode
atravessar a rua se o "sinal estiver vermelho" e "se não houver nenhum carro vindo a direita" e "nem
esquerda". Altere as variaveis para verificar se o programa está correto. Mostre na saída do programa
o valor lógico

3) Agora faça a mesma coisa que o exercicio anterior, mas desta vez você etá com pressa para atravessar
a rua, basta que o sinal esteja vermelho "OU" que não venha carro da esquerda e direita. Altere as
variáveis para verificar a resposta em comparação com ao exercicio anterior. Mostre a saída do
programa o valor lógico

'''

falta_comida = True
e_sabado = False
eu_preciso_ir_ao_mercado = falta_comida and e_sabado
print ("Eu preciso ir ao mercado?", eu_preciso_ir_ao_mercado)

sinal_vermelho = True
carroaesquerda = False
carroadireita = False
posso_atravessar = sinal_vermelho and not carroaesquerda and not carroadireita
print ("Eu posso atravessar?", posso_atravessar)

sinal_vermelho = False
carroaesquerda = False
carroadireita = False
posso_atravessar = sinal_vermelho or not carroaesquerda and not carroadireita
print ("Eu posso atravessar?", posso_atravessar)

## TYPE AND CASTING

#TYPE: Mostra o tipo de uma variável
texto = "olá" #class 'str'
numero = 2 #class 'int'
decimal = 1.5 #class 'float'
booleano = True #class 'bool'
print (type(texto))

#CASTING: Transformar dados de um tipo para o outro
'''
string_em_int = int(texto) #Type passa a ser inteiro
string_em_float = float(texto) #Type passa a ser float
int_em_string = str(numero) #Type passa a ser string
int_em_float = float(numero) #Type passa a ser float
int_em_bool = bool(numero) #Type passa a ser booleano
float_em_string = str(decimal) #Type passa a ser string
float_em_int = int(decimal) #Type passa a ser inteiro
float_em_boolean = bool(decimal) #Type passa a ser booleano
'''

'''
1) Crie um programa que possui uma variavel do "tipo string" contendo um número qu indique quanto
você tem no banco. Em seguida desconte mil deste valor e mostre na saída do programa

2) Crie um programa que indique se seu saldo bancário está zerado (valor lógico). Declare uma
variavel para guardar seu saldo bancário.

3) Crie um programa que contenha sua altura, mas deve somente mostrar a parte inteira da sua altura
na saída do programa, pois queremos uma estimativa
'''

saldo_banco_str = "1500.75"
saldo_banco_float = float(saldo_banco_str)
novo_saldo = saldo_banco_float - 1000
novo_saldo_str = str(novo_saldo)
print("Seu novo saldo é: " + novo_saldo_str)

saldo_banco_str = "0.0"
saldo_banco_float = float(saldo_banco_str)
saldo_zerado = (saldo_banco_float == 0.0)
print("Seu saldo bancário está zerado: " + str(saldo_zerado))

altura = 1.75
altura_inteira = int(altura)
print("A parte inteira da sua altura é: " + str(altura_inteira))


## LENDO ENTRADAS DO USUÁRIO
'''
valor = input ()
idade = eval(input("Quantos anos você tem? ")) #input converte como número
'''
'''
1) Crie um programa que leia por input dois números e realize a divisão entre ambos. Formate
o print para mostrar o calculo completo

2) Crie um programa que mostre o dia, mês, ano, hora, minuto e segundos inseridos pelo usuário.
Formate o valor
'''

num1= input("Um numero: ")
num2= input("Outro numero: ")
div = int(num1) / int(num2)
print(div)

dia = input("Insira o dia: ")
mes = input("Insira o mes: ")
ano = input("Insira o ano: ")
hora = input("Insira a hora: ")
minuto = input("Insira o minuto: ")
segundo = input("Insira o segundo: ")

print ("%s/%s/%s/ %s:%s:%s" %(dia, mes, ano, hora, minuto,segundo))


## ATRIBUIÇÃO E COMBINAÇÃO DE OPERADORES LÓGICOS

numero = 1 #Atribui 1 a numero
numero +=1 #numero recebe o proprio valor da variavel e soma 1
numero /=2 #divide o valor de numero por 2
booleana = (numero == 10) #verifica se numero é igual a 10
emaior = nume1 > nume1 #Numero 1 maior que numero 2
emenor = nume1 < nume1 #Numero 1 menor que numero 2
maiorigual = nume1 <= nume1 #Numero 1 menor ou igual que numero 2
boolean = nume1 > 0 and nume1 < 10 #Numero entre 0 e 10

'''
Crie um programa que responda se você foi aprovado numa prova. Você somente  foi aprovado numa prova
se sua média for maior ou igual que 7 ou se sua nota no exame for maior ou igual a 5. 
Leia esses valores  por input

2) Crie um programa que diga se a senha está correta e portanto você tem acesso ao sistema. A senha
deverá ser salva no código, e a tentativa deve ser lida por input
'''

media = input("Qual é sua média?")
exame = input ("Qual é sua nota no exame?")
aprovado = int(media) >= 7 or int(exame) >= 5
print (aprovado)


senha = "mysharepoint123"
tentativa = input ("coloque a senha ")
criptografia = senha == tentativa
print (criptografia)


## SLICING DE STRINGS

var = "EXEMPLO"
'''    0123456'''
#var[3] -> "m"
#var[1:3] -> "xe" - ultima posição ignorada
#var[3:] -> "mplo" - Da posição até a ultimo caractere
#var[:5] -> "exemp" - Do inicio até o 4o aractere

texto1 = "olá"
texto2 = ", "
texto3 = "tudo bem?"
texto_completo = texto1 + texto2 + texto3 #olá, tudo bem?
texto1 += "mundo" #olá mundo
texto = "Python é bem produtivo,"
texto_repetido = texto * 3 #Python é bem produtivo, Python é bem produtivo, Python é bem produtivo

var = "CARRO"
'''   -54321'''
print (texto[-4]) #a
print (texto[::-1]) #ortem
texto = "abcdefg"
texto = texto [:3] + texto [4:] #abcefg

## OPERADORES DE STRINGS
texto1 = "Ola"
texto2 = "Ola"
igual = texto1 == texto2
print ("Textos são iguais?", igual) #True
print ("a" != "a") #False

texto = "Programação"
print ("a" in texto) #Se está contido a na palavra Programação, retornará verdadeiro
print ("Vinte" not in texto)

tamanho = len(texto)
print (tamanho) #11

#ATIVIDADES
'''
1) Crie uma única string que contém seu nome e sobrenome, em seguida use o Slicing para separar
o nome em uma variavel e o seu sobrenome em outra. Printe esses valores
2) Leia uma String através do input e retire o ultimo caractere
3) Faça um programa que leia uma String através do input e diga se ela possui uma vogal
4) Faça um programa que insira a palavra "ABC" na primeira posição de uma string lida por input
'''
nome = "Felipe Otávio"
prim_nome = nome[:6]
sobrenome = nome[6:]
print(prim_nome + "" + sobrenome)

palavra = input("Insira uma palavra: ")
print (palavra[:-1])

palavra = input("Insira uma palavra: ")
possui_vogal = ("a" in palavra) or ("e" in palavra) or ("i" in palavra) or ("o" in palavra) or ("u" in palavra)
print (possui_vogal)

palavra = input("Insira uma palavra: ")
print ("ABC" + palavra[0:])


