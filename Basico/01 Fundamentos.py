#COMENTÁRIOS E MÉTODO PRINT

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


# PRINCIPAIS VARIAVEIS
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

#TECNICAS DE FORMATAÇÃO DE TEXTO
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


