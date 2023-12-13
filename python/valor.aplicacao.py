valor_presente = float(input("Digite o valor presente:\n"))
taxa_juros_str = (input("Digite a taxa de juros por período (em decimal):\n"))
taxa_juros = float(taxa_juros_str.replace(',', '.'))
periodos = int(input("Digite o número de períodos:\n"))

valor_futuro = valor_presente * (1 + taxa_juros) ** periodos

print("O valor futuro da aplicação é:", valor_futuro)
