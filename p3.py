lista = []
diario = []
maior = 0
menor = 0
total = 0
while True:
    print('Digite 999 em dia para parar.')
    dia = input('DIA: ').strip()
    if dia == '999':
        break
    valor = float(input('VALOR: '))
    total += valor
    diario.append(dia)
    diario.append(valor)
    lista.append(diario[:])
    diario.clear()
    if maior == 0:
        maior = valor
    else:
        if valor > maior:
            maior = valor
    if menor == 0:
        menor = valor
    else:
        if valor < menor:
            menor = valor
print(lista)
print(f'O MAIOR faturamento foi {maior}.')
print(f'O MENOR faturamento foi {menor}.')
media = total / len(lista)
print(media)
for c in lista[]:
    print(c)
