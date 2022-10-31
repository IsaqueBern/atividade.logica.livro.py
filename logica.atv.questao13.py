idade:int
peso:float

mediaPesosFaixa1a10:float
mediaPesosFaixa11a20:float
mediaPesosFaixa21a30:float
mediaPesosFaixa31Acima:float

somaPesosFaixa1a10:float
somaPesosFaixa11a20:float
somaPesosFaixa21a30:float
somaPesosFaixa31Acima:float

qtdPesosFaixa1a10:float
qtdPesosFaixa11a20:float
qtdPesosFaixa21a30:float
qtdPesosFaixa31Acima:float

mediaPesosFaixa1a10 = 0
mediaPesosFaixa11a20 = 0
mediaPesosFaixa21a30 = 0
mediaPesosFaixa31Acima = 0

somaPesosFaixa1a10 = 0
somaPesosFaixa11a20 = 0
somaPesosFaixa21a30 = 0
somaPesosFaixa31Acima = 0

qtdPesosFaixa1a10 = 0
qtdPesosFaixa11a20 = 0
qtdPesosFaixa21a30 = 0
qtdPesosFaixa31Acima = 0

for n in range(1, 16):
    idade = int(input("Informe sua idade: "))
    peso = float(input("Informe seu peso: "))

    if idade >= 1 and idade <= 10:
        somaPesosFaixa1a10 += peso
        qtdPesosFaixa1a10 += 1

    if idade >= 11 and idade <= 20:
        somaPesosFaixa11a20 += peso
        qtdPesosFaixa11a20 += 1

    if idade >= 21 and idade <= 30:
        somaPesosFaixa21a30 += peso
        qtdPesosFaixa21a30 += 1

    if idade >= 31:
        somaPesosFaixa31Acima += peso
        qtdPesosFaixa31Acima += 1

if qtdPesosFaixa1a10 > 0:
    mediaPesosFaixa1a10 = somaPesosFaixa1a10 / qtdPesosFaixa1a10
    print(" Faixa etária média de 1 a 10 anos: ", mediaPesosFaixa1a10)
else:
    print("Não houve idade na faixa etária entre 1 a 10 anos!")

if qtdPesosFaixa11a20 > 0:
    mediaPesosFaixa11a20 = somaPesosFaixa11a20 / qtdPesosFaixa11a20
    print("Faixa etária média de 11 a 20 anos: ", mediaPesosFaixa11a20)
else:
    print("Não houve idade na faixa etária entre 11 a 20 anos!")

if qtdPesosFaixa21a30 > 0:
    mediaPesosFaixa21a30 = somaPesosFaixa21a30 / qtdPesosFaixa21a30
    print("Faixa etária média de 21 a 30 anos: ", mediaPesosFaixa21a30)
else:
    print("Não houve idade na faixa etária entre 21 a 30 anos!")

if qtdPesosFaixa31Acima > 0:
    mediaPesosFaixa31Acima = somaPesosFaixa31Acima / qtdPesosFaixa31Acima
    print("Faixa etária média acima de 31 anos : ", mediaPesosFaixa31Acima)
else:
    print("Não houve idade na faixa etária acima de 31 anos!")
