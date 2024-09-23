print("Hello World")
'''
Apesar de o cauculo fatorial na matemática ser feito de forma decrescente, o código do python faz no formato boton up, pegando o valor menor e multiplicando pelo seguinte até chegar no número que o usuário deseja fatorar, correto?
'''
numero = int(input("Insira o número que deseja fatorar: "))

fatorial = 1 
for termo in range (1, (numero + 1)):
    fatorial *= termo
print("O fatorial de {} é: {}!" .format(str(numero), str(fatorial)))