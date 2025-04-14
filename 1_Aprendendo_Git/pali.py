def eh_palindromo(palavra):
    # Remove espaços e converte para minúsculas para comparação case-insensitive
    palavra = palavra.replace(" ", "").lower()
    # Compara a palavra com sua versão invertida
    return palavra == palavra[::-1]

# Exemplo de uso
entrada = input("Digite uma palavra ou frase para verificar se é palíndromo: ")
if eh_palindromo(entrada):
    print(f"'{entrada}' é um palíndromo!")
else:
    print(f"'{entrada}' não é um palíndromo.")