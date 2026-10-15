# Week 1.3, Session 1: Task 6b

values = [1,4,2,6,3,7]

print(values)

newval = []
for i in values:
    if i % 2 == 0:
        newval.append(2 * i)
    else:
        newval.append(i)

print(newval)


fruit = ['2','5','78','21']
print(fruit)

new_val = []
for i in fruit:
    if i % 2 == 0:
        new_val.append(2 * i)
    else:
        new_val.append(i)
print(new_val)
# write the list comprehension equivalent to the `for` loop

