#!/usr/bin/env python3

from Board import Board

BOARD_FILE = 'data/move_1_across_1d_array.json'

board = Board(init_file=BOARD_FILE)

print(board)

for i in range(10):
    board.iterate()
    print(board)
