from random import randint
board = [['.' for i in range(8)] for i in range(8)]
for x in range(8):
    for y in range(8):
        if randint(0,1) == 1:
            board[x][y] = '◉'
def print_board(board):
    print('  A B C D E F G H')
    for i in range(8):
        print(i+1,*board[i])

def change_board(board,a):
    alf = 'ABCDEFGH'
    if a in '12345678':
        for i in range(8):
            board[int(a)-1][i] = '.'
    elif a in alf:
        for i in range(8):
            board[i][alf.find(a)] = '.'

def game():
    print(
    '''
Добро пожаловать в игру "Супер ним" !
(для выхода из игры напишите "exit")
    '''
    )
    flag = 1
    print_board(board)
    print()
    player = 1
    alf = '123456789ABCDEFGH'
    alf = list(alf)
    while flag:
        if player%2 == 0: player = 2
        else: player = 1
        print('Игрок',player,'Введите букву или цифру (Например, 1 или A): ', end='')
        
        hod = input()
        print()
        if hod == '':
            print_board(board)
            print()
            print('Пожалуйста, введите ЗАГЛАВНУЮ букву или цифру от 1 до 8!')
            print()
        elif hod == 'exit':
            print('Игра окончена')
            print()
            return
        elif hod in alf:
            try: change_board(board,hod)
            except:return

            print_board(board)
            print()
            player+=1
            b = 0
            for i in board:
                for x in i:
                    if x =='.': b +=1
            if b == 64:flag = 0
        else:
            print_board(board)
            print()
            print('Пожалуйста, введите ЗАГЛАВНУЮ букву или цифру от 1 до 8!')
            print()
        

    print(f'''
⠄⠄⢀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣤⣤⣄⣀⠄⠄
⠄⠠⣿⢿⣿⢿⣯⣿⣽⢯⣟⡿⣽⢯⣿⣽⣯⣿⣽⣟⣟⣗⠄
⠄⢸⡻⠟⡚⡛⠚⠺⢟⣿⣗⣿⢽⡿⡻⠇⠓⠓⠓⠫⢷⢳⠄
⠄⢼⡺⡽⣟⡿⣿⣦⡀⡈⣫⣿⡏⠁⢀⣰⣾⢿⣟⢟⢮⢱⡀
⠄⣳⠑⠝⠌⠊⠃⠃⢏⢆⣺⣿⣧⢘⠎⠋⠊⠑⠨⠣⠑⣕⠂
⠄⢷⣿⣯⣦⣶⣶⣶⡶⡯⣿⣿⡯⣟⣶⣶⣶⣶⣦⣧⣷⣾⠄
⠄⢹⢻⢯⢟⣟⢿⢯⢿⡽⣯⣿⡯⣗⡿⡽⡯⣟⡯⣟⠯⡻⠂
⠄⠢⡑⡑⠝⠜⣑⣭⠻⢝⠿⡿⡯⠫⠯⣭⣊⠪⢊⠢⢑⠰⠁
⠄⠈⢹⣔⡘⢿⣿⣿⣶⠄⠁⠑⠈⠠⣵⣿⡿⡯⠂⣠⡞⡈⠄
⠄⠄⠨⢻⡆⢄⣀⢩⠄⠄⠴⠕⠄⠄⠈⠉⣀⠠⢢⡟⢌⠄⠄
⠄⠄⠈⠐⡝⣧⠈⡉⡙⢛⠛⠛⠛⠛⢋⠉⡀⡼⠩⡂⠁⠄⠄
⠄⠄⠄⠄⠈⠪⡻⣔⣮⣷⡆⠄⢰⣿⢦⣣⢞⠅⠁⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠈⠓⣷⣿⡅⠄⢸⣿⡗⠇⠁⠄⠄⠄⠄⠄⠄
''')

game()