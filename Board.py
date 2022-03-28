from collections import namedtuple

Cell = namedtuple("Cell", "state next_state output")

class Board:

   def __init__(self, neighborhood="von neumann", dimension=1, length=5):
      # Take in variables
      self.neighborhood = neighborhood
      self.dimension = dimension
      self.length = length

      # Build the board
      self.board = self.buildBoard(dimension, length)

   def buildBoard(self, dim, length):
      if dim == 1:
         return [Cell(0, 0, 0) for i in range(length)]
      
      return [self.buildBoard(dim-1, length) for i in range(length)]

   def printBoard(self):
      print(self.board)

   def setNeighborhood(self, neighborhood):
      self.neighborhood = neighborhood
   
   def setDimension(self, dimension):
      self.dimension = dimension

   
