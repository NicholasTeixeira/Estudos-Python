from statistics import median


nota1 = eval(input('Primeira nota bimestra: '))
nota2 = eval(input('Segundaa nota bimestra: '))
nota3 = eval(input('Terceira nota bimestra: '))
nota4 = eval(input('Quartaa nota bimestra: '))

somanota = nota1 + nota2 + nota3 + nota4
media = somanota / 4

print(f'Sua média é {media} esse bimestre!')
