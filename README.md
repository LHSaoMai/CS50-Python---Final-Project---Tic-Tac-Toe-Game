# CS50P Project - TIC-TAC-TOE GAME
#### Video Demo:  https://youtu.be/7C-HMG_UFEk
#### Description:
This is a basic tic tac toe game where the player plays against the computer. This game comes with a "new design": the player doesn't need to choose the row and the column to play. He just need to choose the number.

![Tic tac toe game](/project/tic tact toe.png)

## Folder Contents
- **project.py**: File which contains the ```main``` function and the other functions necessary to implement the game.
- **requirements.txt**: List of All ```pip```-installable libraries that are used for this project.
- **test_project.py**: All the tests functions for project.py.


## Game Mechanism
- You always begin and you play against the computer. Everyone plays in turn.
- To win, you need to have a full row, column, or diagonal line of your symbol.


## Documentation

```python
def main():
```
**Description:**
- This function is the root function. It takes all the others functions in order to play the game.
- At the end of the game, it will return a ``str```: "Sorry, you lose". "Congrat, you win", or "No winner".
- It also handle errors. When the user types a wrong command (ex: not a number available to play), the command line will return a ``str``: 'Not available position'


```python
def win(board_play,board_col,board_dig):
```

**Args:**
- ```board_play``` (```list```): the board game (that is display to the player)
- ```board_col``` (```list```): the board that check all the columns
- ```board_dig``` (```list```): the board that check all the diagonals


**Description:**
- This function return a ``str`` 'WIN' or 'LOSE'.
- If the player has a full row, column, or diagonal line of his symbol, the function return 'WIN', or conversely if it is the machine, the function return 'LOSE'



```python
def replace(board_game, board_game_diagonale, board_game_verticale, position, computer_position)
```
**Args:**
- ```board_game``` (```list```): the board game (that is display to the player)
- ```board_game_diagonale``` (```list```): the board that check all the columns
- ```board_game_verticale``` (```list```): the board that check all the diagonals
- ```position``` (```int```): the position that the player chooses to play
- ```computer_position``` (```int```): the position that the cpmputer chooses to play


**Description:**
- This function returns a ``list`` the board game
- This function is use to replace all the boards the position that the computer or the player choose to play


```python
def generate_random_number(list_exception)
```

**Args:**
- ```list_exception``` (```list```): list of all the position that were already played by the player and the computer

**Description:**
- This function generates a random number that will be the position that the computer plays
- It generates a random number that is not a position that was already played

## Design choice
- The design was to have a boardgame were the player directly choses a position without given the first the row and after the column
- Secondly, the esthetic design was to display a game board like this, therefore this add complexity because it was a list od string. To get the position and draw it in the boardgame was done with replacing str and not with index as the whole board game was in str by design.
