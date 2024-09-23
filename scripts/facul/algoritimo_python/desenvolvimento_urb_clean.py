def calcular_area(largura, profundidade):
    return largura * profundidade

def obter_dados_terreno():
    largura = float(input('Largura em metros: '))
    profundidade = float(input('Profundidade em metros: '))
    return largura, profundidade

def verificar_normativas(p_ocup, terreno_loc):
    normativas = {
        "Zona Norte": 25,
        "Zona Leste": 30,
        "Zona Oeste": 30,
        "Zona Sul": 40
    }
    if terreno_loc in normativas and p_ocup <= normativas[terreno_loc]:
        return "O Projeto está de acordo com as normativas!"
    elif terreno_loc not in normativas:
        return "Você nem mora na cidade certa!"
    else:
        return "Infelizmente você não está seguindo os padrões!"

def main():
    print('Hello World!')
    nome = input('Digite seu nome: ')
    matricula = int(input('Digite sua matrícula: '))

    print("\n--- Dados da Garagem ---")
    largura_g, profundidade_g = obter_dados_terreno()
    area_g = calcular_area(largura_g, profundidade_g)
    print(f'A área da garagem é: {area_g:.2f} m²')

    print("\n--- Dados do Terreno ---")
    largura_t, profundidade_t = obter_dados_terreno()
    area_t = calcular_area(largura_t, profundidade_t)
    print(f'A área do terreno é: {area_t:.2f} m²')

    p_ocup = (area_g / area_t) * 100
    print(f'O percentual de ocupação do terreno é: {p_ocup:.2f}%')

    if p_ocup <= 40:
        terreno_loc = input("Localização do terreno: ")
        resultado = verificar_normativas(p_ocup, terreno_loc)
        print(resultado)
    else:
        print("Infelizmente você não está seguindo os padrões!")

if __name__ == "__main__":
    main()