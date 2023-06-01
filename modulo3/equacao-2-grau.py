# Ler os coeficientes da equação
a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

# Calcular o valor do delta
delta = b**2 - 4*a*c

# Calcular as raízes da equação
raiz1 = (-b + (delta**0.5)) / (2*a)
raiz2 = (-b - (delta**0.5)) / (2*a)

# Imprimir as raízes
print("Raiz 1:", raiz1)
print("Raiz 2:", raiz2)

