from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from King import King
from Queen import Queen
from ChessBoard import ChessBoard
from Square import Square
from Dot import Dot
from Piece import Piece
import contextlib
with contextlib.redirect_stdout(None):
    import pygame


def screen_init():
    pygame.init()
    background_colour = (255, 255, 255)
    (width, height) = (800, 600)
    num_squares = 8
    sq_list = []
    for i in range(8):
        sq_list.append([])

    scrn = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Chess Board')
    for i in range(num_squares):
        for j in range(num_squares):
            square = Square(0 + j * 70, 0 + i * 70, scrn)
            sq_list[i].append(square)
            # square = Square(50, 10, screen)
    scrn.fill(background_colour)

    color = 1
    for i in range(len(sq_list)):
        color = -color
        for square in sq_list[i]:
            square.display(color)
            color = -color
    return scrn, sq_list


def opp_player(turn):
    if turn == 'white':
        ret = 'black'
    else:
        ret = 'white'
    return ret

#def check(king, board, list):

'''
evaluate_block(block, player) {
        var score = 0;
        var opp_player = player;
        if (player == 1) {
            opp_player = 2;
        }
        var opp_count = 0;
        var  empty_count = 0;
        for (var i = 0; i < score; i++){
            if (block[i] == player)
                score++; 
            else if (block[i] == opp_player)
                opp_count++;
            else
                empty_count++;
        }
        if (p == 4) {
            score += 100;
        }
        elif (board.get_board()[i][j] == Pawn) 
            score += 10;
        elif (board.get_board()[i][j] == Knight) 
            score += 30;
        elif (opp_count == 3) {
            score = -4;
        }
        return score;
    }

    count_scores(board, player) {
        var score = 0;

        var center_count = 0;
        for (var i = 0; i < 6; i++) {
            if (board[i][3] == player) {
                center_count++;
            }
        }
        score += (center_count * 3);

        // Pawn Score
        for (var i = 0; i < 6; i++) {
            var row_array = [];
            for (var j = 0; j < 7; j++) {
                row_array.push(board[i][j]);
            }
            for (var k = 0; k < 4; k++) {
                var block = row_array.slice(k, k+4);
                score += this.evaluate_block(block, player);
            }
        }

        // Knight score
        for (var i = 0; i < 7; i++) {
            var col_array = [];
            for (var j = 0; j < 6; j++) {
                col_array.push(board[j][i]);
            }
            for (var k = 0; k < 4; k++) {
                var block = col_array.slice(k, k+4);
                score += this.evaluate_block(block, player);
            }
        }

        // Bishop Diagonal score
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 4; j++) {
                var block = [];
                for (var k = 0; k < 4; k++) {
                    block.push(board[i+k][j+k]);
                }
                score += this.evaluate_block(block, player);
            }
        }

        // Rook Diagonal score
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 4; j++) {
                var block = [];
                for (var k = 0; k < 4; k++) {
                    block.push(board[i+3-k][j+k]);
                }
                score += this.evaluate_block(block, player);
            }
        }
        return score;
    }
'''

