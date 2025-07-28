#quadrados = [i**2 for i in range(5)]
#print(quadrados)
#print("######################################")

#for numero in sorted([3, 1, 2]):
#    print(numero)

print("Encontre todas as palavras em uma sequência que tenham menos de 4 letras")
maiusc = [item.upper() for item in ["joao", "li", "maria", "leopoldo", "leoncio", "gertrudes"] if len(item) <=4]
print(maiusc,"\n")


div3 = [i for i in range(30) if i%3 ==0]
print(div3, "\n")

print("Produza uma lista contendo a palavra par se um número na lista for par, e a palavra ímpar se o número for ímpar ")
lista = [2,4,6,10, 15, 20, 25, 50, 63, 2587]
nova = ["par" if i % 2 ==0 else "impar" for i in lista]
print(nova, "\n")


print("Dada uma lista de números, remova todos os números ímpares da lista:")
lista1 = [1,6,7,9,10,15,24,56]
nova_lista1 = [number for number in lista1 if number %2 ==0]
print(nova_lista1, "\n")


print("Encontre todos os números de 1 a 1000 que são divisíveis por 7:")
nova_lista2 = [number for number in range(100) if number %7 ==0]
print(nova_lista2, "\n")


print("Encontre todos os números de 1 a 1000 que tenham um 3 neles:")
nova_lista3 = [number for number in range(100) if "3" in str(number) ]
print(nova_lista3, "\n")

print("Contar o número de espaços em uma string")
novalista4 = len([space for space in "agsdfjad hdfgkfksadk afkadafa sadfdafdf" if " " in space])
print(novalista4, "\n")

print("Obtenha apenas os números em uma frase")
frase = "Em 1984, houve 13 ocorrências de um protesto com mais de 1.000 pessoas presentes"
novalista5 = [num for num in frase if num.isnumeric()]
print(novalista5, "\n")

print("Use uma list Comprehension aninhada para encontrar todos os números de 1 a 1000 que são divisíveis por qualquer dígito único além de 1 (2 a 9)")
primos = [n for n in range(100) if all(n % d != 0 for d in range(2, int(n**0.5) + 1))]
print(primos)

