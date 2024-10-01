#Alannah Steck
#U2L3
#Tic Tac Toe
from tic_tac_toe import TicTacToe
from colorama import Fore
B = Fore.BLUE
W = Fore.RESET
G = Fore.GREEN

def rules(): #the rules, shockingly
  print(f"       {B}OXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX{W}")
  print("\t\t     Tic Tac Toe")
  print(f"       {B}OXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX{W}\n")
  print("\t\t\tRules\n")
  print("- You and the computer take turns placing tokens")
  print("- Your token must be placed in an empty spot")
  print("- Whoever gets 3 in a row (vertically, horizontally, or diagonally) first wins\n")
  input("\t\t  Press Enter To Start")

def keepPlayingCheck():
  keepPlaying = input("\tDo you want to keep playing?(yes/no) ")
  keepPlaying = keepPlaying.lower()
  while keepPlaying != "yes" and keepPlaying != "no":
    print("\tPlease type yes or no")
    keepPlaying = input("\tDo you want to keep playing?(yes/no) ")
    keepPlaying = keepPlaying.lower()
  if keepPlaying == "no":
    return True
  else:
    return False

def pickLocation(): #Let user pick spot and checks if input is valid
  row = input("     pick row (top, middle, bottom) : ")
  row = row.lower()
  while row != "top" and row != "middle" and row != "bottom":
    print("Please enter top, middle, or bottom when selecting a row.")
    row = input("     pick row (top, middle, bottom) : ")
    row = row.lower()

  column = input("     pick column (left, middle, right) : ")
  column = column.lower()
  while column != "left" and column != "middle" and column != "right":
    print("Please enter left, middle, or right when selecting a column.")
    column = input("     pick column (left, middle, right) : ")
    column = column.lower()
  
  if row == "top":
    row = 0
  elif row == "middle":
    row = 1
  else:
    row = 2

  if column == "left":
    column = 0
  elif column == "middle":
    column = 1
  else:
    column = 2

  return row, column


def main():
  rules()
  win = False
  game = TicTacToe()
  while win == False:
   print(game)
   row, column = pickLocation()
   print("\n")
   sucess, GameWon, WhoWon = game.place_token(row, column)
   if sucess == False: #checks if spot already has a token 
    if GameWon:
     output = game.is_winner()
     print(game)
     print(output)
     win = True
    print("\t\t\tThis spot already has a token in it. Please pick another spot.\n")
    row, column = pickLocation()
    print("\n")
    sucess, GameWon, WhoWon = game.place_token(row, column)
   if GameWon:
     output = game.is_winner()
     print(game)
     print(f"{G}{output}{W}")
     startAgain = keepPlayingCheck()
     game = TicTacToe()
     win = startAgain




if __name__ == "__main__":
  main()