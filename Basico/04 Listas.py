## INTRODUÇÃO
'''
1) Tipos de dados que podem armazenar mais de um valor: Vetor. Geralmente os valores são relacionados
2) Por exemplo: Nomes de funcionários

LISTAS
-List:
Vetores dinâmicos.Pode ser modificado com adição e remoção.
Ordenada.

-Set:
Lista não ordenada, sem elementos duplicados.
Pode adicionar elementos, mas não modificar elementos existentes.
Não é possivel acessar elemento pelo indice

-Dictionary:
Lista com chave/valor
Permite modificações, mas não permite valores duplicados para as chaves

-Tuple:
Uma lista imutável.
Lista de valores que tem sempre o mesmo numero de itens e não pode ser modificada.
Ordenada
'''

## CRIANDO TIPOS DE LIST
array = []
array = list()
array_numeros = [1,2,3]
array_floats =  [56.3, -2.2, 0.5]
array_str = ["A","B","C"]
array_misto = [2,2.3,"ABC"]
print(array)
print(array_numeros)
print(array_floats)
print(array_str)
print(array_misto)

array = list([1,2,3])
print(array) #[1, 2, 3]
primeiro_elemento = array[0]
print(primeiro_elemento) #1
array[0] = 20
primeiro_elemento = array[0]
print(primeiro_elemento) #20
print(array[-1]) #3
print(array) #[20, 2, 3]

array = [1,"texto",3]
print(array[1:3]) #['texto', 3]

array = [10,2,3]
print(array) #[10, 2, 3]
array.append(2) #Adiciona um elemento ao final de uma lista
print(array) #[10, 2, 3, 2]
array.insert(2,"4") #Insere o numero 4 na posição 2
print(array) #[10, 2, '4', 3, 2]

array = [10,2,3,20,"3"]
array.remove(10) #Tenta remover o primeiro elemento de valor 10 da lista
print(array) #[2, 3, 20, '3']
array.pop(2) #Remove o elemento de indice 2 da lista
print(array) #[2, 3, '3']
print(len(array)) #Retorna o numero de elementos

array.clear() #Remove os elementos de uma lista
print(array)

array = [1, "teste", 1.3, True]
print (1 in array) #verifica se o valor 1 está presente na lista. Como o valor 1 está presente na lista, a expressão retorna True.
print(False not in array) #verifica se o valor False não está presente na lista array. Como o valor False não está presente na lista, a expressão retorna True.

lista = [5,6,7,2,3,4,7]
teste = lista.count(7) #Conta quantas vezes o número 7 aparece na lista lista.
print(teste) #2

lista = [5,6,7,2,3,4,7]
pos = lista.index(5) #Retorna o índice da primeira ocorrência do valor 5 na lista
print(pos) #0

array1 = [1,2,3]
array2 = [3,4,5]
soma = array1 + array2
print(soma) #[1,2,3,3,4,5]

array1 = [1,2,3]
mult = array1 * 3 #lista 3x
print(mult) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

numeros = ["um", "dois", "três"]
x,y,z = numeros
print(x)
print(y)
print(z)

cores = ["azul", "preto", "amarelo"]
for x in cores: #O loop for iterará sobre cada elemento da lista cores. Em cada iteração, a variável x assumirá o valor do próximo elemento da lista.
    print(x) #azul, preto, amarelo

cores = ["azul", "preto", "amarelo"]
for i in range(0,len(cores)): #cria uma sequência de números que vai de 0 até o fim da lista. Range vira os valores 1,2,3
    print(cores[i]) #azul, preto, amarelo (imprime as cores quando i assumir a posição atual)

cores = ["azul", "preto", "amarelo"]
indice = 0
while (indice < len(cores)): #Enquanto houver lista o loop é executado
    print(cores[indice]) #Imprime o elemento da lista cores no índice atual de indice.
    indice += 1 #Incrementa + 1 no indice

