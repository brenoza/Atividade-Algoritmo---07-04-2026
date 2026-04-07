import random


segredo = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("escreva um número entre 1 e 100: "))

    tentativas += 1
    if palpite < segredo:

        print("maior")
    elif palpite > segredo:
        print("menor")

    else:
        print("Acertou Tentativas:", tentativas)
        break


numeros = []
for i in range(8):
    n = int(input("escreva um número: "))
    numeros.append(n)

print("Números escritos:", numeros)

for n in set(numeros):
    qtd = numeros.count(n)
    
    if qtd > 1:
        print(n, "opa", qtd, "vezes")
