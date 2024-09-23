print('Helo World!')
nome = str(input('Digite seu nome: '))
matricula = int(input('Digite sua matricula: '))

#Bloco A - Captura da metragem do terreno
largura_g = float(input('Largura da garagem em Metros: '))
profundidade_g = float(input('Profundidade da garagem em Metros: '))

area_g = largura_g*profundidade_g

print('A area da garagem é:{:.2f}' .format(area_g))

largura_t = float(input('Largura do terreno em Metros: '))
profundidade_t = float(input('Profundidade do terreno em Metros: '))

area_t = largura_t*profundidade_t

print('A area do terreno é:{:.2f}' .format(area_t))

p_ocup = area_g/area_t*100

print('O percentual de ocupação do terreno é: {:.2f}' .format(p_ocup))

#Bloco B - Está de acordo com as normativas?
if p_ocup <= 40:     

    ''' #Cauculo de porcentagem permitida
    zona_n = float(25 / area_t * 100)
    zona_l_o = float(30 / area_t * 100)
    zona_s = float(40 / area_t * 100)
    '''

    terreno_loc = str(input("Localização do terreno: "))

    if terreno_loc == "Zona Norte" or terreno_loc == "Zona Leste" or terreno_loc == "Zona Oeste" or terreno_loc == "Zona Sul":

        if terreno_loc == "Zona Norte" and p_ocup <=25:
            print("O Projeto está de acordo com as normativas!")

        elif terreno_loc == "Zona Leste" or terreno_loc == "Zona Oeste"and p_ocup <=30:
            print("O Projeto está de acordo com as normativas!")
        elif terreno_loc == "Zona Sul"and p_ocup <=40:
            print("O Projeto está de acordo com as normativas!")

    else:
        print("Você nem mora na cidade certa!")

else:
    print("Infelizmente você não está seguindo os padrões!")

