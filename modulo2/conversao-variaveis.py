variavel_1 = input("Primeira variável: ")
variavel_2 = input("Segunda variável: ")
variavel_3 = input("Terceira variável: ")
variavel_4 = input("Quarta variável: ")

print(f"Váriavel 1 -> Tipo: {type(variavel_1)}, Valor: {variavel_1}")
print(f"Váriavel 2 -> Tipo: {type(variavel_2)}, Valor: {variavel_2}")
print(f"Váriavel 3 -> Tipo: {type(variavel_3)}, Valor: {variavel_3}")
print(f"Váriavel 4 -> Tipo: {type(variavel_4)}, Valor: {variavel_4}")

variavel_1 = bool(variavel_1)
variavel_2 = float(variavel_1)
variavel_3 = int(variavel_1)

# A quarta váriavel não precisa ser convertida, já que toda entrada já
# se apresenta como do tipo string

# Pular uma linha
print()
print(f"Váriavel 1 -> Tipo: {type(variavel_1)}, Valor: {variavel_1}")
print(f"Váriavel 2 -> Tipo: {type(variavel_2)}, Valor: {variavel_2}")
print(f"Váriavel 3 -> Tipo: {type(variavel_3)}, Valor: {variavel_3}")
print(f"Váriavel 4 -> Tipo: {type(variavel_4)}, Valor: {variavel_4}")
