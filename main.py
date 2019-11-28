import random
while True:
    inpt = input('Сгенерировать число?(y/n)')
    if inpt == 'y':
        rnd_num = random.randint(0, 10)
        if rnd_num <= 5:
            print('Решка')
        elif rnd_num >= 5:
            print('Орел')
    else:
        break

    
