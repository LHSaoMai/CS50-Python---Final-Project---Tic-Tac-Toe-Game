import random
import re
################### Tik Tak Tok Game ###########################

def main():
    board_game = ['[1][2][3]', '[4][5][6]' ,'[7][8][9]']
    board_game_diagonale = ['[1][4][7]', '[2][5][8]' ,'[3][6][9]']
    board_game_verticale = ['[1][5][9]', '[7][5][3]','']
    [print(board_game[i]) for i in range(3)]
    already_play= []

    while True:
        try:
            if len(already_play)<8:
                    position = int(input("please choose a position "))
                    if 1<=position<=9 and (position not in already_play):
                        already_play.append(position)
                        number = generate_random_number(already_play)
                        replace(board_game, board_game_diagonale, board_game_verticale, position, number)
                        [print(board_game[i]) for i in range(3)]
                        if  win(board_game,board_game_diagonale,board_game_verticale) == 'WIN':
                                print('Congrat, you win')
                                break
                        elif win(board_game,board_game_diagonale,board_game_verticale) == 'LOSE':
                                print('Sorry, you lose')
                                break
                    else:
                        print('Not available position')
                        continue
            elif len(already_play)==8:
                    position = int(input("please choose a position "))
                    if 1<=position<=9 and (position not in already_play):
                        replace(board_game, board_game_diagonale, board_game_verticale, position, number)
                        [print(board_game[i]) for i in range(3)]
                        [print('Congrat, you win') if win(board_game, board_game_diagonale, board_game_verticale) == 'WIN' else print('No Winner')]
                        break

        except ValueError:
            print('Not available position')
            pass


def win(board_play,board_col,board_dig):

    for _ in range(3):
        if len(re.findall("O", board_play[_]))==3 or len(re.findall("O", board_col[_]))==3 or len( re.findall("O", board_dig[_]))==3:
              return "WIN"
        elif  len(re.findall("X", board_play[_]))==3 or len(re.findall("X", board_col[_]))==3 or len( re.findall("X", board_dig[_]))==3:
             return "LOSE"

def replace(board_game, board_game_diagonale, board_game_verticale, position, computer_position='NA'):

    for _ in range(3):
        board_game_diagonale[_] = board_game_diagonale[_].replace(str(position), 'O')
        board_game_diagonale[_] = board_game_diagonale[_].replace(str(computer_position), 'X')
        board_game[_] = board_game[_].replace(str(position), 'O')
        board_game[_] = board_game[_].replace(str(computer_position), 'X')
        board_game_verticale[_] = board_game_verticale[_].replace(str(position), 'O')
        board_game_verticale[_] = board_game_verticale[_].replace(str(computer_position), 'X')

    return board_game, board_game_diagonale, board_game_verticale


def generate_random_number(list_exception):
    while True:
        if len(list_exception)<9:
            n = random.randint(1,9)
            if n not in list_exception:
                list_exception.append(n)
                return n
        else:
            break

if __name__ == "__main__":
    main()