lista = [[1,2,3] ,[4,5,6]]
primeira_lista = lista[0] #[1, 2, 3]
segunda_lista = lista[1] #[4,5,6]
print (primeira_lista)
print(segunda_lista)
primeiro_elemento_primeira_lista = lista[0][0] #Localiza o primeiro elemento da primeira sub-lista
print(primeiro_elemento_primeira_lista) #1
primeiro_elemento_primeira_lista = lista[1][1] #Localiza o segundo elemento da segunda sub-lista
print(primeiro_elemento_primeira_lista) #5


## CONHECENDO SETS

lista_set = {}
lista2_set = {1,2,3}
lista3_set = set({1,2,3})
print(lista_set) #{}
print(lista2_set) #{1,2,3}
print(lista3_set) #{1,2,3}

lista_set = {1,2,3}
lista_set.add(5)
print(lista_set) #{1,2,3,5}
lista_set.remove(1)
print(lista_set) #{2,3,5}

'''
lista_set = {1,2,3,4}
lista_set.clear()
print(lista_set) #set()
print (len(lista_set(4))) #4
print(1 in lista_set) #True
print(5 in lista_set) #False
'''

lista_set = {1,2,3,'4',True,6.1}
for item in lista_set:
    print(item)

set1 = {1,2,3}
set2 = {1,2,3,4}
set_unido = set1.union(set2) #{1,2,3,4}
print(set_unido)
set_inser = set1.intersection(set2) #{1,2,3}
set_dif = set2.difference(set1) #{4}

## TUPLAS
'''
tupla = (5,"3", True, 7234)
    for x in tupla:
        print(x) #5 3 True 7234
    for i in range(0, len(tupla)):
        print(tupla[i]) #5 3 True 7234
'''

## Dominando Dictionaries

idades = {'ana':10 , 'maria':20 , 'joao':34 , 'fernando':'indefinido'}
print(idades['maria']) #20
print("ana" in idades)
idades.update({"joao":40})
idades.get('fernando')

lista = idades.items()
print(lista)
for item in lista:
    print(item[0], item[1])

#Separar chaves de valores
chaves = idades.keys()
valores = idades.values()
for item in chaves:
    print(item)
for item in valores:
    print(item)

#Busca de dados
lista_nome = list(idades.values())
pessoas_com_20_anos = lista_nome.count(20)
print(pessoas_com_20_anos) #2

#Limpando dados
idades.clear()

#Dados por nome
dados_por_nome = {
    'ana': {
        'sexo':'feminino',
        'cpf': '7878465555421',
        'rg': '8200000035'
    }
}
print(dados_por_nome['ana']['rg']) #8200000035


## LIST COMPREHENSIONS
'''Uma forma diferente de criar e manipular listas'''

lista = ['1' , 'zero' , 'Quatro']
lista = [x for x in lista]
print (lista)

lista = [x for x in range(1,11) if x %2 == 0]
print(lista) #[2,4,6,8,10]

lista_aux = [1,5,9]
lista = [x for x in range (1,11) if x not in lista_aux]
print(lista) #[2,3,4,6,8,10]

lista = [x for x in range(-10,20) if x < 10 if x >= 0]
print(lista) #[0,1,2,3,4,5,6,7,8,9]

lista = [x*2 for x in range(0,11)]
print(lista) #[0,2,4,6,8,10,12,14,16,18,20]

lista = ['negativo' if x < 0 else 'positivo' for x in range (-3, 4)]
print(lista) #['negativo','negativo','negativo','positivo','positivo','positivo','positivo',]

