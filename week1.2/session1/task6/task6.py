# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {"megadeth": "rust in peace", "blossoms": "cool like you"}
print(music)
# Pretty-print the data structure
import pprint
pprint.pprint(music)

# Display details of one album recorded by a specific artist
print(music["megadeth"])