## Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos

frutas = ['Maçã', 'Banana', 'Laranja']
print (frutas)
print(frutas[0])
print(f'Tamanho: {len(frutas)}')

frutas.append('Uva')
print(frutas)

frutas.insert(0, 'Abacaxi')
print(frutas)

#fruta = frutas.pop()
# print(f'Removido: {fruta}')
frutas.remove('Laranja')
print(frutas)

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numeros)

# Ordenar - crescente
numeros_ord_c = sorted(numeros)
print(f'Lista ordenada (c): {numeros_ord_c}')

# Ordenar - descrescente
numeros_ord_d = sorted(numeros, reverse=True)
print(f'Lista ordenada (d): {numeros_ord_d}')

# numeros_dobrados = []
# for n in numeros:
#   numeros_dobrados.append(n*2)
numeros_dobrados = list(map(lambda n: n*2, numeros))
print(numeros_dobrados)

# numeros_filtrados = {}
# for n in numeros:
#    if n > 4:
#        numeros_filtrados.append(n)
numeros_filtrados = list(filter(lambda n: n>4, numeros))
print(numeros_filtrados)

soma = 0
for n in numeros:
    soma += n
    print(soma)
# Reduzir isso para uma linha
from functools import reduce

soma = reduce(lambda soma, n: soma + n, numeros, 1)
print(soma)