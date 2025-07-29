#Soma 
soma = lambda x,y: x+y
print(soma(5,4))

#Constante 
const = lambda :50
print(const())

#Par ou Ímpar
e_par = lambda x: "par" if x%2 ==0 else "impar"
print(e_par(5833))

#Usando Map
num = [2,4,6,8]
quad = tuple(map(lambda x:x**2, num))
print(quad)

#Usando Filter
lista = [1,5,8,6,97,458,124]
pares = list(filter(lambda x:x%2==0, lista))
print(pares)

#Usando Sorted
nomes = ['joao', 'godofredo', 'alice']
ordenados = sorted(nomes, key = lambda nome: len(nome)) #Ordandando pelo tamanho da palavra
print(ordenados)

# Escreva um programa em Python para criar uma função lambda que adicione 15 a 
#um determinado número passado como argumento. Crie também uma função lambda que multiplique o argumento x pelo argumento y e imprima o resultado.

add15 = lambda x:x+15
mult = lambda x,y: x*y

print(add15(59), mult(9,2))

#Escreva um programa em Python para descobrir se uma determinada string começa com um determinado caractere usando Lambda.

determina = lambda x:True if str(x)[0] == "l" else False 
print(determina("lais"))

#Escreva um programa em Python para verificar se uma determinada string é um número ou não usando Lambda.

e_numero = lambda x: True if type(x) == int else False
print(e_numero(3))