if __name__ == "__main__":
    (screen, square_list) = screen_init()
    selected = 0
    chessBoard = ChessBoard()
    chessBoard.setup()
    white_fallen_list = []
    black_fallen_list = []
    white_pawn_list = []
    white_knight_list = []
    white_bishop_list = []
    white_rook_list = []
    black_pawn_list = []
    black_knight_list = []
    black_bishop_list = []
    black_rook_list = []
    for i in range(8):
        black_pawn_list.append(Pawn('black', 1, i))
        white_pawn_list.append(Pawn('white', 6, i))
        (chessBoard.get_board())[1][i] = black_pawn_list[i]
        (chessBoard.get_board())[6][i] = white_pawn_list[i]
    black_knight_list.append(Knight('black', 0, 1))
    black_knight_list.append(Knight('black', 0, 6))
    white_knight_list.append(Knight('white', 7, 1))
    white_knight_list.append(Knight('white', 7, 6))
    (chessBoard.get_board())[0][1] = black_knight_list[0]
    (chessBoard.get_board())[0][6] = black_knight_list[1]
    (chessBoard.get_board())[5][2] = Queen('black', 5, 2)
    # (chessBoard.get_board())[2][4] = Knight('white', 2, 4)
    (chessBoard.get_board())[3][3] = Bishop('black', 3, 3)
    (chessBoard.get_board())[7][1] = white_knight_list[0]
    (chessBoard.get_board())[7][6] = white_knight_list[1]
    black_bishop_list.append(Bishop('black', 0, 2))
    black_bishop_list.append(Bishop('black', 0, 5))
    white_bishop_list.append(Bishop('white', 7, 2))
    white_bishop_list.append(Bishop('white', 7, 5))
    (chessBoard.get_board())[0][2] = black_bishop_list[0]
    (chessBoard.get_board())[0][5] = black_bishop_list[1]
    (chessBoard.get_board())[7][2] = white_bishop_list[0]
    (chessBoard.get_board())[7][5] = white_bishop_list[1]
    black_rook_list.append(Rook('black', 0, 0))
    black_rook_list.append(Rook('black', 0, 7))
    white_rook_list.append(Rook('white', 7, 0))
    white_rook_list.append(Rook('white', 7, 7))
    (chessBoard.get_board())[0][0] = black_rook_list[0]
    (chessBoard.get_board())[0][7] = black_rook_list[1]
    (chessBoard.get_board())[7][0] = white_rook_list[0]
    (chessBoard.get_board())[7][7] = white_rook_list[1]
    (chessBoard.get_board())[0][3] = King('black', 0, 3)
    (chessBoard.get_board())[0][4] = Queen('black', 0, 4)
    (chessBoard.get_board())[7][3] = King('white', 7, 3)
    (chessBoard.get_board())[7][4] = Queen('white', 7, 4)
    for j in range(8):
        print(chessBoard.get_board()[j])

    black_pawn_img = pygame.image.load('black_pawn.png')
    white_pawn_img = pygame.image.load('white_pawn.png')
    black_knight_img = pygame.image.load('black_knight.png')
    white_knight_img = pygame.image.load('white_knight.png')
    black_bishop_img = pygame.image.load('black_bishop.png')
    white_bishop_img = pygame.image.load('white_bishop.png')
    black_rook_img = pygame.image.load('black_rook.png')
    white_rook_img = pygame.image.load('white_rook.png')
    black_queen_img = pygame.image.load('black_queen.png')
    white_queen_img = pygame.image.load('white_queen.png')
    black_king_img = pygame.image.load('black_king.png')
    white_king_img = pygame.image.load('white_king.png')

    running = True
    s_piece = 0
    pos_list = 0
    select_x = 0
    select_y = 0
    dot_list = []
    white_king_coor = []
    white_king_pos = (7, 3)
    black_king_coor = []
    black_king_pos = (0, 3)
    white_check = False
    black_check = False
    white_checkmate = False
    black_checkmate = False
    game_end = False
    player_turn = 'white'
    font = pygame.font.SysFont('timesnewroman', 20)
    directions = [[1, 1], [-1, 1], [-1, -1], [1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
    while running:
        if player_turn == 'white':
            text = font.render("White Piece's Turn", True, (0, 0, 0))
        else:
            text = font.render("Black Piece's Turn", True, (0, 0, 0))

        textRect = text.get_rect()
        textRect.center = (650, 100)
        screen.blit(text, textRect)
        st = "White: "
        for piece in white_fallen_list:
            if type(piece) is Pawn:
                st += "Pawn "
            elif type(piece) is Knight:
                st += "Knight "
            elif type(piece) is Bishop:
                st += "Bishop "
            elif type(piece) is Rook:
                st += "Rook "
            elif type(piece) is Queen:
                st += "Queen "
            elif type(piece) is King:
                st += "King "
        font1 = pygame.font.SysFont('timesnewroman', 12)
        text = font1.render(st, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (580, 300)
        screen.blit(text, textRect)
        white_king_check = False
        black_king_check = False
        for i in range(8):
            for j in range(8):
                if chessBoard.get_board()[i][j] != 0:
                    if chessBoard.get_board()[i][j].get_color() == 'black':
                        if white_king_pos in chessBoard.get_board()[i][j].possible(chessBoard.get_board()):
                            white_king_check = True
                        for pos in chessBoard.get_board()[i][j].possible(chessBoard.get_board()):
                            if pos in white_king_coor:
                                white_king_coor.remove(pos)
                    else:
                        if black_king_pos in chessBoard.get_board()[i][j].possible(chessBoard.get_board()):
                            black_king_check = True
                        for pos in chessBoard.get_board()[i][j].possible(chessBoard.get_board()):
                            if pos in black_king_coor:
                                black_king_coor.remove(pos)
                if type(chessBoard.get_board()[i][j]) is Pawn:
                    if chessBoard.get_board()[i][j].get_color() == 'black':
                        screen.blit(black_pawn_img, (j * 70, i * 70))
                    else:
                        screen.blit(white_pawn_img, (j * 70, i * 70))
                elif type(chessBoard.get_board()[i][j]) is Knight:
                    if chessBoard.get_board()[i][j].get_color() == 'black':
                        screen.blit(black_knight_img, (j * 70, i * 70))
                    else:
                        screen.blit(white_knight_img, (j * 70, i * 70))
                elif type(chessBoard.get_board()[i][j]) is Bishop:
                    if chessBoard.get_board()[i][j].get_color() == 'black':
                        screen.blit(black_bishop_img, (j * 70, i * 70))
                    else:
                        screen.blit(white_bishop_img, (j * 70, i * 70))
                elif type(chessBoard.get_board()[i][j]) is Rook:
                    if chessBoard.get_board()[i][j].get_color() == 'black':
                        screen.blit(black_rook_img, (j * 70, i * 70))
                    else:
                        screen.blit(white_rook_img, (j * 70, i * 70))
                elif type(chessBoard.get_board()[i][j]) is Queen:
                    if chessBoard.get_board()[i][j].get_color() == 'black':
                        screen.blit(black_queen_img, (j * 70, i * 70))
                    else:
                        screen.blit(white_queen_img, (j * 70, i * 70))
                elif type(chessBoard.get_board()[i][j]) is King:
                    if chessBoard.get_board()[i][j].get_color() == 'black':
                        screen.blit(black_king_img, (j * 70, i * 70))
                        black_king_coor = []
                        for direction in chessBoard.get_board()[i][j].possible(
                                chessBoard.get_board()):
                            black_king_coor.append(direction)
                    else:
                        screen.blit(white_king_img, (j * 70, i * 70))
                        white_king_coor = []
                        for direction in chessBoard.get_board()[i][j].possible(
                                chessBoard.get_board()):
                            white_king_coor.append(direction)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #if game_end:
            #    pygame.time.wait(10000)
            #    running = False

            # Starting here on when the mouse is clicked.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected != 0:
                    selected.set_color(selected.bd_color[0], selected.bd_color[1], selected.bd_color[2])
                # Removes the trail
                if s_piece != 0:
                    pos_loc = square_list[s_piece.get_x()][s_piece.get_y()]
                    pos_loc.set_color(pos_loc.bd_color[0], pos_loc.bd_color[1],
                                      pos_loc.bd_color[2])
                if pos_list != 0:
                    for k in range(len(pos_list)):
                        pos_location = square_list[pos_list[k][0]][pos_list[k][1]]
                        pos_location.set_color(pos_location.bd_color[0], pos_location.bd_color[1],
                                               pos_location.bd_color[2])
                (mouseX, mouseY) = pygame.mouse.get_pos()
                for i in range(8):
                    for j in range(8):
                        if square_list[i][j].check_clicked(mouseX, mouseY) == 1:
                            # If the player clicks the empty block
                            if chessBoard.get_board()[i][j] == 0:
                                # If the piece has been selected.
                                if selected != 0:
                                    # Get the coordinate for the piece on that square, so that when it is pressed again,
                                    # the light turns off.
                                    if (i, j) in pos_list:
                                        chessBoard.get_board()[i][j] = chessBoard.get_board()[select_x][select_y]
                                        chessBoard.get_board()[i][j].set_x(i)
                                        chessBoard.get_board()[i][j].set_y(j)
                                        chessBoard.get_board()[select_x][select_y] = 0
                                        if type(chessBoard.get_board()[i][j]) is Pawn:
                                            chessBoard.get_board()[i][j].set_moved(True)
                                        if type(chessBoard.get_board()[i][j]) is King:
                                            if chessBoard.get_board()[i][j].get_color() == 'black':
                                                black_king_coor = []
                                                for direction in chessBoard.get_board()[i][j].possible(
                                                        chessBoard.get_board()):
                                                    black_king_coor.append(direction)
                                                black_king_pos = (i, j)
                                                print("black king", black_king_coor)

                                            else:
                                                white_king_coor = []
                                                for direction in chessBoard.get_board()[i][j].possible(
                                                        chessBoard.get_board()):
                                                    white_king_coor.append(direction)
                                                white_king_pos = (i, j)
                                                print("white king", white_king_coor)
                                        selected = 0
                                        pos_list = 0
                                        player_turn = opp_player(player_turn)
                                    else:
                                        selected = 0
                                        pos_list = 0
                            # In case when the piece has been clicked for the first time.
                            else:
                                s_piece = chessBoard.get_board()[i][j]
                                # print("piece or a 0:", select_x, select_y, selected)
                                # Add conditional with selected, so that it can take over other pieces
                                if selected != 0:
                                    # If the same piece has been clicked.
                                    if (i, j) == (select_x, select_y):
                                        selected = 0
                                        pos_list = 0
                                    # If the same colored piece has been clicked
                                    elif (chessBoard.get_board()[i][j].get_color() ==
                                          chessBoard.get_board()[select_x][select_y].get_color()):
                                        selected = 0
                                        pos_list = 0
                                    # If an empty square has been clicked
                                    elif chessBoard.get_board()[select_x][select_y] == 0:
                                        selected = 0
                                        pos_list = 0
                                    # If the opposite colored piece has been clicked
                                    elif (chessBoard.get_board()[i][j].get_color() !=
                                            chessBoard.get_board()[select_x][select_y].get_color()):
                                        # print ("1: select_x, select_y:", select_x, select_y, "\n", "2: pos_list:", pos_list)
                                        # print ("3: i, j:", i, j)
                                        # If it is a valid move
                                        if (i, j) in pos_list:
                                            if type(chessBoard.get_board()[i][j]) is King:
                                                game_end = True
                                            if player_turn == 'black':
                                                white_fallen_list.append(chessBoard.get_board()[i][j])
                                            else:
                                                black_fallen_list.append(chessBoard.get_board()[i][j])
                                            chessBoard.get_board()[i][j] = chessBoard.get_board()[select_x][select_y]
                                            chessBoard.get_board()[i][j].set_x(i)
                                            chessBoard.get_board()[i][j].set_y(j)
                                            chessBoard.get_board()[select_x][select_y] = 0
                                            selected = 0
                                            pos_list = 0
                                            player_turn = opp_player(player_turn)
                                        # If it is not a valid move
                                        else:
                                            selected = 0
                                            pos_list = 0
                                            print("pos_list:", pos_list)
                                # Show the possible movements.
                                else:
                                    if player_turn == chessBoard.get_board()[i][j].get_color():
                                        selected = square_list[i][j]
                                        selected.set_color(255, 255, 204)
                                        if chessBoard.get_board()[i][j].get_color() == 'black':
                                            print(chessBoard.get_board()[i][j].possible(chessBoard.get_board()))
                                            # print(chessBoard.get_board()[i][j].possible(chessBoard.get_board())[0])
                                        pos_list = chessBoard.get_board()[i][j].possible(chessBoard.get_board())
                                        for k in range(len(pos_list)):
                                            pos_location = square_list[pos_list[k][0]][pos_list[k][1]]
                                            pos_location.set_color(255, 255, 204)
                                select_x = i
                                select_y = j
                                print("Check?", black_king_check)
                                if black_king_check:
                                    print("CHECK ON BLACK KING", black_king_coor)
                                    if not black_king_coor:
                                        print("CHECKMATE ON BLACK KING")
                                    # pygame.time.wait(1000)
                                elif white_king_check:
                                    print("CHECK ON WHITE KING")
                                    if not white_king_coor:
                                        print("CHECKMATE ON WHITE KING")
                                    # pygame.time.wait(1000)
                                if game_end:
                                    font = pygame.font.SysFont('timesnewroman', 20)
                                    if player_turn == 'black':
                                        text = font.render("White Piece Wins", True, (0, 0, 0))
                                    else:
                                        text = font.render("Black Piece Wins", True, (0, 0, 0))
                                    textRect = text.get_rect()
                                    textRect.center = (650, 300)
                                    screen.blit(text, textRect)
        '''
        minimax(bd, depth, alpha, beta, maxPlayer) 
        var self = this;
        var valid_location = this.findColEmpty(bd);
        var player;
        // Since we check if the game is over from the previous move,
        // If maxPlayer, player = 1
        if (maxPlayer == true)
            player = 1;
        }
        else {
            player = 2;
        }
        var is_terminal = this.game_over(bd, player);
        if (depth == 0 || is_terminal)
            if (is_terminal)
                if (this.check_win(bd, 2, 'sim'))
                    return [null, 10000]
                }
                else if (this.check_win(bd, 1, 'sim'))
                    return [null, -10000]
                }
                else 
                    return [null, 0]
                
            
            else
                return [null, this.count_scores(bd, 2)]
            
        
        if (maxPlayer)
            //console.log("performing minmax: max");
            var value = -999999999999999;
            var best_col;
            for (var i = 0; i < (valid_location).length; i++) 
                var row_num = this.findRowOpen(bd, valid_location[i]);
                var b_copy = JSON.parse(JSON.stringify(bd));
                var index = this.convert_index(row_num, valid_location[i]);
                this.place_dot(b_copy, index, 2);
                //console.log(b_copy[5], b_copy[4]);
                var new_score;
                var given;
        '''
        pygame.display.flip()
        # pygame.time.wait(60)