[[str(x) + '*' + str(y) + '=' + str(x*y) for x in range (1,5)]for y in range (1,10)]
'''[['1*1 = 1', '2*1 = 2', '3*1 = 3', '4*1 = 4'
    ['1*2 = 2', '2*2 = 4', '3*2 = 6', '4*2 = 8'
    ['1*3 = 3', '2*3 = 6', '3*3 = 9', '4*3 = 12'
    ['1*4 = 4', '2*4 = 8', '3*4 = 12', '4*4 = 16'
    ['1*5 = 5', '2*5 = 10', '3*5 = 15', '4*5 = 20'
    ['1*6 = 6', '2*6 = 12', '3*6 = 18', '4*6 = 24'
    ['1*7 = 7', '2*7 = 14', '3*7 = 21', '4*7 = 28'
    ['1*8 = 8', '2*8 = 16', '3*8 = 24', '4*8 = 32'
    ['1*9 = 9', '2*9 = 18', '3*9 = 27', '4*9 = 36'
'''

##ATIVIDADES
'''
1) Crie uma lista com os seguintes números 1,10,6,7,8,10. Em seguida printe a soma destes números
2) Cria uma lista e preencha ela com valores de 1 a 100, em seguida printe esses valores
3) Crie uma lista com os seguintes valores 30,4,43,52,65,-10 e 43,2,4,76,32,65,3. Agora faça a junção dessas listas,
mas se houverem valores repetidos entre ambas, eles não podem repetir na lista unida
4) Crie uma lista contendo o nome de todos os meses do ano. Em seguida receba por input o mês (número) em que 
você nasceu e mostre qual o nome do mês que você nasceu
5) Crie uma lista contendo todos os dias (número) do mes que você nasceu. Em seguida receba por input o dia (numero)
em que você nasceu e remova desta lista. Ao final mostre o conteúdo da lista
'''

array_numeros = [1,10,6,7,8,10]
print(sum(array_numeros)) #42

lista = [x for x in range(1,101)]
print(lista) #1...100

lista1 = [30,4,43,52,65,-10]
lista2  = [43,2,4,76,32,65,3]
lista3 = list(set(lista1+lista2))
print (lista3) #[32, 65, 2, 3, 4, 43, 76, 52, -10, 30]

meses = {'1':'Janeiro' , '2':'Fevereiro' , '3':'Março' , '4':'Abril' ,
         '5':'Maio' ,'6':'Junho' ,'7':'Julho' ,'8':'Agosto' ,
         '9':'Setembro' ,'10':'Outubro' ,'11':'Novembro' ,'12':'Dezembro' ,}
print(meses['10']) #Outubro

lista = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
             27,28,29,30,31}
dia = int(input("Qual o dia do seu aniversário?"))
if dia in lista:
    lista.remove(dia)
    print(lista)

'''
6) Escolha três objetos de sua escolha, e em seguida cria uma lista para armazenar o objeto e sua função.
Agora por input receba o nome desse objeto e imprima sua função. Caso o objeto não exista, informa ao usuário
Todas as atividades a seguir devem utilizar List Comprehension
7) Crie uma lista contendo numeros negativos de -30 até 20. Printe essa lista
8) Percorra os números de 4 a 100 e mantenha apenas aqueles divisiveis por 4
9) (DESAFIO) Crie uma lista contendo todos os numeros de 0 a 100, mas filtre, mantendo apenas os numeros que
terminam com 0
10) Percorra os numeros de 0 a 20 e crie um array, onde caso o numero terminar com zero o valor deverá ser 0,
caso contrário deverá ser '-'
'''

objetos = {
    'cadeira' : 'Serve para sentarmos',
    'monitor' : 'Serve para visualizar o  processamento',
    'Mouse' : 'Serve para realizar operações'
}
objeto_procurado = input("digite o objeto")
if objeto_procurado in objetos:
    print(objetos[objeto_procurado])
else:
    print("Objeto não encontrado")


lista = [ x for x in range(-30,-19)]
print(lista)


lista = [x for x in range(4,101) if x % 4 == 0]
print(lista)


lista = [x for x in range(4,101) if str(x)[-1] == 0]
print(lista)

lista = ['0' if str(x)[-1] == '0' else '-' for x in range(0,21)]
print(lista)
