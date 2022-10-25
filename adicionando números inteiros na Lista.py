lista1 = list()
while True:
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
    pergunta = " "
    while pergunta != "SN":
        pergunta = str(input('Quer continuar?\n[S] para SIM.\n[N] para NÃO.\n->')).strip().upper()
        if len(pergunta) == 0:
            print("ERRO.\nDigite uma resposta válida!\n[S] para SIM ou [N] para NÃO.")
        elif pergunta in "SN":
            break
        else:
            print("ERRO.\nDigite uma resposta válida!\n[S] para SIM ou [N] para NÃO.")
    if pergunta in 'N':
        break
lista1.sort()
print(lista1)
