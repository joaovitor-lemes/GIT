
prod = [
{'prod' : 'arroz', 'preco' : 10.00},
{'prod' : 'feijao', 'preco' : 5.00},
{'prod' : 'carne', 'preco' : 20.00},
{'prod' : 'frango', 'preco' : 15.00},
{'prod' : 'leite', 'preco' : 3.00},
{'prod' : 'ovos', 'preco' : 2.00},
{'prod' : 'pao', 'preco' : 1.00},
{'prod' : 'manteiga', 'preco' : 4.00},
{'prod' : 'queijo', 'preco' : 6.00},
]

prod1 = prod.copy()

for value in prod1:
    value['preco'] = round(value['preco'] * 1.1,2)
    
print(*prod1, sep='\n', end='\n\n')

print('Lista Ordenada por preço')
print(sorted(prod1, key = lambda x: x['preco']), sep = '\n', end = '\n\n')

print('Lista ordenadda por nome')
print(sorted(prod1, key = lambda x:x['prod']), sep = '\n')