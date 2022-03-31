from collections import namedtuple
import json

Cell = namedtuple("Cell", "state next_state output")

class Board:

   def __init__(self, neighborhood="von neumann", dimension=1, length=5):
      # Take in variables
      self.neighborhood = neighborhood
      self.dimension = dimension
      self.length = length
      self.transitions = []

      # Build the board
      self.board = self.buildEmptyBoard(dimension, length)

   def buildEmptyBoard(self, dim, length):
      if dim == 1:
         return [Cell(0, 0, 0) for i in range(length)]
      
      return [self.buildBoard(dim-1, length) for i in range(length)]

   def buildJsonBoard(self, json_file):

      # Open file
      f = open(json_file)
      data = json.load(f)

      # Get dimension, length, init_states, transitions
      self.dimension = data["dimension"]
      self.length = data["length"]
      init_states = data["init_state"]
      self.transitions = data["transitions"]

      # Build board in init state
      return []
   
   def iterate():
      pass

   def printBoard(self):
      print(self.board)

   def setNeighborhood(self, neighborhood):
      self.neighborhood = neighborhood
   
   def setDimension(self, dimension):
      self.dimension = dimension

   
