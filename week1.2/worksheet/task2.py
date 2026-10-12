# Worksheet 1.2: Task 2 Solution
import sys

user_input = input("Enter 5 float values: ")
original_list = user_input.split()

number_list = []
for o in original_list:
    number_list.append(float(o))

if len(number_list) == 0:
    print("Error: no numbers provided.",file = sys.stderr)
    sys.exit(1)

minimum = min(number_list)
maximum = max(number_list)
mean = sum(number_list)/len(number_list)

number_list.sort()
count = len(number_list)
if count % 2 == 1:
    median = number_list[count//2]
else:
    a = number_list[count//2 - 1]
    b = number_list[count//2]
    median = (a + b)/2

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")