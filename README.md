# CA-simulator

## Members
Nick Marshall, Jacob Mazur, Mary McCann

## Project Idea
We will be building a software emulator for cellular automata. The program will run in a terminal and provide a visual representation of the state of the automaton being emulated. A major part of the project will involve determining how to read in a text representation of a CA, store the automaton state in memory, and simulate the behavior from the provided state.

## Instructions for Running the Code
In order to execute the code, use the test files we have provided which implement cellular automata of various dimensions. For example, run ```./test_1d.py``` to see a simple 1D CA that fills in cells with 1s from left to right. The following test files are provided:
- test_1d.py
- test_2d.py
- test_3d.py
- test_game_of_life.py

Alternatively, you can interface with the Board class directly inside a python shell:
- ```$ python3```
- ```>>> from Board import Board```
- ```>>> b = Board(dimension=2,length=5)```
  - Creates an empty 5x5 Board
- ```>>> b = Board(init_file="data/game_of_life_blinker.json")```
  - Creates a Board from a specified JSON config file (data/game_of_life_blinker.json in this case)
- ```>>> b.addBorder()```
  - Adds a border of $ cells at the edges of the board
- ```print(board)```
  - Prints the current state of the board
- ```>>> b.iterate()```
  - Iterates the board by one generation
- ```>>> b.iterations(5, .5)```
  - Iterates the board 5 times with .5 seconds per generation
## Documentation
First Progress Report:
- [Link to Google Doc](https://docs.google.com/document/d/1y39QktQpo54GqGPqDYo-eAqYU1BLYIeka3R_D4U9WtE/edit?usp=sharing)

Second Progress Report:
- [Link to Google Doc](https://docs.google.com/document/d/1_EfxgBAqRC_GcodutS2VJ86j_b47td_2m0iGsq_8L4I/edit?usp=sharing)

Presentation Slides
- [Link to Google Slides](https://docs.google.com/presentation/d/1oNxd8QKMqQlQdnTD0Dkyd0wEhAuaZhLaGBBZFpyPTvA/edit?usp=sharing)

Final Report 
- [Link to PDF]()
