#!/usr/bin/env python3

from Board import Board

BOARD_FILE = 'data/game_of_life_chaos.json'

board = Board(init_file=BOARD_FILE)

board.iterations(23, 0.5)
