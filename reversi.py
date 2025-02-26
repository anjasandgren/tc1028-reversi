"""
REVERSI

"""


"""
Function that creates the start board
OUTPUT : matrix, the start game bord with 2 black and 2 white in the middle
"""
def create_start_board():
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            if i==j==3 or i==j==4:
                row.append('white')
            elif (i==3 and j==4) or (i==4 and j==3):
                row.append('black')
            else:
                row.append('')
        board.append(row)
    return board



"""
Function that prints the board
INPUT : matrix, game board to print 
"""
def print_board(board):    
    print("    A B C D E F G H")
    print("   -----------------")
    for row in range(len(board)):
        print(str(row+1) + " | ", end="")
        for elem in board[row]:
            if elem == 'black':
                elem_print = '●'
            elif elem == 'white':
                elem_print = '◯'
            else:
                elem_print = ' '
            print(elem_print, end=" ")
        print("| " + str(row+1))
    print("   -----------------")
    print("    A B C D E F G H \n")    



"""
Function that counts number of a specific color in a matrix

INPUT	: matrix, game board
          string, color to count, 2 possibilties: 'black' or 'white'
OUTPUT	: integer, the current number of pices with the requested color on the game board
"""
def count_color(board, color):
    nr_of_color = 0
    for row in range(len(board)):
        nr_of_color += board[row].count(color)
    return nr_of_color



"""
Function that prints help/rules
"""
def show_help():
    print("""
Players take turns placing their pieces (one side black, the other white) on the board.
When a player places a piece, any opponent's piece in a straight line (horizontal, vertical,
or diagonal) between the placed piece and another of the player's pieces are flipped to the
player's color. The game ends when the board is full or no more valid moves are possible.
Each placement have to turn at least one of th opponents pieces. 

THe winner is the player with the most pieces, of their color, on the board when it's full
or no player can do a valid move. 

To place a piece enter the letter of the column (a-h) and the number of the row (1-8)
you want to place your piece.
""")



"""
Function that compute the start menu
OUTPUT : integer, the requested number from the menu (1, 2 or 3) 
"""
def compute_menu():    
    print("""
 --------- MENU -------- 
|	  	  	|
|	1. PLAY		|
|	2. Help		|
|	3. Exit 	|
|		  	|
 -----------------------
 
""")
    
    choice_made = False
    while not choice_made :
        choice = int(input("Enter your choice: "))
        
        if choice!=1 and choice!=2 and choice!=3 :
            print("ERROR! You must choose a number from the menu (1-3).\n")
        else :
            choice_made = True

    return choice
 


"""
Function that turns a requested piece so the color of the spot changes from black to white or the other way around
INPUT	: matrix, game board
          array,  requested spot, format ex: [0,0] for 'a1' and [2,4] for 'e3'
OUTPUT	: matrix, game board
"""
def switch_color(board, spot):
    if board[spot[1]][spot[0]] == 'black':
        board[spot[1]][spot[0]] = 'white'
    else:
        board[spot[1]][spot[0]] = 'black'
    return board



"""
Function that turns pices

INPUT	: matrix,  the gamebord
          array,   the last put piece that is causing the turning, ex: [1, 1] for 'b2'
          string,  the direction the turning should be done, 4 possibilities: 'left', 'right', 'up' or 'down' 
          integer, the number of pieces that should be turned to the given direction
          
OUTPUT	: matrix,  updated game board with the pieces turned
"""
def turn_pieces(board, spot, direction, nr_of_pieces):
    
    for i in range(1, nr_of_pieces+1) :
        
        if direction == 'left':
            piece_to_turn = [spot[0]-i, spot[1]]
        elif direction == 'right':
            piece_to_turn = [spot[0]+i, spot[1]]
        elif direction == 'up':
            piece_to_turn = [spot[0], spot[1]-i]
        elif direction == 'down':
            piece_to_turn = [spot[0], spot[1]+i]
        elif direction == 'up_left':
            piece_to_turn = [spot[0]-i, spot[1]-i]
        elif direction == 'down_left':
            piece_to_turn = [spot[0]-i, spot[1]+i]
        elif direction == 'down_right':
            piece_to_turn = [spot[0]+i, spot[1]+i]
        elif direction == 'up_right':
            piece_to_turn = [spot[0]+i, spot[1]-i]
        
        board = switch_color(board, piece_to_turn)
        
    return board



