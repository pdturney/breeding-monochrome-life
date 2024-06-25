#
#
# Peter Turney, June 22, 2024
#
# run_figures1234.py
#
#
# NOTE: This Python program requires Golly, the Game of Life
# software. See https://en.wikipedia.org/wiki/Golly_(program)
# and https://golly.sourceforge.io/.
#
# NOTE: This program requires Immigration.rule, which defines
# the rules for a variation on the Game of Life. The variation
# preserves the general patterns of the Game of Life, but it
# adds colours to the patterns, making it possible to see
# interactions that would otherwise be invisible.
#
#
# IMPORT
# ======
#
import golly
import monochrome as mono
import random as rand
import numpy as np
import targets as targ
import time
import copy
import pickle
import os
#
#
# PARAMETERS
# ==========
#
# Standard Game of Life, white background, black foreground.
#
white  = 0
black  = 1
#
# Run a series of experiments.
#
population_size = 1000  # fixed population: each new birth requires one death
new_matrices = 1000001  # randomly choose a matrix from the population and
                        # mutate it
num_steps =        100  # number of steps for the Game of Life
prob_black =      0.30  # probability of black
prob_mutation =   0.05  # probability of switching between black and white
matrix_offset_x =  -10  # shift the 20 x 20 matrix by 10 to the left
matrix_offset_y =  -10  # shirt the 20 x 20 matrix by 10 upwards
#
#
# STEPS
# =====
#
# - make a torus
rule_name =     "B3/S23"      # - use the Game of Life rule
max_dimension = ":T60,60"     # - Torus of 60 x 60
golly.autoupdate(True)
golly.new(rule_name)
# - Immigration:T60,60 makes a torus of 60 x 60
# - a torus is finite, which means the live cells should
#   be packed more densely and uniformly, which is good
golly.setrule(rule_name + max_dimension)
# - start a log
log_path = "log_file_figs1234.txt"
log_file = open(log_path, "w+")
# - the population size is fixed at population_size
population = []
# - set the target for determining fitness
# - the fitness of an organism is determined by how well it
#   matches with the given target
# - matching with the target means having a pattern of colours
#   that is similar to the target's pattern of colours
golly.setcolors([white,255,255,255,black,0,0,0])
target = targ.target_3()
# - create generation zero
# - generation zero is random; no selection has been applied yet
for i in range(population_size):
  # - randomly sample a small number of seed matrices
  sample_size = 10
  sample_set  = []
  # - collect 10 samples and then extract the best sample
  for sample in range(sample_size):
    # - make a random seed matrix
    seed_matrix = mono.make_seed_matrix(prob_black)
    # - grow the matrix
    adult_matrix = mono.grow_matrix(seed_matrix, num_steps)
    # - measure how well the adult matches with the target
    target_score = targ.compare(target, adult_matrix)
    # - append sample
    sample_set.append([seed_matrix, adult_matrix, target_score])
  # - sort the list (sample_set) by the third element (target_score)
  sorted_samples = sorted(sample_set, key=lambda tup: tup[2])
  # - best_sample is the last tuple in the list of sorted_samples
  best_sample = sorted_samples[-1]
  # - store the vector [seed, adult, target]
  population.append(best_sample)
#
# - now we apply mutation and selection
# - we randomly sample two individuals in the population
# - one of the two individuals is randomly mutated using
#   randomize_one_box()
# - the fitter of the two individuals enters or remains in the
#   population and the less fit individual is removed
#
for j in range(new_matrices):
  # - randomly sample two members of the population
  position1 = rand.randint(0, population_size - 1)
  position2 = rand.randint(0, population_size - 1)
  while (position1 == position2):
    position2 = rand.randint(0, population_size - 1)
  # - find their degree of match with the target
  [seed1, adult1, score1] = population[position1]
  [seed2, adult2, score2] = population[position2]
  # - select the matrix with the lower match and
  #   replace it with a mutated version of the matrix
  #   with the higher match
  # - that is, the less fit (lower match) matrix dies
  #   and is replaced with a slightly modified version
  #   of the more fit matrix (a new child)
  # - since the new child is a mutation, it might be less
  #   fit than the matrix it is replacing, but that's OK
  if (score1 > score2):
    # - score1 is better than score2, therefore keep 
    #   [seed1, adult1, score1]
    # - replace [seed2, adult2, score2] with a mutated
    #   version of [seed1, adult1, score1]
    seed3 = copy.deepcopy(seed1)
    seed4 = mono.mutate_seed(seed3, prob_mutation)
    adult2 = mono.grow_matrix(seed4, num_steps)
    score2 = targ.compare(target, adult2)
    population[position2] = [seed4, adult2, score2]
  else:
    # - score2 is better than score1, therefore keep 
    #   [seed2, adult2, score2]
    # - replace [seed1, adult1, score1] with a mutated
    #   version of [seed2, adult2, score2]
    seed3 = copy.deepcopy(seed2)
    seed4 = mono.mutate_seed(seed3, prob_mutation)
    adult1 = mono.grow_matrix(seed4, num_steps)
    score1 = targ.compare(target, adult1)
    population[position1] = [seed4, adult1, score1]
#
# - report the best score
# - start with the first score
[seed, adult, score] = population[0]
best_score_so_far = score
for k in range(population_size):
  [seed, adult, score] = population[k]
  log_file.write(str(k) + " fitness " + str(score) + "\n")
  if (score >= best_score_so_far):
    best_score_so_far = score
    top_score = score
    top_seed  = seed
    top_adult = adult
log_file.close()
# - store the top data
data = [top_score, top_seed, top_adult]
data_file = open("top_result_figures1234.bin", "wb")
pickle.dump(data, data_file)
data_file.close()
#
#