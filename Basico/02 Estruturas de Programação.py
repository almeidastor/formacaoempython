## FUNDAMENTOS DA ESTRUTURA IF

print ("isto está fora dos ifs")
if (True):
    print("Este código vai ser executado")

print ("isto está fora dos ifs")
if (False):
    print("Este código não vai ser executado") #não aparece

print ("isto está fora dos ifs")

valor1 = 10
valor2 = 20
sao_iguais = (valor1 == valor2)
if sao_iguais:
    print ("são iguais") #condição falsa, não executa


## UTILIZANDO ELSE
## Sempre deve ser utilizado depois de IF e ele vai ser executado caso o if não seja executado (if = false)

numero = 9
if (numero>10):
    print ("É maior que 10")
else:
    print ("É menor que 10")


## ANINHANDO IFS
'''
Em uma mesma estrutura eu só posso ter um if e eu só posso ter um else (opcional). Outro argumento é o elif
Existe outro argumento que é o ELIF pode ser usado para testar condições lógicas adicionais e podem ser usado quantas vezes quiser
O ELIF deve estar entre o IF e o ELSE
'''

numero = 11
if numero < 10:
    print ("Menos que 10")
elif numero < 100:
    print("Menos que 100")
elif numero < 1000:
    print("Menos que 1000")
else:
    print ("Nenhuma anterior")

numero = 1
resultado = "Um" if numero == 1 else "Dois" if numero == 2 else "Três"


## ATIVIDADES
'''
1) Crie um novo programa que receba o seu saldo bancário e o quanto você deve. Em seguida o programa
deve dizer se você tem o saldo positivo ou negativo.

2) Crie um programa que possui uma variavel que guarde seu CPF e que guarde uma senha de sua escolha. 
Em seguida receba por input uma senha de usuário. Caso a senha recebida seja a correta mostre o CPF,
caso não diga que a senha está incorreta

3) Crie um programa que fale sobre a sua idade. As regras são a seguinte, você deve receber por input
a sua idade, se você tiver até 3 anos printe que é um bebê, até 13 anos uma criança, até 18 anos
adolescente, até 65 adulto. E em nenhum desses casos é um idoso

4) Crie um programa que receba 2 numeros, e também receba do usuário a operação que deve ser feita, as
possibilidades são soma (+), subtração (-), divisão (/) e multiplicação (*). Realize a operação escolhida
sobre os dois numeros
'''

saldo = 1200.00
deve_cartao = 500.00

print("Seu saldo: R$",saldo)
print("--------------------------")
print("Fatura do cartão: R$",deve_cartao)

if saldo > 0 and saldo > deve_cartao:
    print ("Você tem saldo suficiente, gostaria de pagar sua fatura? (Y/N)")
    resposta = input()
    if resposta == "Y":
        saldo = float(saldo) - float(deve_cartao)
        deve_cartao = 0
        print ("Seu saldo: R$",saldo)
        print("--------------------------")
        print("Fatura do cartão: R$", deve_cartao)
    elif resposta == "N":
        print("Seu saldo: R$", saldo)
        print("--------------------------")
        print("Fatura do cartão: R$", deve_cartao)
    else:
        print("Insira um comando válido")
else:
    print("Você não tem saldo suficiente")



cpf = "123.456.789-00"
senha = "minhasenha"

print ("=====BEM-VINDO======")
print ("DIGITE SUA SENHA DE ACESSO")
portal = input ("Senha: ")
if senha == portal:
    print("=================")
    print("Olá, seu CPF é: ", cpf)
else:
    print("senha não confere")



idade = int(input("Coloque a sua idade em anos: "))
if idade <= 3:
    print("você é um bebê")
elif idade > 3 and idade <=13:
    print("você é uma criança")
elif idade > 13 and idade <=65:
    print("você é um adulto")
else:
    print("Você é um idoso")


numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
print("OPERADORES")
print("1) Soma")
print("2) Subtração")
print("3) Multiplicação")
print("4) Divisão")

operador = input("Escolha o número do operador: ")
if operador == "1":
    resultado = numero1 + numero2
    print(resultado)
elif operador == "2":
    resultado = numero1 - numero2
    print(resultado)
elif operador == "3":
    resultado = numero1 * numero2
    print(resultado)
elif operador == "4":
    resultado = numero1 / numero2
    print(resultado)
else:
    print("Coloque um número válido")


## LAÇOS WHILE
'''
EXECUTA UM CÓDIGO ENQUANTO A CONDIÇÃO DELE FOR VERDADEIRA
'''


interacao = 10
while (interacao > 0):
    print(interacao)
    interacao-=1