"""
Function that checks if a spot on the board is full (or empty/available)

INPUT	: matrix,  the current game board
          array,   the requested spot
          string,  the letter of the column and the number of the row that is going to be checked on format 'a1', 'g4', 'h8' etc.
          boolean, True if the board should change, False if this function is only used to check if there are available spots

OUTPUT	: boolean, True if there are pieces on every place of the row, otherwise False
"""
def check_spot(board,spot,color,update_board):

# 1. Already occupied? 
    if board[spot[1]][spot[0]] != '' :
        if update_board:
            print("\nERROR! \nThe spot is already taken, try another one.\n\n")
        return False, board


# 2. Placement turns pieces from opponent?
    if color == 'white' :
        opp_color = 'black'
    else :
        opp_color = 'white'
    
    spot_is_connected = False 

    #Check left
    if spot[0] > 1 :
        if board[spot[1]][spot[0]-1] == opp_color :
            for i in range(1,spot[0]):
                if board[spot[1]][spot[0]-i] == '':
                    break
                elif board[spot[1]][spot[0]-i] == color :
                    if update_board:
                        board = turn_pieces(board, spot, 'left', i-1)
                    spot_is_connected = True
                    break

    #Check right
    if spot[0] < 6 :
        if board[spot[1]][spot[0]+1] == opp_color :
            for i in range(1,7-spot[0]):
                if board[spot[1]][spot[0]+i] == '':
                    break
                elif board[spot[1]][spot[0]+i] == color :
                    if update_board:
                        board = turn_pieces(board, spot, 'right', i-1)
                    spot_is_connected = True
                    break
    
    #Check up
    if spot[1] > 1 :
        if board[spot[1]-1][spot[0]] == opp_color :
            for i in range(1,spot[1]):
                if board[spot[1]-i][spot[0]] == '':
                    break
                elif board[spot[1]-i][spot[0]] == color :
                    if update_board:
                        board = turn_pieces(board, spot, 'up', i-1)
                    spot_is_connected = True
                    break
    
    #Check down
    if spot[1] < 6 :
        if board[spot[1]+1][spot[0]] == opp_color :
            for i in range(1,7-spot[1]):
                if board[spot[1]+i][spot[0]] == '':
                    break
                elif board[spot[1]+i][spot[0]] == color :
                    if update_board:
                        board = turn_pieces(board, spot, 'down', i-1)
                    spot_is_connected = True
                    break
    
    
    #Check diagonal up-left
    if spot[0] > 1 and spot[1] > 1 :
        if board[spot[1]-1][spot[0]-1] == opp_color :
            for i in range(1, min(spot[0],spot[1])):
                if board[spot[1]-i][spot[0]-i] == '':
                    break
                elif board[spot[1]-i][spot[0]-i] == color :
                    if update_board:
                        board = turn_pieces(board, spot, 'up_left', i-1)
                    spot_is_connected = True
                    break
    
    
    #Check diagonal down-left
    if spot[0] > 1 and spot[1] < 6 :
        if board[spot[1]+1][spot[0]-1] == opp_color :
            for i in range(1, min(spot[0], 7-spot[1])):
                if board[spot[1]+i][spot[0]-i] == '':
                    break
                elif board[spot[1]+i][spot[0]-i] == color :
                    if update_board:
                        board = turn_pieces(board, spot, 'down_left', i-1)
                    spot_is_connected = True
                    break
    
    
    #Check diagonal down-right
    if spot[0] < 6 and spot[1] < 6:
        if board[spot[1]+1][spot[0]+1] == opp_color :
            for i in range(1,min(7-spot[0], 7-spot[1])):
                if board[spot[1]+i][spot[0]+i] == '':
                    break
                elif board[spot[1]+i][spot[0]+i] == color :
                    if update_board:
                        board = turn_pieces(board, spot, 'down_right', i-1)
                    spot_is_connected = True
                    break
                
                
    #Check diagonal up-right
    if spot[0] < 6 and spot[1] > 1:
        if board[spot[1]-1][spot[0]+1] == opp_color :
            for i in range(1, min(7-spot[0], spot[1])):
                if board[spot[1]-i][spot[0]+i] == '':
                    break
                elif board[spot[1]-i][spot[0]+i] == color :
                    if update_board:
                        board = turn_pieces(board, spot, 'up_right', i-1)
                    spot_is_connected = True
                    break
    
    
    if spot_is_connected :
        return True, board
    else :
        return False, board



