precoIng:float
despesas:float
lucro:float
quantidadeIng:int

precoIng = 5.00
quantidadeIng = 120
despesas = 200.00

while precoIng >= 1.00:
    lucro = quantidadeIng * precoIng - despesas
    print(f"|Preço: \t\t|R$ {precoIng:.2f}")
    print(f"|Lucro: \t\t|R$ {lucro:.2f}")
    print(f"|Ingressos Vendidos: \t|{quantidadeIng}")
    print("-------------------------------------")
    quantidadeIng = quantidadeIng + 26
    precoIng = precoIng - 0.50
