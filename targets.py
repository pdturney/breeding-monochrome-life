#
#
# Peter Turney, June 20, 2024
#
# targets.py
#
# A variety of matrices of 60 x 60 that are intended
# to provide targets for an evolutionary algorithm.
# The evolutionary algorithm randomly writes numbers
# (representing different colours) and receives a
# score based on how well the given target matches
# the random colours of the algorithm. The algorithm
# gets feedback on the number of colours that it has
# matched. Through this feedback, it should be able
# to guess some of the colours.
#
#
import golly
import numpy as np
#
rows   = 60
cols   = 60
white  = 0
black  = 1
#
# - scoring the targets
# - given two matrices, measure how much they agree
def compare(matrix_1, matrix_2):
  score = 0
  for i in range(rows):
    for j in range(cols):
      # - black on black = 1 point (black target + black adult)
      if ((matrix_1[i, j] == black) and (matrix_2[i, j] == black)):
        score += 1
      # - white on white = 1 point
      if ((matrix_1[i, j] == white) and (matrix_2[i, j] == white)):
        score += 1
      # - white on black or black on white = -1 point
      if ((matrix_1[i, j] == white) and (matrix_2[i, j] == black)):
        score -= 1
      if ((matrix_1[i, j] == black) and (matrix_2[i, j] == white)):
        score -= 1
      # - white = -0.02
      # - process both matrix_1 and matrix_2, since only
      #   one of the two matrices will change -- the one
      #   that is the target will never have white
      if ((matrix_1[i, j] == white) or (matrix_2[i, j] == white)):
        score -= 0.002
  golly.show("score=" + str(score))
  return score
#
# - show target
# - show the target pattern that the seed should evolve towards
def show_target(matrix):
  # - make a box of 60 x 60 centewhite on the origin
  # - golly.setcell(x, y, state) -- x is horizontal, y is vertical
  # - top_seed[i][j] -- i is rows (vertical), j is cols horizontal
  # - therefore we need to swap i and j, to rotate the image
  [left, top, width, height] = [-30, -30, 60, 60]
  for i in range(height):
    for j in range(width):
      colour = matrix[i, j]
      golly.setcell(j + top, i + left, colour)
  return
#
# - target_1
def target_1():
  matrix_1 = np.zeros([rows, cols], dtype=int)
  # - four boxes
  # - white, black
  # - black, white
  for i in range(rows):
    for j in range(cols):
      if (j >= 0) and (j < 30) and (i >= 0) and (i < 30):
        matrix_1[i, j] = white
      if (j >= 0) and (j < 30) and (i >= 30) and (i < 60):
        matrix_1[i, j] = black
      if (j >= 30) and (j < 60) and (i >= 0) and (i < 30):
        matrix_1[i, j] = black
      if (j >= 30) and (j < 60) and (i >= 30) and (i < 60):
        matrix_1[i, j] = white
  return matrix_1
#
# - target 2
def target_2():
  matrix_2 = np.zeros([rows, cols], dtype=int)
  # - vertical stripes of white and black
  for i in range(rows):
    for j in range(cols):
      if (j >= 0) and (j < 30):
        matrix_2[i, j] = white
      if (j >= 30) and (j < 60):
        matrix_2[i, j] = black
  return matrix_2
#
# - target 3
def target_3():
  matrix_3 = np.zeros([rows, cols], dtype=int)
  # - vertical stripes of white, black, white
  for i in range(rows):
    for j in range(cols):
      if (j >= 0) and (j < 20):
        matrix_3[i, j] = white
      if (j >= 20) and (j < 40):
        matrix_3[i, j] = black
      if (j >= 40) and (j < 60):
        matrix_3[i, j] = white
  return matrix_3
#
# - target 4
def target_4():
  matrix_4 = np.zeros([rows, cols], dtype=int)
  # - vertical stripes of white, black, white, black
  for i in range(rows):
    for j in range(cols):
      if (j >= 0) and (j < 15):
        matrix_4[i, j] = white
      if (j >= 15) and (j < 30):
        matrix_4[i, j] = black
      if (j >= 30) and (j < 45):
        matrix_4[i, j] = white
      if (j >= 45) and (j < 60):
        matrix_4[i, j] = black
  return matrix_4
#
# - target 5
def target_5():
  matrix_5 = np.zeros([rows, cols], dtype=int)
  ##########
  # r /\ r #
  #  /  \  #
  # / b  \ #
  #/      \#
  #   /\   #
  #  /  \  #  - 60 x 60
  # / r  \ #  - 0 = white, 1 = black
  #/      \#
  ##########
  # - top left
  for i in range(30):
    for j in range(30):
      if (i >= j):
        matrix_5[i, 29 - j] = white
      else:
        matrix_5[i, 29 - j] = black
  # - top right
  for i in range(30):
    for j in range(30):
      if (i >= j):
        matrix_5[i, 30 + j] = white
      else:
        matrix_5[i, 30 + j] = black
  # - bottom left
  for i in range(30):
    for j in range(30):
      if (i > j):
        matrix_5[30 + i, 29 - j] = black
      else:
        matrix_5[30 + i, 29 - j] = white
  # - bottom right
  for i in range(30):
    for j in range(30):
      if (i > j):
        matrix_5[30 + i, 30 + j] = black
      else:
        matrix_5[30 + i, 30 + j] = white
  #
  return matrix_5
#
#
#