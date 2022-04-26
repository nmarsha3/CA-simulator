#!/usr/bin/env python3

from Board import Board

BOARD_FILE = 'data/wireworld_inverter_forward.json'

board = Board(init_file=BOARD_FILE)

board.iterations(9, 1.5)
