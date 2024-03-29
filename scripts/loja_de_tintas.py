lata = 18
galao = 4
plata = 80
pgalao = 25

print ("Olá Vapt Blue!")
print ("Informe a baixo quantos m³ tem a área a ser pintada:")
area = int(input (' '))

litros = area // 6
if area % 6 > 0:
    litros = litros + 1

print ('Litros necessários: ', litros, '\n')

print ('1) Apenas latas de 18 Litros')
latas = litros // 18
if litros % lata > 0:
    latas = latas + 1
    

print ('Serão necessários', latas, "latas")
print ('Teremos', latas * 18, 'litros')
print ("Valor total de: R$", latas * 80)


print ('2) Apenas galões de 4 Litros')
galoes1 = litros // 4
if litros % galao > 0:
    galoes1 = galoes1 + 1
    



print ('Serão necessários', galoes1, "galões")
print ('Teremos', galoes1 * 4, 'litros')
print ("Valor total de: R$", galoes1 * 25)

print("\n3)Misturar latas e galões, de forma que o preço seja o menor.")
galoes = 0
litros_restantes = litros % 18
if litros_restantes <= 3 * 4:
    galoes = litros_restantes // 4
    if litros_restantes % 4 > 0:
        galoes += 1
else:
    latas += 1

print ('Serão necessárias ', latas, 'Latas')
print ('E Serão necessários ', galoes, 'Galões')
print ('Onteremos então ', latas * 18 + galoes * 4, 'Litros de tinta!')
print ('Custará: R$', galoes * 25 + latas * 80)
