def calculadora_rank(vit, der):
    rank = vit - der

    if rank < 10:
        rank = "Ferro"
    elif 11 < rank <= 20:
        rank = "Bronze"
    elif 21 < rank <= 50:
        rank = "Prata"
    elif 51 < rank <= 80:
        rank = "Ouro"
    elif 81 < rank <= 90:
        rank = "Diamante"
    elif 91 < rank <= 100:
        rank = "Lendário"
    else:
        rank = "Imortal"

    
    print(f"O Herói tem saldo de {vit - der} e está no nível {rank}")

calculadora_rank(300, 50)