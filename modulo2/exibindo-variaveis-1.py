# Crie três variáveis, que armazenam respectivamente seu nome, idade e altura.
# Depois, exiba os valores armazenados, todos da mesma linha e separados por
# espaço.

nome = input("Digite o seu nome: ")
# idade também deve ser convertida para a unidade mais adequada, nesse caso,
# um número inteiro
idade = int(input("Digite a sua idade: "))
# Altura pode conter valores decimais, por esse motivo realizaremos a conversão
# para um valor do tipo float. Isso pode servir para futuros cáculos, já que 
# não se pode realizar cáculos com valores do tipo string.
altura = float(input("Digite a sua altura em metros(1.65, 1.90, etc): "))

print(nome, idade, altura)
