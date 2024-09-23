
num_primo = []
total = int(input("Insira um numero: "))
qtdenum = 0

#Estrutura que vai dizer quais são os números primos dentro do valor escolhido pelo usuário!
for numero in range (total):
    div = 0
    for divisor in range(1, numero + 1):
        if(numero % divisor) == 0:
            div += 1
    if div == 2:
        num_primo.append(numero)
print(num_primo)

#Estrutura que vai me dizer quantos números primos tem dentro do valor escolhido pelo usuário!
for char in num_primo:
    qtdenum += 1
print("dentro de {} se tem {} números primos" .format(str(total), str(qtdenum)))
