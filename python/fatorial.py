while True: # Estrutura de repetição
    entrada = input("Digite um número inteiro: ") # Entrada de dados

    if entrada.isdigit(): # Verifica se todos os caracteres na string entrada são dígitos (0 a 9) 
        numero = int(entrada) # Conferindo se os dados se trata de inteiros 
        if numero >= 0: # Conferindo se é maior que zero
            def fatorial(numero): # Função que recebe o dados tratado (numero)
                if numero == 0: # Se for igual a zero retorna 1
                    return 1
                else: # Caso contrario
                    return numero * fatorial(numero - 1) # Retornar resultado do calculo do fatorial
            # Mensagem formatada com o valor inserido e seu resultado
            print("O fatorial de {} é {}".format(numero, fatorial(numero))) 
            break  # Sair do loop se um número válido for fornecido
    else:
        print("Por favor, insira um número inteiro válido.") # Mensagem caso seja invalido

