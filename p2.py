n = int(input('Digite um número: '))
n1 = 0
n2 = 1
n3 = n1 + n2
lista = []
if n == 1 or n == 0:
    print('O número está na sequência.')
else:
    while True:
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        lista.append(n1)
        lista.append(n2)
        if n == n1:
            print('O número está na sequência.')
            break
        elif n1 > n:
            print('O número não estão na sequência.')
            break
