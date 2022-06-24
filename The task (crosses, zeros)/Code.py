from random import choice, randint
def draw_board_lite(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
def player_input_my():
    inp = input('Выберите сторону "Х" или "0" или нажмите Enter для случайного выбора : ') or choice(['x', 'o'])
    while inp != '':
        if inp in 'ХхЧчXx{[':
            return ('X','O')
        elif inp in 'ОоЩщOoJj0':
            return  ('O', 'X')
        else:
            inp = input('Вы ввели не корректное значение, выберите "Х" или "0": ') or choice(['x', 'o'])
 
def place_marker(board, marker, position):
    board[position] = marker
 
def win_check(board, mark):
     return  ((board[7] == mark and board[8] == mark and board[9] == mark) or
              (board[4] == mark and board[5] == mark and board[6] == mark) or
              (board[1] == mark and board[2] == mark and board[3] == mark) or
              (board[7] == mark and board[4] == mark and board[1] == mark) or
              (board[8] == mark and board[5] == mark and board[2] == mark) or
              (board[9] == mark and board[6] == mark and board[3] == mark) or
              (board[1] == mark and board[5] == mark and board[9] == mark) or
              (board[7] == mark and board[5] == mark and board[3] == mark))
 
def space_check(board, position):
    return board[position] == ' '
 
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True
def player_choose(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Выберите позицию клетку: ')
    return int(position)
def replace():
    return input('Сыграть еще ? введите: "YES" или "NO" :').upper() in 'YES Y НУЫ Н '.split()
 
print('Игра крестики нолики')
while True:
     theBoard = [' '] * 10
     player1_marker, player2_marker = player_input_my()
     print(player1_marker + ' ходит первым')
     game_on = True
     while game_on:
             draw_board_lite(theBoard)
             position = player_choose(theBoard)
             place_marker(theBoard, player1_marker, position)
             if win_check(theBoard, player1_marker):
                draw_board_lite(theBoard)
                print('Победа за ' + player1_marker)
                game_on = False
             else:
                if full_board_check(theBoard):
                    draw_board_lite(theBoard)
                    print('Ничья')
                    break
                else:
                    draw_board_lite(theBoard)
                    position = player_choose(theBoard)
                    place_marker(theBoard, player2_marker, position)
                    if win_check(theBoard, player2_marker):
                        draw_board_lite(theBoard)
                        print('Победа за ' + player2_marker)
                        game_on = False
 
     if not replace():
         break