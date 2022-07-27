from lib2to3.pgen2.literals import simple_escapes

def calculo_imc():
    
    seguir = ("s")

    while (seguir == "s"):
        print("USE '.' AO INVÉZ DE ',' OK?")
        peso = eval(input("Digite seu peso: "))
        altura = eval(input("Digite sua altura: "))
        imc = peso/altura**2
        if imc < 17:
            print("Tenha Cuidado, você está muito abaixo do peso!")
        elif imc >= 17 and imc <= 18.49:
            print("Atenção, você está abaixo do peso!")
        elif imc >= 18.50 and imc <= 24.99:
            print("PARABENS VOCÊ ESTÁ NO PESO IDEAL")
        elif imc >= 25 and imc <= 29.99:
            print("Atenção, você está acima do peso!")
        elif imc >= 30 and imc <= 34.99:
            print("Tenha Cuidado, você está com (obesidade) nível 1!")
        elif imc >= 35 and imc <= 39.99:
            print("Tenha Cuidado, você está com (obesidade severa)  ou seja nível 2!")
        elif imc >= 40:
            print("""Tenha Cuidado, você está com (obesidade mórbida)  ou seja nível 3! Já considerou procurar um nutricionista?""")  
        else:
            print("Então, o valor não foi identificado não!")
        seguir = input("Deseja Repetir?(s/n): ")
    else:
        print("Então amigo, até a próxima!")

resposta = input("Olá, tudo bom? Vamos calcular seu 'IMC'? ")
if resposta == "s":
    calculo_imc()

elif resposta == "sim":
    calculo_imc()

elif resposta == "Sim":
    calculo_imc()

elif resposta == "S":
    calculo_imc()

elif resposta == "Vamos":
    calculo_imc()

elif resposta == "vamos":
    calculo_imc()

else:
    print("Ok, então Tchau amigo!")
