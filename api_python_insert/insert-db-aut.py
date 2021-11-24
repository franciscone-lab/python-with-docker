from random import randint
import time
from connectdb import *

print('='*10, 'INÍCIO DAS MEDIÇÕES', '='*10)
print('-'*10, 'Ctrl+C para parar', '-'*10, '\n')

try:
    acao = 0
    print('*-----------------------------------------*')
    print('*---------------HOME BROKER---------------*')
    print('*-----------------------------------------*')
    print('*-----------AÇÃO: ITSA4 (Itaúsa)----------*')
    print('*-----------------------------------------*')
    while True:
        acao = randint(1, 10)
        print('*-----------------------------------------*')
        print(f'*-------------COTAÇÃO ATUAL:R${acao}-----------*')
        print('*-----------------------------------------*')
        time.sleep(5)
        insert_db(acao)


except KeyboardInterrupt:
    pass
