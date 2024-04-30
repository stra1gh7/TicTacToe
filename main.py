import os
import time
from utilities import drawBoard, checkTurn, checkWin

os.system('color 02')
os.system('mode 45, 13')

spots = {1: '1', 2: '2', 3: '3', 
         4: '4', 5: '5', 6: '6', 
         7: '7', 8: '8', 9: '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')

    drawBoard(spots)

    if (prev_turn == turn):
        print("\nInvalid spot, please pick another one")
    prev_turn = turn

    print("\nIf you want to quit type q")

    if turn%2==0:
        choice = input("\nPlayer 1's turn: ")
    else: choice = input("\nPlayer 2's turn: ")

    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X", "O"}:
            turn += 1
            spots[int(choice)] = checkTurn(turn)

    if checkWin(spots): playing, complete = False, True

    if turn > 8:
        playing = False

os.system('cls' if os.name == 'nt' else 'clear')

drawBoard(spots)

if complete:
    if checkTurn(turn) == 'X':
        os.system('mode 45,10')
        drawBoard(spots)
        print("\n             Player 1 (X) won!")
        time.sleep(500)
    else: 
        os.system('mode 45,10')
        drawBoard(spots)
        print("\n             Player 2 (O) won!")
        time.sleep(500)
else: 
    os.system('mode 45,10')
    drawBoard(spots)
    print("\n              Tie! No winner.")
    time.sleep(500)