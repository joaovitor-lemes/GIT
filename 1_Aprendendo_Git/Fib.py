def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Exemplo de uso:
termos = int(input("Digite o número de termos da sequência de Fib: "))
resultado = fibonacci(termos)
print("Sequência de Fibonacci:", resultado)







