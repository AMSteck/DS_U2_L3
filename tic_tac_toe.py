from random import randint
from colorama import Fore
B = Fore.BLUE
W = Fore.RESET


class TicTacToe:
  def __init__(self): 
    self.__board = [[" "]*3 for time in range(3)]
    self.__turn = randint(1,2) #1 = player, 2 = computer
  
  def __str__(self): #board :D
    output  = ""
    output+= f"\t\t{B}=======================\n"
    output+= "\t\t||     ||     ||     ||\n"
    output+= f"\t\t||  {W}{self.__board[0][0]}{B}  ||  {W}{self.__board[0][1]}{B}  ||  {W}{self.__board[0][2]}{B}  ||\n"
    output+= "\t\t||     ||     ||     ||\n"
    output+= "\t\t=======================\n"
    output+= "\t\t||     ||     ||     ||\n"
    output+= f"\t\t||  {W}{self.__board[1][0]}{B}  ||  {W}{self.__board[1][1]}{B}  ||  {W}{self.__board[1][2]}{B}  ||\n"
    output+= "\t\t||     ||     ||     ||\n"
    output+= "\t\t=======================\n"
    output+= "\t\t||     ||     ||     ||\n"
    output+= f"\t\t||  {W}{self.__board[2][0]}{B}  ||  {W}{self.__board[2][1]}{B}  ||  {W}{self.__board[2][2]}{B}  ||\n"
    output+= "\t\t||     ||     ||     ||\n"
    output+= f"\t\t======================={W}\n"
    return output

  def place_token(self, row, column): #Places player token, checks if spot is taken, places computer token, calls __check_win
    if self.__board[row][column] == " ":
      if self.__turn == 1:
       self.__board[row][column] = "O"
      else:
       self.__board[row][column] = "X" 
      GameWon, WhoWon = self.__check_win()
      if GameWon == True:
        return True, GameWon, WhoWon
      emptySpots = False
      for row in self.__board:
        for spot in row:
          if spot == " ":
            emptySpots = True
      if emptySpots == True:
        moveMade = False
        while moveMade == False:
         row = randint(0,2)
         column = randint(0,2)
         if self.__board[row][column] == " ":
           if self.__turn == 1:
             moveMade = True
             self.__board[row][column] = "X"
           else:
             moveMade = True
             self.__board[row][column] = "O"
         else:
            moveMade = False
      GameWon, WhoWon = self.__check_win()
 
      return True, GameWon, WhoWon
    else:
      GameWon, WhoWon = self.__check_win()
      return False, GameWon, WhoWon
  
  def __check_win(self): #checks win 
    GameWon = False
    WhoWon = None

    for row in self.__board: #check rows for win
      X = 0
      O = 0
      for spot in row:
        if spot == "O":
          O += 1
        elif spot == "X":
          X += 1
      if O == 3:
        WhoWon = "O won"
        GameWon = True
      elif X == 3:
        WhoWon = "X won"
        GameWon = True

    for column in range(3): #check columns for win
      X = 0
      O = 0
      for row in range(3):
        if self.__board[row][column] == "O":
          O += 1
        elif self.__board[row][column] == "X":
          X += 1
      if O == 3:
        WhoWon = "O won"
        GameWon = True
      elif X == 3:
        WhoWon = "X won"
        GameWon = True

    X = 0 #checks diagonal
    O = 0
    numTwo = 2
    for number in range(3):
     if self.__board[number][numTwo] == "O":
        O += 1
     elif self.__board[number][numTwo] == "X":
        X += 1
     numTwo -= 1
    if O == 3:
      WhoWon = "O won"
      GameWon = True
    elif X == 3:
      WhoWon = "X won"
      GameWon = True

    X = 0 #chceks other diagonal
    O = 0
    for spot in range(3):
     if self.__board[spot][spot] == "O":
        O += 1
     elif self.__board[spot][spot] == "X":
        X += 1
    if O == 3:
      WhoWon = "O won"
      GameWon = True
    elif X == 3:
      WhoWon = "X won"
      GameWon = True
        
    spotsFull = True #check 4 draw // DO LAST
    for row in self.__board:
      for spot in row:
        if spot == " ":
          spotsFull = False
    if spotsFull == True and GameWon == False:
      WhoWon = "It's A Draw"
      GameWon = True

    return GameWon, WhoWon

  def is_winner(self): #gets output
    GameWon, WhoWon = self.__check_win()
    if GameWon == False:
      output = "Game was not won yet"
    else:
      output = f"\t\t          {WhoWon}"
      return output
    
  