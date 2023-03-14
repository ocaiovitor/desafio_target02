n = 10

n1 = 0
n2 = 1
n3 = n1 + n2

print('{} - {}'.format(n1, n2), end='')

contador = 3

while contador <= n:
    n3 = n1 + n2
    print(' - {}'.format(n3), end='')
    
    n1 = n2
    n2 = n3

    contador += 1
