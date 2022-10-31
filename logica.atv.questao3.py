faixa1:int
faixa2:int
faixa3:int
faixa4:int
faixa5:int
idade:int

faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for n in range(1, 9):
    idade = int(input("Digite a sua idade: "))

    if idade <= 15:
        faixa1 = faixa1 + 1
    elif idade > 15 and idade <= 30:
        faixa2 = faixa2 + 1
    elif idade > 30 and idade <= 45:
        faixa3 = faixa3 + 1
    elif idade > 45 and idade <= 60:
        faixa2 = faixa2 + 1
    else:
        faixa5 = faixa5 + 1

print(f"Faixa etária 01 (até 15 anos): {faixa1}.")
print(f"Faixa etária 02 (até 30 anos): {faixa2}.")
print(f"Faixa etária 03 (até 45 anos): {faixa3}.")
print(f"Faixa etária 04 (até 60 anos): {faixa4}.")
print(f"Faixa etária 05 (acima de 60 anos): {faixa5}.")

print(f"A porcentagem de pessoas {faixa1/8*100}%")