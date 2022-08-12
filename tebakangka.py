from random import randint
import os
game=0
win=0
lose=0
error=0
while True:
    try:
        os.system ('cls')
        print('TEBAK ANGKA [1 - 9]')
        print('------------------------------------')

        game+=1
        n=randint(1,10)

        for i in range(1,4):
            x=input(f'Angka tebak Anda [Percobaan - {i}] ? ' )
            if x.isnumeric:
                x=int(x)
                if x==n:
                    print('You WIN !!!')
                    print('------------------------------------')
                    win+=1
                    break
                elif x>n:
                    print('Tebakan Anda terlalu tinggi...')
                elif x<n:
                    print('Tebakan Anda terlalu rendah...')
        else:
            print('------------------------------------')
            print('Sorry, You LOSE...')
            lose+=1
    except Exception as e:
        print('Error :',e)
        error+=1
    finally:
        while True:
            jwb=input('\nContinue (y/n) ? ').lower()
            if jwb in ('y','n','yes','no'):
                break
            else:
                print('Input harus berupa y/n...')
        if jwb in ('n','no'):
            os.system('cls')
            print('Sumarry :')
            print('=========')
            print('Banyak Percobaan / Game =',game-error)
            print('Banyak Menang =',win)
            print('Banyak Kalah  =',lose)
            print('\n***** Thanks *****')
            break