"""
Function that changes the format of the requested spot,
    ex. 'a1' --> [0, 0]
        'b3' --> [1, 2]
        'c5' --> [2, 4]
        
INPUT	: string, the spot on format 'a1' or 'A1' or 'a 1 '
OUTPUT	: array of two integers, [column, row], ex: [0,0] for 'a1' and [4, 2] for 'e3'
"""
def format_spot(spot_str):
    spot_arr = [spot_str[0], spot_str[1]]
    spot_arr[0] = spot_arr[0].lower()
    spot_arr[0] = ord(spot_arr[0]) - 97
    spot_arr[1] = int(spot_arr[1]) - 1
    return spot_arr



"""
Function that checks if the requested spot is written on the right format: 'a1', 'G4', 'h 8 ' etc.
INPUT	: string,  the spot string that is going to be checked
OUTOUT	: boolean, True if the format was correct, otherwise False
"""
def spot_format_is_ok(spot):
    
    spot = spot.replace(" ", "")
    spot = spot.lower()
    
    if len(spot)!=2 or (spot[0]!='a' and spot[0]!='b' and spot[0]!='c' and spot[0]!='d' and spot[0]!='e' and spot[0]!='f' and spot[0]!='g' and spot[0]!='h') or (spot[1]!='1' and spot[1]!='2' and spot[1]!='3' and spot[1]!='4' and spot[1]!='5' and spot[1]!='6' and spot[1]!='7' and spot[1]!='8'):
        print("\nERROR!")
        print("The format of the requester spot is wrong. Please write on the format 'a1', 'g4', 'h8' etc.\n")
        return False
    return True



"""
Function that computes one turn.

INPUT	: matrix, the game board
          string, the color who's turn it is ('black' or 'white')
          
OUTPUT	: matrix, the updated game board after the turn 
"""
def one_turn(board, color):
        
        if move_availble(board, color):
            
            print(f"\n\n   It's {color}'s turn!\n")
            print_board(board)
            
            choice_made = False
            
            while not choice_made : 
                spot_str = input("Enter where you wanna place your piece: ")
                
                if spot_format_is_ok(spot_str):
                    spot = format_spot(spot_str)
                    result = check_spot(board,spot,color,True)
                    spot_is_ok = result[0]
                    board = result[1]
                    
                    if spot_is_ok :
                        board[spot[1]][spot[0]] = color
                        choice_made = True
                    else:
                        print("\nERROR! \nYou need to choose a spot next that turn at least on of your opponents pieces.\n\n")

            return board
        
        else :
            print("No possible places for " + color)
            return board



"""
Function that check is a player has any avaiable valid move.

INPUT	: matrix,  the game board
          string,  the color of the player who's turn it is ('black' or 'white')
OUTPUT	: booelan, True if there are valid spots to place a piece, otherwise False 
"""
def move_availble(board, color):
    
    for column in range(8):
        for row in range(8):
            spot = [column, row]
            spot_is_ok, theoretical_board = check_spot(board,spot,color,False)
            if spot_is_ok :
                return True

    return False



"""
Function that checks if the game is still going on or if the board is full.
If the board is full it print the game-over-message.

INPUT	: matrix,  game board
OUTPUT 	: boolean, True if the game is continuing, False is the game is over
"""
def game_is_continuing(board) :
    
    nr_of_black = count_color(board, 'black')
    nr_of_white = count_color(board, 'white')
    
    if nr_of_black + nr_of_white == 64:
        if nr_of_black > nr_of_white :
            winner = 'Black'
        else :
            winner = 'White'
        
        print("Game finished! " + winner + " wins!\n\n")
        return False
    
    return True



"""
Function the computes one game
"""
def play():
    board = create_start_board()
    playing = True
    
    print("\n\nLET'S PLAY REVERSI!")
    while playing :

        board = one_turn(board, 'black')
        board = one_turn(board, 'white')
        playing = game_is_continuing(board)



"""
Main function for Reversi
"""
def main():
    print("WELCOME TO REVERSI")
    
    game_open = True
    
    while game_open: 
        choice = compute_menu()
        
        if choice == 1 :
            play()
            
        elif choice == 2 :
            show_help()
            
        else :
            game_open = False


main()
