from collections import namedtuple
import json

Cell = namedtuple("Cell", "state next_state output")

class Board:

   def __init__(self, neighborhood="von neumann", dimension=1, length=5):
      # Take in variables
      self.neighborhood = neighborhood
      self.dimension = dimension
      self.length = length

      # Build the board
      self.board = self.buildBoard(dimension, length)

   def buildEmptyBoard(self, dim, length):
      if dim == 1:
         return [Cell(0, 0, 0) for i in range(length)]
      
      return [self.buildBoard(dim-1, length) for i in range(length)]

   def buildJsonBoard(self, json_file):

      f = open(json_file)
      data = json.load(f)

      for i in data

   
   def printBoard(self):
      print(self.board)

   def setNeighborhood(self, neighborhood):
      self.neighborhood = neighborhood
   
   def setDimension(self, dimension):
      self.dimension = dimension

   
