import os

total_entrevistados = 0
user_android = 0
user_ios = 0
user_outros = 0
soma_idade = 0
data = 0
media_idade = 0
# Função para coletar dados de um entrevistado
def coleta():
    global total_entrevistados, user_ios, user_android, user_outros, soma_idade, data

    total_entrevistados += 1

    idade = int(input("Qual a sua idade? "))
    soma_idade += idade
    sistema = int(input("Responta com '1 ou '2'\n1)Android\n2)IOS\n- "))
    if sistema == 1:
        user_android += 1
    elif sistema == 2:
        user_ios += 1
    else:
        user_outros += 1

# Função para calcular a idade média
def idade_media(): 
    global media_idade
    if total_entrevistados == 0:
        return 0
    media_idade = float(soma_idade / total_entrevistados)

# Função para armazenar os dados do dia
def armazenar_dados():
    caminho_do_arquivo = os.path.join("D:/GitHub/estudos-python/scripts/facul/algoritimo_python/forum_de_algoritimos_e_lógica_de_programação/dados", "dados_da_pesquisa.txt")
    media_idade = idade_media()
    with open(caminho_do_arquivo, "a") as arquivo:
        arquivo.write(f"data: {data}\n")
        arquivo.write(f"Total de entrevistados: {total_entrevistados}\n")
        arquivo.write(f"Total de usuarios Android: {user_android}\n")
        arquivo.write(f"Total de usuarios IOS: {user_ios}\n")
        arquivo.write(f"Usuarios de outros Sistemas: {user_outros}\n")
        arquivo.write(f"Idade Media dos entrevistados: {media_idade}\n")
        arquivo.write(f"\n")

# Função para resetar os dados para o próximo dia
def resetar_dia():
    global total_entrevistados, user_android, user_ios, user_outros, soma_idade, data
    total_entrevistados = 0
    user_android = 0
    user_ios = 0
    user_outros = 0
    soma_idade = 0
    data = 0

#Execução
while True:

    coleta()
    continuar = input("Deseija continuar? (s/n)" ).strip().lower()
    if continuar != "s":
        dia = int(input("Que dia é hoje (Em numero!!): "))
        mes = int(input("em que mês estamos (Em numero!!): "))
        ano = int(input("Que em que ano estamos: "))
        data = ("{}.{}.{}" .format(str(dia), str(mes), str(ano)))
        print("Finalizando pesquisa!")
        break

armazenar_dados()
print("Resumindo:\n{} Usuários foram entrevistados\n{} Preferem usar Android.\n{} Preferem usar IOS.\n{} Usam algum outro tipo de sistema.\nA idade média dos entrevistados hoje foi de {}.\nOBRIGADO PELO SEU TEMPO!!".format(total_entrevistados, user_android, user_ios, user_outros, media_idade))
print("Dados Armazenados!")

resetar_dia()

print("Dados do dia armazenados e variáveis resetadas para o próximo dia.")