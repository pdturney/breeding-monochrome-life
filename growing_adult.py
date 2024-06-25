#
#
# Peter Turney, June 21, 2024
#
# growing_adult.py
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
# - make a torus
rule_name = "B3/S23"          # - use the Game of Life rule
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
# Write top_adult in the Golly window.
#
# - golly.setcell(x, y, state) -- x is horizontal, y is vertical
# - top_seed[i][j] -- i is rows (vertical), j is cols (horizontal)
# - therefore we need to swap i and j, to rotate the image
golly.new("") # - clear the screen
# 0 = white (255,255,255)
# 1 = black (0,0,0)
golly.setcolors([0,255,255,255,1,0,0,0])
rows = len(top_adult)
cols = len(top_adult[0])
# - show the seed growing in 3 steps
# - step 0 -- the initial state
for i in range(rows):
  for j in range(cols):
    colour = top_adult[i][j]
    golly.setcell(j - 30, i - 30, colour)
# - steps: 50, 100
for step in range(2):
  time.sleep(10)
  golly.run(50)
#
#