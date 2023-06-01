# Calculando a soma dos dígitos de um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))
soma = 0

# Convertendo o número em uma string para iterar sobre os dígitos
for digito in str(numero):
    soma += int(digito)

print("A soma dos dígitos é", soma)
