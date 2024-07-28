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