soma_idade_mulheres = 0
soma_altura_mulheres = 0
soma_idade_homens = 0
cont_idade_18_a_35 = 0
total_pessoas = 20

for i in range(1, total_pessoas + 1):
    sexo = int(input(f"Digite o sexo (0-feminino, 1-masculino) da {i}° pessoa:\n"))
    idade = int(input(f"Digite a idade da {i}° pessoa:\n"))
    altura_str = input(f"Digite a altura da {i}ª pessoa:\n")
    altura = float(altura_str.replace(',', '.'))

    if sexo == 0:
        soma_idade_mulheres += idade
        soma_altura_mulheres += altura
    else:
        soma_idade_homens += idade

    if 18 <= idade <= 35:
        cont_idade_18_a_35 += 1
 
media_idade_grupo = (soma_idade_mulheres + soma_idade_homens) / total_pessoas
media_altura_mulheres = soma_altura_mulheres / (total_pessoas / 2)
media_idade_homens = soma_idade_homens / (total_pessoas / 2)
percentual_idade_18_a_35 = (cont_idade_18_a_35 / total_pessoas) * 100

print("A média da idade do grupo é:", media_idade_grupo)
print("A média da altura das mulheres é:", media_altura_mulheres)
print("A média da idade dos homens é:", media_idade_homens)
print("O percentual de pessoas com idade entre 18 e 35 anos é:", percentual_idade_18_a_35, "%") 