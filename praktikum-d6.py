import os
os.system('cls')

a = True

while a:
    jawab = input('Apakah Ingin Lanjutkan? (y/n)')
    if jawab == 'y':
        print('Terima Kasih')
        a = True
    elif jawab == 'n':
        print('sampai jumpa')
        a = False
    else:
        print('KAMU JANGAN MACAM MACAM YAAA')
        a = True

