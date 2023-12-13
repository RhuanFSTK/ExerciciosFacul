maior = 0
menor = 0
soma = 0

for i in range(1, 11):
    valor = float(input(f"Digite o {i}º valor:\n"))
    if i == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
    soma += valor
    
media = soma / 10

print("O maior valor é:", maior)
print("O menor valor é:", menor)
print("A média dos valores é:", media)
