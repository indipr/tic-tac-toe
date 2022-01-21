from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print("|", end='')
        for col in range(3):
            print(f"   {board[row][col]}   |", end='')
        print()
        print("|       |       |       |")
        print("+-------+-------+-------+")

# display_board results:
#     +-------+-------+-------+
#     |       |       |       |
#     |   1   |   2   |   3   |
#     |       |       |       |
#     +-------+-------+-------+
#     |       |       |       |
#     |   4   |   5   |   6   |
#     |       |       |       |
#     +-------+-------+-------+
#     |       |       |       |
#     |   7   |   8   |   9   |
#     |       |       |       |
#     +-------+-------+-------+

# find index in 2d list
def index_2d(list, search):
    for i, x in enumerate(list):
        if search in x:
            return i, x.index(search)

# asks the user about their move,
# checks the input, and updates the board
def enter_move(board): 
    valid_input = False
    while not valid_input:
        user_move = input("Enter your move: ")
        result = index_2d(board, user_move)

        if result != None:
            board[result[0]][result[1]] = 'O'
            valid_input = True
        else:
            print("Invalid input!")

# checks victory
def victory_for(board, sign):
    win = None

    # checking rows
    for i in range(3):
        win = True
        for j in range(3):
            if board[i][j] != sign:
                win = False
                break
        if win:
            return win
    
    # checking columns
    for i in range(3):
        win = True
        for j in range(3):
            if board[j][i] != sign:
                win = False
                break
        if win:
            return win
    
    # checking diagonals
    # X - -
    # - X -
    # - - X
    win = True
    for i in range(3):
        if board[i][i] != sign:
            win = False
            break
    if win:
        return win
    
    # - - X
    # - X -
    # X - -
    win = True
    j = 0
    for i in range(2, -1, -1):  # 2, 1, 0
        if board[i][j] != sign:
            win = False
            break
        j += 1
    if win:
        return win
    return False

def is_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                return False
    return True

# draws the computer's move and updates the board
def draw_move(board):
    available_move = False
    while not available_move:
        comp_move = str(randrange(10))
        result = index_2d(board, comp_move)

        if result != None:
            # print(result)
            board[result[0]][result[1]] = 'X'
            available_move = True

# main code
board = [
    ['1', '2', '3'], 
    ['4', '5', '6'], 
    ['7', '8', '9']
]

display_board(board)

while True:
    enter_move(board)   # user's turn ('O')
    display_board(board)
    if victory_for(board, 'O'):
        print("Congrats, you win!!!")
        break
    if is_tie(board):
        print("It's a tie!")
        break

    draw_move(board)    # computer's turn ('X')
    display_board(board)
    if victory_for(board, 'X'):
        print("You lose... :(")
        break
    if is_tie(board):
        print("It's a tie!")
        break
    
