from copy import deepcopy as dp
# D E E P C O P I E S O N L Y

# Used in base-case of recursion to determine if white/black
# can win in a single move i.e. capture the opposing queen
def game_ogre(board,white,black,w):

    if w:
        all_moves = legal_moves(white,board,w)
        qp = black[0]
    else:
        all_moves = legal_moves(black,board,w)
        qp = white[0]

    for key,l in all_moves.items:
        for p in l:
            fro,moves = p
            for move in moves:
                if move == qp:
                    return True
    return False

# Performs the given move on the given board and updates
# the underlying data structures
def make_move(board,move,piece,opposing):
    fro,to = move

    a,b = fro

    c,d = to

    op_piece = list(opposing.keys())
    if board[c][d] in op_piece:

        del opposing[board[a][b]]

        board[a][b] = -1
        board[c][d] = piece



    else:
        board[a][b] = -1
        board[c][d] = piece

# Returns a list of all legal moves
def legal_moves(pieces,board,w):
    
    
    if w:
        opposing = [4,5,6,7]
        friendly = [0,1,2,3]
    else:
        friendly = [4,5,6,7]
        opposing = [0,1,2,3]
    
    def check_knight(start):
        moves = []
        possible_adders = [(-2,1),(2,1),(-1,2),(1,2),(-2,-1),(2,-1),(-1,-2),(1,-2)]
        hp,vp = start
        for p in possible_adders:
            a,b = p
            if 0 <= hp + a <= 3:
                if 0 <= vp + b <= 3:
                    if board[hp+a][vp+b] in opposing + [-1]:
                        moves.append((hp+a,vp+b))
        return moves
    
    def check_diag(start):
        hp,vp = start
        moves = []
        possible = [[(1,1),(2,2),(3,3)],[(1,-1),(2,-2),(2,-3)],[(-1,1),(-2,2),(-3,3)],[(-1,-1),(-2,-2),(-3,-3)]]
        for p in possible:
            for s in p:
                a,b = s
                if 0 <= hp + a <= 3:
                    if 0 <= vp + b <= 3:
                        t = board[hp+a][vp+b]
                        if t == -1:
                            moves.append((hp+a,vp+b))
                            continue
                        if t in opposing:
                            moves.append((hp+a,vp+b))
                            break
                        if t in friendly:
                            break
        return moves
    def check_str8(start):
        hp,vp = start
        moves = []
        possible = [[(0,1),(0,2),(0,3)],[(0,-1),(0,-2),(0,-3)],[(-1,0),(-2,0),(-3,0)],[(1,0),(2,0),(3,0)]]
        for p in possible:
            for s in p:
                a,b = s
                if 0 <= hp + a <= 3:
                    if 0 <= vp + b <= 3:
                        t = board[hp+a][vp+b]
                        if t == -1:
                            moves.append((hp+a,vp+b))
                            continue
                        if t in opposing:
                            moves.append((hp+a,vp+b))
                            break
                        if t in friendly:
                            break
        return moves
            
        
    output = {}
    
    for key in pieces.keys():
        output[key] = []
    
    for key,l in pieces.items():
        for start in l:
            if key % 4 == 0:
                moves = check_diag(start) + check_str8(start)
                
            elif key % 4 == 1:
                moves = check_str8(start)
                
            elif key % 4 == 2:
                moves = check_diag(start)
                
            elif key % 4 == 3:
                moves = check_knight(start)
                
            output[key].append([start,moves])
    return output
                
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










