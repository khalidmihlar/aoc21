import re

def winner(board, called):
    for i in range(5):
        if set(board[i::5]).issubset(called):
            return True;
    for i in range(5):
        if set(board[i*5:(i*5)+5]).issubset(called):
            return True
    return False;
            
def score(board, called):
    sum = 0
    for i in range(len(board)):
        if board[i] not in called:
            sum+=board[i]
    return sum   

def four(file):
    #reading
    f = open(file)
    called = set() # to put in winner
    input = f.read() #for the original input (order)
    boards = input.split("\r\n\r\n")
    input = boards[0]
    boards = boards[1:]   
    
    #formatting
    for i in range (len(boards)):
        boards[i] = map(int,re.findall(r"\d+", boards[i])) #for future regex
    input = map(int,re.findall(r"\d+", input)) #for future regex
    
    #main
    for num in input:
        called.add(num)
        for board in boards:
            if winner(board, called):
                if len(boards) == 1:
                    print(board)
                    return(score(board,called)*num)
                boards.remove(board)

a = four("input.txt")
print(a)
