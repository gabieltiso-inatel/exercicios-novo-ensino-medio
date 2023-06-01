lista_numeros = []

# Esse loop é responsável por exigir os 5 números como entrada. Os números 
# são armazenados na lista de números para que possamos procurar o número 
# desejado mais tarde. O símbolo "_" na declaração do loop diz ao Python que
# o valor da váriavel oriunda da função range não terá utilidade para nós, ou
# seja, ele será ignorado.
for _ in range(0, 5):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)

numero_desejado = int(input("Qual número você deseja procurar: "))

# Se esse valor permanecer -1 mesmo após o fim deste próximo loop
# significa que o número não foi encontrado na lista, já que essa estrutura
# não suporta índices negativos.
posicao_item = -1

for i in range(0, len(lista_numeros)):
    # Se o item na posição i for igual ao número desejado,
    # queremos que seu índice seja armazenado na variável posicao_item,
    # para que possamos imprimi-lo no final
    if lista_numeros[i] == numero_desejado:
        posicao_item = i
        break

if posicao_item != -1:
    print(f"O item foi encontrado na posição {posicao_item}")
else:
    print("O item não foi encontrado")

