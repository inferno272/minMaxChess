from copy import deepcopy as dp
# D E E P C O P I E S O N L Y










# Used in base-case of recursion to determine if white/black
# can win in a single move i.e. capture the opposing queen
def game_ogre(board,white,black,w):
    #Parameter w is True if we're checking if white can win
    #and False if we're checking if black can win


    #Get all possible legal moves for the side we're checking for
    #qp will be the position of the opposing side's queen
    if w:
        all_moves = legal_moves(white,board,w)
        qp = black[0]
    else:
        all_moves = legal_moves(black,board,w)
        qp = white[0]


    #Loop through all moves and check to see if the queen
    #is on a square we can move to, if it is then we can 
    #capture it, so we return True.


    for key,l in all_moves.items():
        for p in l:
            fro,moves = p
            for move in moves:
                if move == qp:
                    return True
    return False









# Performs the given move on the given board and updates
# the underlying data structures
def make_move(board,move,piece,opposing):



    #fro is the current position of the piece
    # and to is the square we want to move it to
    fro,to = move
    fro_x,fro_y = fro
    to_x,to_y = to

    #Make a list of the opposing sides pieces
    #so we can check if a piece is on a square
    #we want to move to


    op_piece = list(opposing.keys())



    #if the to position is occupied by an opposing
    #piece, we have to capture it so it must be 
    #deleted from the dictionary


    if board[to_x][to_y] in op_piece:
        #delete from dictionary
        del opposing[board[a][b]]
        #set from position empty
        #set to position as the piece
        board[fro_x][fro_y] = -1
        board[to_x][to_y] = piece



    else:
        #set from position empty
        #set to position as the piece
        board[fro_x][fro_y] = -1
        board[to_x][to_y] = piece






# Returns a dictionary of all legal moves
def legal_moves(pieces,board,w):
    #pieces is a dictionary of the pieces we want
    #to check the legal moves for
    #board is the current board
    #w is True if we're checking for white
    #and False is we're checking for black



    #Set opposing variables according to
    #the parameter w
    if w:
        opposing = [4,5,6,7]
        friendly = [0,1,2,3]
    else:
        friendly = [4,5,6,7]
        opposing = [0,1,2,3]
    
    #Function to check moves for knights
    def check_knight(start):
        moves = []
        #The 8 possible moves a knight can make
        possible_adders = [(-2,1),(2,1),(-1,2),(1,2),(-2,-1),(2,-1),(-1,-2),(1,-2)]
        hp,vp = start
        for adder in possible_adders:
            a,b = adder

            #check if moving the knight keeps it on the 4x4 grid
            if 0 <= hp + a <= 3:
                if 0 <= vp + b <= 3:
                    #only add it as a possible move if the square
                    #we're checking is occupied by enemy piece
                    #or is empty
                    if board[hp+a][vp+b] in opposing + [-1]:
                        moves.append((hp+a,vp+b))
        return moves
    #Function to check diagnal moves (for bishops)
    def check_diag(start):
        hp,vp = start
        moves = []
        #All the possible progressions for a dignal move
        possible = [[(1,1),(2,2),(3,3)],[(1,-1),(2,-2),(2,-3)],[(-1,1),(-2,2),(-3,3)],[(-1,-1),(-2,-2),(-3,-3)]]
        for progression in possible:
            for adder in progression:
                a,b = adder

                #check to see if adder will keep piece in 4x4 grid
                if 0 <= hp + a <= 3:
                    if 0 <= vp + b <= 3:
                        #the state of the square in the board
                        t = board[hp+a][vp+b]
                        #if current state is empty, add it to possible moves
                        #and move the next adder in the progression
                        if t == -1:
                            moves.append((hp+a,vp+b))
                            continue
                        #if the current state is an enemy piece
                        #add if to possible move b/c we can capture it
                        #but break the loop in the current progression
                        #b/c it is blocking the path
                        if t in opposing:
                            moves.append((hp+a,vp+b))
                            break

                        #if the current state is occupied by friendly piece
                        #break b/c it's blocking the path
                        if t in friendly:
                            break
        return moves

    #Function to check straight path moves (like a rook)
    def check_str8(start):
        hp,vp = start
        moves = []
        possible = [[(0,1),(0,2),(0,3)],[(0,-1),(0,-2),(0,-3)],[(-1,0),(-2,0),(-3,0)],[(1,0),(2,0),(3,0)]]
        for progression in possible:
            for adder in progression:
                a,b = adder

                #check to see if adder will keep piece in 4x4 grid
                if 0 <= hp + a <= 3:
                    if 0 <= vp + b <= 3:
                        #the state of the square in the board
                        t = board[hp+a][vp+b]
                        #if current state is empty, add it to possible moves
                        #and move the next adder in the progression
                        if t == -1:
                            moves.append((hp+a,vp+b))
                            continue
                        #if the current state is an enemy piece
                        #add if to possible move b/c we can capture it
                        #but break the loop in the current progression
                        #b/c it is blocking the path
                        if t in opposing:
                            moves.append((hp+a,vp+b))
                            break

                        #if the current state is occupied by friendly piece
                        #break b/c it's blocking the path
                        if t in friendly:
                            break
        return moves
            
    #output dictionary
    output = {}
    
    #for each possible piece type (knight, rook, etc.)
    #instantiate a list b/c we can have two of each type
    for key in pieces.keys():
        output[key] = []
    
    for typ,starting_positions in pieces.items():
        for start in starting_positions:

            #if the type is queen, check diagnal and straight moves 
            if typ % 4 == 0:
                moves = check_diag(start) + check_str8(start)
            #if the type is rook, check straight moves
            elif typ % 4 == 1:
                moves = check_str8(start)
            #if the type is bishop, check diagnal moves
            elif typ % 4 == 2:
                moves = check_diag(start)
            #if the type is knight, check knight moves
            elif typ % 4 == 3:
                moves = check_knight(start)
            #append the possible moves to the list
            #corresponding to its type in the output dictionary


            output[key].append([start,moves])


    return output
             


