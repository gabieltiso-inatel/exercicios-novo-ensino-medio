# Utilizamos o método lower para que todos os caracteres estejam em formato
# minúsculo. Isso ajudará na hora das comparações.
frase = str(input("Digite uma frase: ")).lower()

# Essa variável aponta para o primeiro caractere da frase
inicial = 0
# Essa variável aponta para o último caractere da frase
final = len(frase) - 1

# Essa variável, ao fim de toda a lógica, nos dirá se a frase é um palíndromo
# ou não.
palindromo = True

# Enquanto os ponteiros não se cruzarem, ou seja, inicial não pode ser
# maior que final(se isso acontecesse, estariamos iterando sobre items já
# analisados), continuaremos analisando os caracteres
while(inicial < final):
    # Ignorando espaços em branco, tanto no ponteiro final, quanto no inicial
    if frase[inicial] == " ":
        inicial += 1
        continue
  
    if frase[final] == " ":
        final -= 1
        continue
  
    # Se em algum momento tivermos caracteres diferentes nessa comparação,
    # podemos nos certificar que a frase não é um palíndromo.
    if frase[inicial] != frase[final]:
        palindromo = False
        break;
    
    # Não podemos nos esquecer de mover os ponteiros
    inicial += 1
    final -= 1
    
if palindromo:
  print("A frase é um palíndromo!")
else:
  print("A frase não é um palíndromo!")
