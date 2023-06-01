# Exibindo os N primeiros termos da sequência de Fibonacci
N = int(input("Digite um número inteiro positivo: "))

# Essa lista armazenará todos os valores calculados, e servirá para 
# que possamos computar o valor dos números seguintes também. Como foi 
# informado pelo exercício, temos que os dois primeiros números da seqência
# são 0 e 1.
fibonacci = [0, 1]

# O laço de repetição é responsável por armazernar o novo número da sequência,
# que é obtido ao realizar a soma dos últimos dois termos, que podem ser encontrados
# na lista.
for i in range(2, N):
    termo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(termo)

# Mostrando os elementos da lista
for termo in fibonacci[:N]:
    print(termo, end=" ")

# Esse print resulta em uma quebra de linha ao fim do programa
print()
