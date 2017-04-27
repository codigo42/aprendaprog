# coding: utf-8

import random
import math

def pede_int(msg):
    while True:
        resp = input(msg)
        try:
            resp = int(resp)
        except ValueError:
            print('Digite apenas dígitos')
        else:
            break
    return resp

# programa principal
maximo = 100

chances = math.ceil(math.log(maximo, 2))
nosso_numero = random.randint(1, maximo)

print('Chute um número de 1 a %s.' % maximo)
print('Você tem %s chances de acertar.' % chances)

chute = 1

while chute <= chances:
    resp = pede_int('[%d] ' % chute)
    if resp == nosso_numero:
        print('Acertou!')
        break
    elif resp > nosso_numero:
        print('Muito alto...')
    else:
        print('Muito baixo...')
    chute += 1
else:
    print('Game over')