indice = 10
print ("Programa começou")
while (indice >= 2):
    resto = (indice % 2)
    if resto == 0:
        print ("O número %d é par" % (indice))
    else:
        print ("O número %d é impar" % (indice))
    indice -= 1
print("Programa finalizado!")

soma = 0
numeros_lidos = 0
while (numeros_lidos < 5):
    num_str = input ("Digite um valor: ")
    num_lido = float(num_str)
    soma += num_lido
    numeros_lidos += 1
print("Soma é %.2f" % (soma))


texto = "Olá 123_"
indice = 0
while (indice < len(texto)):
    print (texto[indice])
    indice += 1


## USO DE BREAK E CONTINUE

num_atual = 0
while (True):
    if (num_atual == 5):
        break
    print (num_atual)
    num_atual += 1
print ("Encerrou!")


## ATIVIDADES
'''
1) Crie um programa que receba 5 números e retorne a média aritmética entre esses números
2) Crie um programa que receba 5 números, realiza a soma destes números, mas caso um destes números seja
negativo não considere ele na soma
3) Cria um programa que receba um número arbitrário (definido pelo usuário) de números que sesão lidos
e retorne a soma de todos eles
4) Percorra os números 2 até 10 e diga se o número é par ou impar
5) Crie um programa que receba como input uma string. Em seguida percorra a string e diga quantos espaços
em branco essa string tem
'''

contador = 1
indice = 1
numero_armazenamento = 0
while (contador <= 5):
    numero_list = int(input("Insira o %dº número: " % (indice)))
    numero_armazenamento = numero_list + numero_armazenamento
    contador += 1
    indice += 1
print(numero_armazenamento/5)

contador = 1
indice = 1
numero_armazenamento = 0
numero_list = 0
while (contador <= 5):
    numero_list = int(input("Insira o %dº número: " % (indice)))
    if(numero_list>=0):
        numero_armazenamento = numero_list + numero_armazenamento
        contador += 1
        indice += 1
    else:
        numero_list = int(input("Insira o %dº número: " % (indice)))
print(numero_armazenamento)


## USO DE FOR
'''
Ele vai executar um intervalo e ele vai executar cada valor desse intervalo
'''
for x in range(10):
    print (x)

'''
A função RANGE pode ter 3 parametros, a posição de inicio, a posição de parada e o step (passo)
Se não for informado o padrão de inicio é 0 e o Stop é o único que é obrigatório ele sempre 
para um número antes
'''

for x in range(5,20,5):
    print (x)

texto = "123t56789"
for x in range (0, len(texto)):
    print (texto[x])

letra = input("Digite uma letra: ")
if (len(letra) != 1):
    print("Precisa ter um digito")
else:
    texto = input("Digite um texto: ")
    for i in range (0, len(texto)):
        if letra == texto [i]:
         print("Encontrei a letra %s na posisção %d" %(letra, i))

for x in range(1,4):
    print("------------------")
    for y in range(1,11):
        print("%d x %d = %d" % (x,y,x*y))

## ATIVIDADES
'''
1) Crie um programa que receba uma string por input e conte quantos caracteres ela tem,
não leve em conta os caracteres por espaço. Você não deve usar o len()

2) Crie um programa que faça o calculo do fatorial de um número. O fatorial a ser calculado 
deve ser recebido por input

3) Crie um programa que leia uma quantidade arbitraria de textos e concatene eles numa string unica

4) Crie um programa que printe a tabuada de divisão de um número lido por input

5) (DESAFIO) Crie um programa que percorra os numeros de 3 até 30 e diga se o número é primo ou não
'''

texto = input("Digite um texto: ")
num_caracteres = 0
for letra in texto:
    if(letra != " ,"):
        num_caracteres +=1
print ("Tem %d caracteres no texto" % (num_caracteres))


fatorial_str = input("Digite o fatorial desejado: ")
fatorial_numero = int(fatorial_str)
resultado = 1
for i in range(1,fatorial_numero + 1):
    resultado *=1
print ("O fatorial de %d é %d" % (fatorial_numero, resultado))


numero_de_leituras = int(input("Digite o numero de textos que serão lidos "))
texto_total = ""
for i in range(numero_de_leituras):
    texto_total += input("Digite o texto: ")
print ("Texto completo: ", texto_total)


numero = int(input("digite a tabuada de divisão desejada: "))
for num in range(1,11):
    print("%d / %d = %f" % (num, numero, num / numero))


for numero in range (3,31):
    e_primo = True
    for num_teste in range(2,numero):
        if (numero % num_teste == 0):
         e_primo = False
         break
    if (e_primo):
        print ("O numero %d é primo" % (numero))
    else:
        print("O numero %d não é primo" % (numero))
