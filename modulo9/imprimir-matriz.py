# Criação de uma matriz em python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Existem algumas maneiras de iterar sobre os elementos de uma matriz em 
# Python, e esse é um deles. Basta criarmos dois laços for, sendo que um deles
# é responsável por iterar sobre todas as listas (o primeiro), e o outro é responsável
# por iterar sobre cada item dessa sublista (o segundo).
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()
