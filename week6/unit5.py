# Week 6, Unit 5: Exercise (Python_1)

# The non-standard library py-sudoku offers the possibility to create your own sudokus. Follow the above link and
# have a look how to install and use the library. Install the library and create a new sudoku with a difficulty of
# 0.7 Display the sudoku and the solution of the sudoku.

# pip install py-sudoku

from sudoku import Sudoku
puzzle = Sudoku(3).difficulty(0.7)
puzzle.show()