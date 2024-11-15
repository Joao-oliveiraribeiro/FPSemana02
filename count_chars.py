frase = input()

palavras = frase.split()

contagemfrase = {}

for palavra in palavras:
    contagemfrase[palavra] = len(palavra)

print(contagemfrase)