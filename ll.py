import random
while True:
    me = input('ввод')
    variant = ['камень','ножницы','бумага']
    ai = random.choice(variant)
    print(f'первый ход {me}, ответный ход {ai}')
    if me=='ножницы' and ai=='камень':
        print('Game Over')
    if me == 'ножницы' and ai == 'ножницы':
        print('Draw')
    if me == 'ножницы' and ai == 'бумага':
        print('You Win')
    if me == 'камень' and ai == 'камень':
        print('Draw')
    if me == 'камень' and ai == 'ножницы':
        print('You Win')
    if me == 'камень' and ai == 'бумага':
        print('Game Over')
    if me == 'бумага' and ai == 'камень':
        print('You Win')
    if me == 'бумага' and ai == 'ножницы':
        print('Game Over')
    if me == 'бумага' and ai == 'бумага':
        print('Draw')