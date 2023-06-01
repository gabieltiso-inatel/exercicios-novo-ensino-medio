# Calculando a soma dos elementos da diagonal principal de uma matriz
n = int(input("Digite a ordem da matriz quadrada: "))
matriz = []

# Recebendo a matriz do usuário
for _ in range(n):
    linha = input("Digite os elementos da linha separados por espaço: ")
    elementos = linha.split()

    linha_int = []
    for elemento in elementos:
        linha_int.append(int(elemento))

    matriz.append(linha_int)

# Calculando a soma da diagonal principal. Note que é possível realizar essa
# soma com apenas um laço for. Isso se deve ao fato de os elementos da diagonal 
# principal terem a seguinte característica: Seu índice de coluna é igual ao 
# seu índice de linha. Como exemplo, o primeiro item da diagonal pode ser 
# referenciado por "matriz[1][1]", o segundo por "matriz[2][2]", e assim por 
# diante.
soma = 0
for i in range(n):
    soma += matriz[i][i]

print("A soma dos elementos da diagonal principal é", soma)