if __name__ == '__main__':   
    # MAIN FUNCTION REPEATS FOR NUM_GAMES                
    num_games = int(input())
    for game in range(num_games):
        
        board = [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
        
        l_to_num = {'A':0,'B':1,'C':2,'D':3}
        bnum_to_num = {'1':0,'2':1,'3':2,'4':3}
        w_to_num = {'Q':0,'R':1,'B':2,'N':3}
        b_to_num = {'Q':4,'R':5,'B':6,'N':7}
        
        white_pieces = {0:[],1:[],2:[],3:[]}
        black_pieces = {4:[],5:[],6:[],7:[]}
        
        n_white_pieces,n_black_pieces,num_moves = list(map(int,input().split()))
        for x in range(n_white_pieces):
            temp_name,hp,vp = input().split()
            hp = l_to_num[hp]
            vp = bnum_to_num[vp]
            num = w_to_num[temp_name]
            white_pieces[num].append((hp,vp))
            board[hp][vp] = num
            
            
        for x in range(n_black_pieces):
            temp_name,hp,vp = input().split()
            hp = l_to_num[hp]
            vp = bnum_to_num[vp]
            num = b_to_num[temp_name]
            black_pieces[num].append((hp,vp))
            board[hp][vp] = num
            
        print(legal_moves(white_pieces,board,True))
        

        # @TODO DETERMINE IF WHITE CAN WIN IN NUM_MOVE TURN(s) 
        # RETURN YES OR NO  


# MAX RECURSION FUNCTION
# Checks if White can win in one move, if not recursively calls 
# Blacks legal moves
def WhiteValue(board, moves_left, alpha, beta):
    if (GameOgre(b) or (num_moves-1) == 0)
        return Analysis(b)
    max = -infinity

    all_moves = legal_moves(pieces, board, w)

    for key, l in all_moves.items():
        for p in l:
            fro, moves = p
            for move in moves:
                new_board = dp(board)
                new_blacks = dp(black_pieces)
                make_move(new_board, [fro,move], key, new_blacks)
                x = BlackValue(c, num_moves-1, alpha, beta)
                if (x>max) max = x
                if (x>alpha) alpha = x
                if (alpha>=beta) return alpha
    return max
# MIN RECURSION FUNCTION 
def BlackValue(board, depth, alpha, beta):
    if (GameOgre(b) or depth>MaxDepth)
        return Analysis(b)
    min = infinity
    for each legal move m in board b
        new_board = make_move(b[:], move)
        x = WhiteValue(c, depth+1, alpha, beta)
        if (x<min) min = x
        if (x<beta) beta = x
        if (alpha>=beta) return beta
    return min

# DETERMINES BEST MOVE FOR CURRENT PLAYER
# CALLED BY BOTH BLACK/WHITE
def Analysis(board):
    # 0 = LOSE
    # 1 = WIN


    return 0










