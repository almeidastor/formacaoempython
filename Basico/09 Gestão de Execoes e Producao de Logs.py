
## Introdução a Gestão de Exceções
'''
> Ocorrencias em que um fluxo de programa produz algum tipo de erro
> Pode ser em decorrencia de problemas de codificação ou situação inesperada (banco de dados indisponivel)
> Uma exceção não tratada causa o fim do programa
> Uma exceção tratada permite controlar o fluxo do programa e se possivel, seguir um caminho diferente


try:
    nesse bloco pode ocorrer erro
except:[pode haver mais uma clausula]
    esse bloco é executado em caso de erro
else:[esse bloco é opcional]
    executa somente se não tiver erro
finally:[opcional]
    sempre será executada, com ou sem erro

'''

## Exemplos básicos
print ("inicio")
lista = [1,2,3]
print(lista[10])
print("Fim")

print("Inicio")
lista = [1,2,3]
try: #código que pode dar erro
    print(lista[10])
except Exception as error: #código executado se der erro
    print("Falha ao acessar, linha não encontrada" + str(error))
else: #código executado se não ser erro
    print("Não houve erro")
finally: #código executado sempre
    del lista
    print("Executa sempre que o try-except acabar, mesmo que não ocorra erro")
print("Fim")

## Diferentes Tipos de Exceções
'''Podem existir tipos de código que podem gerar um erro especifico ou podem gerar diferentes tipos de erro, então 
você pode criar tratamentos especificos ou um tratamento genérico'''

print("Inicio")
lista = [1,2,3]
try:
    print(lista[10])
except IndexError as erro1: #Só executa se o tipo IndexError ocorrer
    print("Erro de acesso ao Indice " + str(erro1))
except:
    print("ocorreu outro erro" + str(erro1))
else:
    print("Executa se não ocorre erro")
print("Fim")

'''
Lista de referencia de erros padrão
https://docs.python.org/3/library/exceptions.html
'''

## Gerando as Próprias Exceções
'''
Pode gerar um erro com uma mensagem própria
'''
raise Exception ("Nós geramos uma exceção")
raise IndexError ("Exceção de indice")

def printa_positivo(numero):
    assert (numero >=0)
    print(numero)
try:
    printa_positivo(-1)
except AssertionError as erro:
    print("O erro é", str(erro))
except Exception as erro1:
    print("Erro qualquer> ", str(erro1))


## Introdução a Logs
'''
> Registro da execução do Programa:
 - Erros
 - Etapas cumpridas
 - Avisos

> Por que?
 - Informação
 - Depuração
 - Registro de Atividade para fins de auditoria
 
> Onde?
 - Tela
 - Arquivo
 - Banco de Dados
'''

'''
PYTHON: LOGGING
- Classe de Gestão de Logs
- Permite salvar em Disco
- Formatar saída
- Levels
  - Debug
  - Info
  - Warning
  - Error
  - Critical
  
O Python tem o uso do logging pela classe e não pela instancia de uma classe, ou você usa o log que vai salvar em
disco ou usa o log na tela.
Se você quer usar os dois você vai ter que usar uma técnica chamada Handlers
'''


def custom_logger(level, message):
    import logging
    logger = logging.getLogger(__name__) #Permitir que crie um handler
    if not (len(logger.handlers)): #Verifica se o handler do log existe
        logging.basicConfig(level=logging.INFO) #o log base o info é nivel
        c_handler = logging.StreamHandler() #criação de log Stream(saida na tela)
        f_handler = logging.FileHandler("file.log") #criação do arquivo log que ele vai gerar em disco
        format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") #usar o mesmo formato para os dois
        c_handler.setFormatter(format) #aplicando o formato no primeiro handler
        f_handler.setFormatter(format) #aplicando o formato no segundo handler
        logger.addHandler(c_handler) #adicionando o handler de stream
        logger.addHandler(f_handler) #adicionando o handler de arquivo

    if level == 'debug': #se o usuario quer um nivel debug
        logger.debug(message)
    elif level == 'info':
        logger.info(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.critical(message)

'''
2022-06-22 00:32:49,657 - __main__ - ERROR - Parametro errado! ERROR:__main__:Parametro errado!
'''

custom_logger("info", "inicio do programa")
lista = [1,2,3]
try:
  print(lista[10]) #Indice errado
except:
  custom_logger("error", "indíce incorreto!") #mostra pro usuario e deixa registrado que ocorreu

custom_logger("info", "fim do programa")