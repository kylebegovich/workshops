#######################################
# Problem 1: broken typewriter:
#######################################
# A typewriter is broken and the letter ‘e’ can’t be typed out. Instead, it will print a space. For ex:
#   Original: “i have a dream” →
#   Typed:    “I hav  a dr am”.

# Given a string typed on this machine and a dictionary of words, return all possible original sentences it could be.

# Assumptions:
# Single Sentence
# No Symbols
# Case-insensitive
# One space between words in original


dictionary = {"i", "have", "a", "dream", "howdy", "yall", "aeon", "on", "aeaea", "aea"}

test1_pre = "I hav  a dr am"
test1_post = ["i have a dream"]

test2_pre = "howdy yall"
test2_post = ["howdy yall"]

test3_pre = "a on"
test3_post = ["a on", "aeon"]

test4_pre = "fvabjwhklj g"
test4_post = []

test5_pre = "a a a a a a a a a"
test5_post = ["aea a", "a aea", "a a a", "aeaea"]



def broken_type_step(split_string, index, curr_sen):

    # determines if a space is an e or a space
    # base case
    if index >= len(split_string):
        return [curr_sen[1:]]

    # recursive case, index < len(split_string)
    curr_word = split_string[index]
    new_sentences = []

    # is curr_word in dictionary
    if curr_word in dictionary:
        new_sen = curr_sen + " " + curr_word
        new_sentences.extend(broken_type_step(split_string, index + 1, new_sen))

    # is curr_word merged with another individual word in the dictionary
    if index + 1 < len(split_string):
        next_word = split_string[index + 1]
        if (curr_word + "e" + next_word) in dictionary:
            new_sen = curr_sen + " " + curr_word + "e" + next_word
            new_sentences.extend(broken_type_step(split_string, index + 2, new_sen))
    return new_sentences


def broken_type(typed):
    # returns list of strings
    split_string = typed.lower().split(" ")
    return broken_type_step(split_string, 0, "")


print(test1_pre, "\n", broken_type(test1_pre), " = ", test1_post)
print()
print(test2_pre, "\n", broken_type(test2_pre), " = ", test2_post)
print()
print(test3_pre, "\n", broken_type(test3_pre), " = ", test3_post)
print()
print(test4_pre, "\n", broken_type(test4_pre), " = ", test4_post)

# print(test5_pre, "\n", broken_type(test5_pre), " = ", test5_post)

#######################################





print("\n#######################################")






#######################################
# Problem 2:
#######################################
# Given a 2D matrix of booleans, "1" means there’s “land” at that tile, and "0" means there’s “water” at that tile. Assign a height to every tile such that:
# Water tiles are always height = 0
# Two adjacent tiles differ by <= 1

# Report the height of the highest peak you can possibly build according to these rules

# Assumptions:
# Diagonal-neighbors are not adjacent
# Report “-1” or “Infinite” if only land
# No constraints at edges of the matrix
# Square Map of booleans


test1_pre = [[0,1,1],
              [1,1,1],
              [1,1,1]]
test1_post = 4

test2_pre = [[1,1],
              [1,1]]
test2_post = -1

test3_pre = [[0,0,0],
              [0,0,0],
              [0,0,0]]
test3_post = 0

test4_pre = [[1,1,1],
              [1,0,1],
              [1,1,1]]
test4_post = 2


def tallest_peak_step(seen, discovered, bool_map):
  new_discovered = set()
  for i,j in discovered:
    if i > 0:
      if (i-1,j) not in seen:
        new_discovered.add((i-1,j))
    if i+1 < len(bool_map):
      if (i+1,j) not in seen:
        new_discovered.add((i+1,j))
    if j > 0:
      if (i,j-1) not in seen:
        new_discovered.add((i,j-1))
    if j+1 < len(bool_map):
      if (i,j+1) not in seen:
        new_discovered.add((i,j+1))

  return new_discovered

def tallest_peak(bool_map):
  water_tiles = set()
  for i in range(len(bool_map)):
    for j in range(len(bool_map)):
      if bool_map[i][j] == 0:
        water_tiles.add((i, j))

  tallest_peak = -1
  seen = set()
  discovery_set = water_tiles
  while len(discovery_set) > 0:
    tallest_peak += 1
    seen = seen.union(discovery_set)
    discovery_set = tallest_peak_step(seen, discovery_set, bool_map)

  return tallest_peak

print()
print([print(line) for line in test1_pre], "\n", tallest_peak(test1_pre), "=",  test1_post)
print()
print([print(line) for line in test2_pre], "\n", tallest_peak(test2_pre), "=",  test2_post)
print()
print([print(line) for line in test3_pre], "\n", tallest_peak(test3_pre), "=",  test3_post)
print()
print([print(line) for line in test4_pre], "\n", tallest_peak(test4_pre), "=", test4_post)
