nota_1 = int(input("Nota 1: "))
nota_2 = int(input("Nota 2: "))
nota_3 = int(input("Nota 3: "))

peso_1 = 0.3
peso_2 = 0.5
peso_3 = 0.2

media = ((nota_1 * peso_1) + (nota_2 * peso_2) + (nota_3 * peso_3)) / (peso_1 + peso_2 + peso_3)

print(media)
