#
#
# Peter Turney, June 21, 2024
#
# view.py
#
# This program reads the file that had the highest
# score in the final population. The result is
# displayed by sending the information to Golly.
#
#
import golly
import pickle
import time
import targets as targ
#
# Standard Game of Life, white background, black foreground.
#
white  = 0
black  = 1
#
# - make a torus
rule_name = "Immigration"     # - use the Immigration rule
max_dimension = ":T60,60"     # - Torus of 60 x 60
golly.autoupdate(True)
golly.new(rule_name)
# - Immigration:T60,60 makes a torus of 60 x 60
# - a torus is finite, which means the live cells should
#   be packed more densely and uniformly, which is good
golly.setrule(rule_name + max_dimension)
#
data_file = open("top_result_figures1234.bin", "rb")
data = pickle.load(data_file)
data_file.close()
[top_score, top_seed, top_adult] = data
#
# Write top_score in the bar at the top of the Golly window.
#
golly.show("score = " + str(top_score))
#
# Write the target in the Golly window.
#
# - target_1() is the matrix with four boxes:
#     white, black
#     black, white
# - target_2() is the matrix with two vertical bars:
#     white, black
# - target_3() is the matrix with three vertical bars:
#     white, black, white
# - target_4() is the matrix with four vertical bars:
#     white, black, white, black
golly.new("") # - clear the screen
golly.setcolors([white,255,255,255,black,0,0,0])
matrix = targ.target_3()
targ.show_target(matrix)
time.sleep(10)
#
# Write top_seed in the Golly window.
#
# - golly.setcell(x, y, state) -- x is horizontal, y is vertical
# - top_seed[i][j] -- i is rows (vertical), j is cols horizontal
# - therefore we need to swap i and j, to rotate the image
golly.new("") # - clear the screen
golly.setcolors([white,255,255,255,black,0,0,0])
rows = len(top_seed)
cols = len(top_seed[0])
for i in range(rows):
  for j in range(cols):
    colour = top_seed[i][j]
    golly.setcell(j - 10, i - 10, colour)
time.sleep(10)
#
# Write top_adult in the Golly window.
#
# - golly.setcell(x, y, state) -- x is horizontal, y is vertical
# - top_seed[i][j] -- i is rows (vertical), j is cols (horizontal)
# - therefore we need to swap i and j, to rotate the image
golly.new("") # - clear the screen
golly.setcolors([white,255,255,255,black,0,0,0])
rows = len(top_adult)
cols = len(top_adult[0])
for i in range(rows):
  for j in range(cols):
    colour = top_adult[i][j]
    golly.setcell(j - 30, i - 30, colour)
time.sleep(10)
#
#