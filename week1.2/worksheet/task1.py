# Worksheet 1.2: Task 1 Solution
import sys

try:
    print("Enter an integer grade in the range 0 to 100: ", end="")
    number = int(input())
except ValueError:
    print("Error: Grade must be an integer between 0 and 100", file=sys.stderr)
    sys.exit(1)

if number < 0 or number > 100:
    print("Error: Grade must be an integer between 0 and 100", file=sys.stderr)
    sys.exit(1)

if 0 <= number <= 39:
    print(f"{number} is a Fail")
elif 40 <= number <= 69:
    print(f"{number} is a Pass")
elif 70 <= number <= 100:
    print(f"{number} is a Distinction")
    