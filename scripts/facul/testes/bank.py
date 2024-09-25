import os

'''
nome = []
idade = []
saldo = []
'''
data = 0

contas = {}

def coleta_de_dados():
    #global nome, idade, saldo
    global contas
    
    cliente = input("Digite seu nome: ") 

    y = input("Digite sua idade: ")
    s = input("Digite seu saldo: ")

    contas2 = {cliente : {"Idade" : y, "Saldo" : s}}

    contas2[cliente] = (y, s)
    contas.update(contas2)
    print (contas)
    #contas2.

def armazenagem_de_dados():
    caminho_do_arquivo = os.path.join("D:/GitHub/estudos-python/scripts/facul/testes", "dados_do_cliente.txt")

    with open(caminho_do_arquivo, "a") as arquivo:
        arquivo.write(f"Data: {data}\n")
        arquivo.write(f"Usuários: {contas}\n")
        arquivo.write(f"\n")

def reset():
    global nome, idade, saldo, contas, data
    nome = 0
    idade = 0
    saldo = 0
    data = 0

while True:
    coleta_de_dados()

    go = input("Continuar cadastro? (S/N)").strip().lower()

    if go != "s":
        print("Finalizando cadastro de usuário!")
        dia = int(input("Que dia é hoje (Em numero!!): "))
        mes = int(input("em que mês estamos (Em numero!!): "))
        ano = int(input("Que em que ano estamos: "))
        data = ("{}.{}.{}" .format(str(dia), str(mes), str(ano)))
        break

armazenagem_de_dados()
reset()
print("Finalizando programa, Obrigado!")