import math
# Tic-Tac-Toe

board = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]


######################### Global Var ########################
turn = 1
player = "x"
winner = ""

####################### Win cond. ###########################
def checkHorizontal(board):
  for row in board:
    if row[0] == row[1] == row[2]:
      return row[0]
  return

def checkVertical(board, y):
  if board[0][y] == board[1][y] == board[2][y]:
    return board[0][y]
  return


def checkDiagonal(board):
  if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
    return board[1][1]
  return

######################## Game Loop ##########################

while not winner and turn < 10:
  for row in board:
    print(row)
  if turn % 2 == 0:
    player = "O"
  else:
    player = "X"

  move = int(input(f"where do you want to place your {player}? "))

  #convert move into x, y coordinates
  y = (move % (len(board[0]))) - 1
  x = int(math.ceil(move / len(board[y])) - 1)

  if board[x][y] in ['X', 'O'] and board[x][y] not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("That spot is not available.")
  else:
    board[x][y] = player

    #check horiz.
    if checkHorizontal(board) or checkVertical(board, y) or checkDiagonal(board):
      winner = player
      print(f"{winner} wins!!!")
      for row in board:
        print(row)


    turn += 1

if not winner:
  print("Its a draw!!!")

