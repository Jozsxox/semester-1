# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','hamster','goldfish']

not_fish = [item for item in animals if item != 'goldfish']

print(not_fish)

num = ['1','2','3','4','5']
not_3 = [item for item in num if item != "3"]
print(not_3)
# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same