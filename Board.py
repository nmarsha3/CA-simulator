from collections import namedtuple
import json
import numpy as np

Cell = namedtuple("Cell", "state next_state output")

class Board:

   def __init__(self, neighborhood="von neumann", dimension=1, length=5, init_file=None):
      # Take in variables
      self.neighborhood = neighborhood
      self.dimension = dimension
      self.length = length
      self.transitions = []

      # Build the board
      if init_file is not None:
         self.board = np.asarray(self.buildJsonBoard(init_file))
      else:
         self.board = np.asarray(self.buildEmptyBoard(dimension, length))

   def __str__(self):

      if self.dimension == 1:
         out_str =  '-'*(4*self.length+1) + '\n'
         out_str += '| ' + ' | '.join([str(cell[2]) for cell in self.board]) + ' |\n'
         out_str += '-'*(4*self.length+1)
         return out_str

      elif self.dimension == 2:
         out_str =  '-'*(4*self.length+1)
         for brd in self.board:
            out_str += '\n| ' + ' | '.join([str(cell[2]) for cell in brd]) + ' |\n'
            out_str += '-'*(4*self.length+1)
         return out_str

      else:
         return str(self.board)

   def buildEmptyBoard(self, dim, length):
      if dim == 1:
         return [Cell('0','0','0') for i in range(length)]
      
      return [self.buildEmptyBoard(dim-1, length) for i in range(length)]
   
   def buildJsonBoard(self, json_file):

      # Open file
      f = open(json_file)
      data = json.load(f)

      # Get dimension, length, init_states, transitions
      self.dimension = data["dimension"]
      self.length = data["length"]
      init_states = data["init_states"]
      init_outputs = data["init_outputs"]
      self.transitions = data["transitions"]

      def recursive_zip(a,b):
         if type(a) is not list and type(b) is not list:
            return Cell(a,'',b)
         return [recursive_zip(i,j) for i,j in zip(a,b)] 
      
      # Build board with initial states and outputs
      return recursive_zip(init_states, init_outputs)
      
   def iterate(self):

      def recursive_iterate(brd, idx=[]):
         if self.dims == (3,):
            print(tuple(idx), self.board[tuple(idx)])
         else:
            for i in range(len(board)):
               recursive_iterate(brd[i],idx+[i])

      recursive_iterate(self.board)

   def addBorder(self):
      '''Adds a border of $ characters around the board, overwriting the outermost cells'''

      def recursive_iterate(brd, idx=[]):
         if brd.shape == (3,):
            for i in idx:
               if i == 0 or i == self.length-1:
                  self.board[tuple(idx)] = np.asarray(Cell('$','','$'))
                  break
         else:
            for i in range(len(brd)):
               recursive_iterate(brd[i],idx+[i])

      recursive_iterate(self.board)

   def printBoard(self):
      print(self.board)

   def setNeighborhood(self, neighborhood):
      self.neighborhood = neighborhood
   
   def setDimension(self, dimension):
      self.dimension = dimension

# vim: set sts=3 sw=3 ts=6 expandtab ft=python: 
