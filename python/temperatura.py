temperatura = 0
celsius = 0
kelvin = 0 
fahrenheit = 0

temperatura = float(input("Qual a temperatura:\n"))
unidade = str(input("Em qual unidade de medida você deseja converter (C para Celsius, K para Kelvin, F para Fahrenheit) ?\n"))
unidade = unidade.upper()

if unidade == 'C':
    celsius = temperatura
    print("Temperatura em Celsius: ", celsius)
elif unidade == 'K':
    kelvin = temperatura + 273.15 
    print("Temperatura em Kelvin: ", kelvin)
elif unidade == 'F':
    fahrenheit = (temperatura * 9 / 5) + 32
    print("Temperatura em Fahrenheit: ", fahrenheit)
else:
    print("Unidade de temperatura inválida.")