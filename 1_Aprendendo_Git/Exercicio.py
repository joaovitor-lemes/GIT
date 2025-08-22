'''
🚀 Desafio: Sistema de Cadastro e Análise de Notas

Você deverá criar um programa em Python que:
Use um while loop para permitir o cadastro de alunos e suas notas (nota de 0 a 10).
O usuário pode continuar cadastrando até digitar "sair".
Armazene os dados em uma lista de dicionários no seguinte formato:

{"nome": "João", "nota": 8}

Crie funções para:

media_notas(alunos): retorna a média das notas.
aprovados(alunos): retorna uma lista apenas com os nomes dos alunos aprovados (nota >= 7).
ranking(alunos): retorna uma lista de tuplas (nome, nota) ordenada da maior para a menor nota.
Use list comprehension em pelo menos uma das funções (exemplo: filtrar os aprovados).

'''

alunos_notas = {}

while True:
    aluno = input("Digite o nome do Aluno: | Digite sair para cancelar -> ")

    if aluno == "sair":
        break

    nota = int(input("Digite a nota do aluno: "))

    alunos_notas[aluno] = nota

print(alunos_notas)

def media(dict):
    soma = sum(alunos_notas.values())
    tamanho = len(alunos_notas.values())
    media = soma/tamanho
    return media


def aprovados(dict):
    lista =[]
    for nome, nota in alunos_notas.items():
        if nota >=7:
            lista.append(nome)
    return lista


def ranking(dict):
    rank = sorted(alunos_notas.items(), key= lambda item:item[1], reverse=True)
    return rank


    ...


print("A Média das notas é: ", media(alunos_notas)) # values é uma função, então precisa dos parênteses → values().
print("Os aprovados são: ", aprovados(alunos_notas))
print("O ranking de alunos é: ", ranking(alunos_notas))