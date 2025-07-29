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