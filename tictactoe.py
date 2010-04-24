#!/usr/bin/env python
#TicTacToe
#Written by Danneh, 21 April 2010
play = ('X', 'O')
playCurrent = play[0]

#TestBoard
testBoard = [['7','8','9'],['4','5','6'],['1','2','3']]

while 1: #Newgames
   #>> Initialising
   win = ' '
   #PlayBoard
   playBoard = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

   #>> Playing
   while 1:
      #>> Header Printing
      #Clearing
      import os
      if os.name == "posix": # Unix/Linux
         os.system('clear')
      elif os.name in ("nt", "dos", "ce"): # Windows
         os.system('CLS')
      else: # Unknown/Undefined Systems
         print "\n"*30

      #Boards
      print "\n\n Place Nums:\t\tPlay Board:",
      for i in range(len(testBoard)):
         print "\n ",
         for j in range(len(testBoard)):
            print testBoard[i][j],
            if (j == 0) or (j == 1):
               print '|',
         print "\t\t",
         for j in range(len(playBoard)):
            print playBoard[i][j],
            if (j == 0) or (j == 1):
               print '|',
      print "\n"

      #Win Check - Continuation
      if win != ' ':
         print 'Congrats, '+win+'!'
         print 'You have won the game!'
         raw_input("Press Enter to Continue")
         break
      
      #>> Position Input
      while 1: #Position Error Checking
         pos = int(raw_input('Which Place, '+playCurrent+'? '))

         #Testing Rows
         if pos > 9:
            continue
         elif pos < 1:
            continue
         elif pos < 4:
            row = 2
         elif pos < 7:
            row = 1
         else:
            row = 0

         #Testing Columns
         if (pos % 3) == 0:
            col = 2
         elif ((pos % 2) == 0 and pos != 4) or pos == 5:
            col = 1
         else:
            col = 0

         if playBoard[row][col] == ' ':
            playBoard[row][col] = playCurrent
            break

      #>> Switching Player
      if playCurrent == play[0]:
         playCurrent = play[1]
      else:
         playCurrent = play[0]
         
      #>> Board Checks
      #Board Filled
      filled = 1
      for i in range(len(playBoard)):
         for j in range(len(playBoard)):
            if playBoard[i][j] == ' ':
               filled = 0
      if filled:
         print 'Board is filled, resetting'
         break

      #Player Win
      win = ' '
      pB = playBoard #just as shorthand

      for player in play:
      
         #Diagonals
         if pB[0][0] == player and pB[1][1] == player and pB[2][2] == player:
            win = player
            break
         elif pB[0][2] == player and pB[1][1] == player and pB[2][0] == player:
            win = player
            break
         
         #Horisontals
         for i in range(len(playBoard)):
            if pB[i][0] == player and pB[i][1] == player and pB[i][2] == player:
               win = player
               break
            elif pB[0][i] == player and pB[1][i] == player and pB[2][i] == player:
               win = player
               break
