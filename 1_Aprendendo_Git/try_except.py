#Exemplo Básico
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
except ValueError:
    print("Digite apenas números válidos!")

print(resultado)

# Usando o Else
try:
    x = int(input("Número: "))
except ValueError:
    print("Valor inválido!")
else:
    print(f"O dobro é {x*2}")

# Usando o Finally
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
finally:
    print("Operação concluída.")

# Usando o Raise

x = -1
if x<0:
    raise ValueError("Número negativo")
