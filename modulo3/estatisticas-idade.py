# Ler o ano de nascimento
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Ler o ano atual
ano_atual = int(input("Digite o ano atual: "))

# Calcular a idade da pessoa
idade = ano_atual - ano_nascimento
print("Idade:", idade)

# Calcular o ano em que a pessoa completará 100 anos de vida
ano_100_anos = ano_nascimento + 100
print("Ano em que completará 100 anos:", ano_100_anos)

# Calcular quantos meses a pessoa já viveu
meses_vividos = idade * 12
print("Meses vividos:", meses_vividos)

# Calcular o século em que a pessoa nasceu
seculo_nascimento = (ano_nascimento // 100) + 1
print("Século de nascimento:", seculo_nascimento)

# Calcular a idade da pessoa ao quadrado
idade_ao_quadrado = idade ** 2
print("Idade ao quadrado:", idade_ao_quadrado)

