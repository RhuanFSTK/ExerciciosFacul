# Solicitar ao usuário que digite o valor presente
valor_presente = float(input("Digite o valor presente:\n"))

# Solicitar ao usuário que digite a taxa de juros por período (em decimal, use ponto como separador)
while True:
    taxa_juros_str = input("Digite a taxa de juros por período (em decimal, use ponto como separador):\n")
    
    # Verificar se a string inserida pode ser convertida para float
    try:
        taxa_juros = float(taxa_juros_str)
        break  # Se a conversão for bem-sucedida, sair do loop
    except ValueError:
        print("Por favor, insira um número decimal.")

# Solicitar ao usuário que digite o número de períodos
periodos = int(input("Digite o número de períodos:\n"))

# Calcular o valor futuro da aplicação usando a fórmula do valor presente
valor_futuro = valor_presente * (1 + taxa_juros) ** periodos

# Exibir o valor futuro calculado
print("O valor futuro da aplicação é:", valor_futuro)
