from tkinter import *
import tkinter as tk
from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from King import King
from Queen import Queen
from ChessBoard import ChessBoard
from Piece import Piece
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

if __name__ == "__main__":
    chessBoard = ChessBoard()
    chessBoard.setup()
    white_pawn_list = []
    white_knight_list = []
    white_bishop_list = []
    white_rook_list = []
    black_pawn_list = []
    black_knight_list = []
    black_bishop_list = []
    black_rook_list = []
    for i in range(8):
        black_pawn_list.append(Pawn('black', 6, i))
        white_pawn_list.append(Pawn('white', 1, i))
        (chessBoard.get_board())[6][i] = black_pawn_list[i]
        (chessBoard.get_board())[1][i] = white_pawn_list[i]
    black_knight_list.append(Knight('black', 7, 1))
    black_knight_list.append(Knight('black', 7, 6))
    white_knight_list.append(Knight('white', 0, 1))
    white_knight_list.append(Knight('white', 0, 6))
    (chessBoard.get_board())[7][1] = black_knight_list[0]
    (chessBoard.get_board())[7][6] = black_knight_list[1]
    (chessBoard.get_board())[0][1] = white_knight_list[0]
    (chessBoard.get_board())[0][6] = white_knight_list[1]
    black_bishop_list.append(Bishop('black', 7, 2))
    black_bishop_list.append(Bishop('black', 7, 5))
    white_bishop_list.append(Bishop('white', 0, 2))
    white_bishop_list.append(Bishop('white', 0, 5))
    (chessBoard.get_board())[7][2] = black_bishop_list[0]
    (chessBoard.get_board())[7][5] = black_bishop_list[1]
    (chessBoard.get_board())[0][2] = white_bishop_list[0]
    (chessBoard.get_board())[0][5] = white_bishop_list[1]
    black_rook_list.append(Rook('black', 7, 0))
    black_rook_list.append(Rook('black', 7, 7))
    white_rook_list.append(Rook('white', 0, 0))
    white_rook_list.append(Rook('white', 0, 7))
    (chessBoard.get_board())[7][0] = black_rook_list[0]
    (chessBoard.get_board())[7][7] = black_rook_list[1]
    (chessBoard.get_board())[0][0] = white_rook_list[0]
    (chessBoard.get_board())[0][7] = white_rook_list[1]
    (chessBoard.get_board())[7][3] = King('black', 7, 3)
    (chessBoard.get_board())[7][4] = Queen('black', 7, 4)
    (chessBoard.get_board())[0][3] = King('white', 0, 3)
    (chessBoard.get_board())[0][4] = Queen('white', 0, 4)
    for j in range(8):
        print(chessBoard.get_board()[j])
