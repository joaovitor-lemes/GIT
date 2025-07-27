quadrados = [i**2 for i in range(5)]
print(quadrados)
print("######################################")
for numero in sorted([3, 1, 2]):
    print(numero)

print("######################################")
maiusc = [item.upper() for item in ["joao", "li", "maria", "leopoldo", "leoncio", "gertrudes"] if len(item) >4]
print(maiusc)
print("######################################")
div3 = [i for i in range(30) if i%3 ==0]
print(div3)

print("######################################")
lista = [2,4,6,10, 15, 20, 25, 50, 63, 2587]

nova = ["par" if i % 2 ==0 else "impar" for i in lista]
print(nova)