entrada = input("Digite um número inteiro:\n")

if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
    numero = int(entrada)
    def fatorial(numero):
        if numero == 0:
            return 1
        else:
            return numero * fatorial(numero - 1)

    print("O fatorial de {} é {}".format(numero, fatorial(numero)))
else:
    print("Por favor, insira um número inteiro válido.")
    
