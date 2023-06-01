# Solicitar os valores de peso e altura para o primeiro usuário
nome1 = input("Digite o nome do primeiro usuário: ")
peso1 = float(input("Digite o peso (em kg) do primeiro usuário: "))
altura1 = float(input("Digite a altura (em metros) do primeiro usuário: "))

# Solicitar os valores de peso e altura para o segundo usuário
nome2 = input("Digite o nome do segundo usuário: ")
peso2 = float(input("Digite o peso (em kg) do segundo usuário: "))
altura2 = float(input("Digite a altura (em metros) do segundo usuário: "))

# Solicitar os valores de peso e altura para o terceiro usuário
nome3 = input("Digite o nome do terceiro usuário: ")
peso3 = float(input("Digite o peso (em kg) do terceiro usuário: "))
altura3 = float(input("Digite a altura (em metros) do terceiro usuário: "))

# Calcular o IMC de cada usuário
imc1 = peso1 / (altura1 ** 2)
imc2 = peso2 / (altura2 ** 2)
imc3 = peso3 / (altura3 ** 2)

# Imprimir os valores do IMC de cada usuário
print("O IMC do usuário", nome1, "é", imc1, "kg/m²")
print("O IMC do usuário", nome2, "é", imc2, "kg/m²")
print("O IMC do usuário", nome3, "é", imc3, "kg/m²")

