lista1 = list()
pergunta = ""
while pergunta in "S":
    while True:
        try:
            n = int(input("Digite o VALOR:"))
            break
        except ValueError:
            print("ERRO.\nDigite um VALOR NUMÉRICO INTEIRO.")
    if n not in lista1:
        lista1.append(n)
    elif n in lista1:
        print("Esse número já está na lista...\nDIGITE OUTRO.")
    while True:
        pergunta = input('Quer continuar?\n[S] para SIM.\n[N] para NÃO.\n->').strip().upper()
        if len(pergunta) == 0:
            print("ERRO.\nDigite [S] para SIM e [N] para NÃO.")
        elif pergunta in "SN":
            break
        else:
            print("Resposta inválida.")
lista1.sort()
print(lista1)
