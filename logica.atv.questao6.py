import os 
c:str
compra:float; cv:float; cp:float; ct:float
compra = 0
comprav = 0
comprap = 0

for n in range (1, 16):
    print(f"Dados da {n}ª venda.")
    c = input("Digite o código da compra (V - à vista ou P - a prazo): ").upper()
    if c == "V":
        compra = float(input("Digite o valor da compra: R$ "))
        comprav = comprav + compra
    elif c == "P":
        compra = float(input("Digite o valor da compra: R$ "))
        comprap = comprap + compra
    os.system("cls")

print(f"O valor total à vista: R$ {comprav:.2f}.")
print(f"O valor total a prazo: R$ {comprap:.2f}.")
print(f"O valor total das compras: R$ {comprap + comprav:.2f}.")
print(f"O valor total da primeira prestação das compras a prazo juntas: R$ {comprap/3:.2f}.")