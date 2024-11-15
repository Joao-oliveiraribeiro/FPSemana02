frase1 = input()
frase2 = input()

set1 = set(frase1.split())
set2 = set(frase2.split())

intersecao = set1 & set2

print(" ".join(intersecao))