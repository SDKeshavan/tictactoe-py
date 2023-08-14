#tic tac toe

board=[["TL","TM","TR"],
       ["ML","MM","MR"],
       ["BL","BM","BR"]]

maps={
    'T':0,
    'L':0,
    'M':1,
    'R':2,
    'B':2
    }

hl="-----"
def displayBoard():
    print("| {:>3} | {:>3} | {:>3} |".format(board[0][0], board[0][1], board[0][2]))
    print("|{:>3}|{:>3}|{:>3}|".format(hl,hl,hl))
    print("| {:>3} | {:>3} | {:>3} |".format(board[1][0], board[1][1], board[1][2]))
    print("|{:>3}|{:>3}|{:>3}|".format(hl,hl,hl))
    print("| {:>3} | {:>3} | {:>3} |".format(board[2][0], board[2][1], board[2][2]))
    
displayBoard()

def check(sym):
    dia1,dia2=1,1
    for i in range(0,3):
        if board[i][1]==sym and board[i][0]==sym and board[i][2]==sym:
            return 0
        if board[0][i]==sym and board[1][i]==sym and board[2][i]==sym:
            return 0
        if board[i][i]!=sym and dia1==1:
            dia1=0
        if board[i][2-i]!=sym and dia2==1:
            dia2=0
    if dia1==1 or dia2==1:
        return 0
    return 1

print("\n\nInstructions :")
print("#If you need your move in a position enter the corresponding position in caps \nEg: TL")
print("#A new board with the move you made will be printed for every command")
print("\n# Enjoy the game")



nos={"X":0,"O":0}
players=['X','O']
crnt=0
cond=1
while cond==1:
    print("Player ",players[crnt%2],"'s chance")
    inp=input("Enter your position :")

    board[maps[inp[0]]][maps[inp[1]]]=players[crnt%2]
    displayBoard()

    cond=check(players[crnt%2])

    if cond==0:
        print(players[crnt%2], " wins the game.")
        break
    crnt+=1
        

