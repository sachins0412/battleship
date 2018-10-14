import time
import os
from random import randint
def clear():
    os.system('cls') 

  
    
board = []
for i in range(0,5):
    board.append(['O']*5)
def printboard(board):
    for i in board:
        print(" ".join(i))

printboard(board)
ship_row=randint(0,4)
ship_col=randint(0,4)

for turn in range(0,3):
    
    
    print("Turn:",turn+1)
    guess_row = int(input("enter row : "))-1
    guess_col = int(input("enter col : "))-1
    if guess_row==ship_row and guess_col==ship_col:
        print("you win XD")
        break
    else :
        
        if guess_row not in range(0,5) or guess_col not in range(0,5):
            print("thats not even in ocean :P")
        elif board[guess_row][guess_col]=="X":
            print("yoou have already hit that")
        else:
            print("Better luck next time//")
            board[guess_row][guess_col]= "X"
        
        if turn==2:
                print("GAME OVER")
    time.sleep(3)

    clear()        
    printboard(board)
    
        
        
            
            
             
        
            
