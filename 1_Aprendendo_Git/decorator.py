import time
import math

def tempo(func):
    def mediadora():
        inicio = time.time()
        func()
        fim = time.time()
        print(f'O tempo foi de {fim - inicio}')
    return mediadora




@tempo
def par_impar(lista = [784, 8754214766984, 41, 48,25,43,36,21,5,9,7894, 78542, 96541, 3652]):
    lista1 = list(('par' if x%2 ==0 else "Impar" for x in lista ))
    return print(lista1)

par_impar()

@tempo
def lista_ordenada(lista = [5,9,13,85,12,44, 125,1,0,8,65,96,47]):
    lista2 = list(sorted(lista))
    return print(lista2)

lista_ordenada()

@tempo
def aplica_raiz(lista = [25, 144, 69, 258, 248, 27, 63]):
    lista3 = list(map(lambda x:math.sqrt(x), lista))
    return print(lista3)

aplica_raiz()


def mul_for(list1 = [1,2,3], list2 = [4,5,6]):
    for i in list1:
        for j in list2:
            print(i, j)

mul_for()

