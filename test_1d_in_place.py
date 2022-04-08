#!/usr/bin/env python3

from Board import Board

from os import system, name
from time import sleep

def clear():

   if name == 'nt':
      _ = system('cls')

   else:
      _ = system('clear')

BOARD_FILE = 'data/move_1_across_1d_array.json'

board = Board(init_file=BOARD_FILE)

board.iterations(5)

