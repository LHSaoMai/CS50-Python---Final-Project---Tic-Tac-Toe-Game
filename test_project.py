from project import win, replace,  generate_random_number

board_game = ['[1][2][3]', '[4][5][6]' ,'[7][8][9]']
board_game_diagonale = ['[1][4][7]', '[2][5][8]' ,'[3][6][9]']
board_game_verticale = ['[1][5][9]', '[7][5][3]','']

def test_win_win():
    assert win(['[O][O][O]', '[4][5][6]' ,'[7][8][9]'],board_game_diagonale,board_game_verticale) == "WIN"
    assert win(board_game,['[O][O][O]', '[2][5][8]' ,'[3][6][9]'],board_game_verticale) == "WIN"
    assert win(board_game,board_game_diagonale,['[O][O][O]', '[7][5][3]','']) == "WIN"

def test_win_lose():
    assert win(['[X][X][X]', '[4][5][6]' ,'[7][8][9]'],board_game_diagonale,board_game_verticale) == "LOSE"
    assert win(board_game,['[X][X][X]', '[2][5][8]' ,'[3][6][9]'],board_game_verticale) == "LOSE"
    assert win(board_game,board_game_diagonale,['[0][0][0]', '[X][X][X]','']) == "LOSE"


def test_replace():
    new_board,new_board_d,new_board_v = replace(board_game,board_game_diagonale,board_game_verticale,2,9)

    check_board = ['[1][O][3]', '[4][5][6]' ,'[7][8][X]']
    check_board_d = ['[1][4][7]', '[O][5][8]' ,'[3][6][X]']
    check_board_v = ['[1][5][X]', '[7][5][3]','']

    assert new_board==check_board
    assert new_board_d==check_board_d
    assert new_board_v==check_board_v


def test_generate_random_number():
    assert generate_random_number([1,2,3,4,5,6,7,8])==9
    assert generate_random_number([1,2,3,5,6,7,8,9])==4
