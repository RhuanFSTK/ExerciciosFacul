# Declaração de variaveis
total_pessoas = 20  # Substitua pelo valor desejado
soma_idade_mulheres = 0
soma_altura_mulheres = 0
soma_idade_homens = 0
cont_idade_18_a_35 = 0

for i in range(1, total_pessoas + 1):
    # Verifica o sexo da pessoa
    sexo_valido = False # reiniciando varioavel de controle
    while not sexo_valido:
        try:
            sexo = int(input(f"Digite o sexo (0 -> feminino, 1 -> masculino) da {i}° pessoa:\n")) # Entrada de dados
            if sexo == 0 or sexo == 1:
                sexo_valido = True
            else:
                print("Insira um valor válido (0 para feminino, 1 para masculino)") # Retorno de erro
        except ValueError:
            print("Insira um valor válido (0 para feminino, 1 para masculino)") # Retorno de erro

    # Verifica a idade da pessoa
    idade_valida = False # reiniciando varioavel de controle
    while not idade_valida:
        try:
            idade = int(input(f"Digite a idade da {i}° pessoa:\n")) # Entrada de dados
            idade_valida = True
        except ValueError:
            print("Insira uma idade válida (número inteiro)") # Retorno de erro

    # Verifica a altura da pessoa
    altura_valida = False # reiniciando varioavel de controle
    while not altura_valida:
        altura_str = input(f"Digite a altura da {i}° pessoa:\n") # Entrada de dados

        if altura_str.isdigit():
            try:
                altura = int(altura_str) / 100.0  # Se a altura for um número inteiro, converte para float dividido por 100.0
                altura_valida = True
                print(altura)
            except ValueError:
                print("Insira uma altura válida (número válido representando centímetros)") # Retorno de erro
        elif ',' in altura_str:
            try:
                altura = float(altura_str.replace(',', '.')) # Se a altura for float com virgula, converte para float com ponto
                altura_valida = True
            except ValueError:
                print("Insira uma altura válida (número válido representando centímetros)") # Retorno de erro
        elif '.' in altura_str:
            try:
                altura = float(altura_str) # Se a altura for inserida como decimal somente confirmar se esta com ponto
                altura_valida = True
            except ValueError:
                print("Insira uma altura válida (número válido representando centímetros)") # Retorno de erro
        else:
            print("Insira uma altura válida (número inteiro ou decimal representando centímetros)") # Retorno de erro

        if sexo == 0:  # Se for mulher, atualiza as variáveis de soma para mulheres
            soma_idade_mulheres += idade
            soma_altura_mulheres += altura
        else:  # Se for homem, atualiza a variável de soma para homens
            soma_idade_homens += idade

        if 18 <= idade <= 35:  # Condição - Se for entre 18 e 35 anos caso esteja executar bloco
            cont_idade_18_a_35 += 1
                
# Calculos
media_idade_grupo = (soma_idade_mulheres + soma_idade_homens) / total_pessoas
media_altura_mulheres = soma_altura_mulheres / (total_pessoas // 2)  
media_idade_homens = soma_idade_homens / (total_pessoas // 2) 
percentual_idade_18_a_35 = (cont_idade_18_a_35 / total_pessoas) * 100


# Apresentação de dados na tela
print("A média da idade do grupo é:", media_idade_grupo)
print("A média da altura das mulheres é:", media_altura_mulheres)
print("A média da idade dos homens é:", media_idade_homens)
print("O percentual de pessoas com idade entre 18 e 35 anos é:", percentual_idade_18_a_35, "%")
