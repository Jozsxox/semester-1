# Worksheet 1.2: Task 1 Solution
import sys
try:
    number = int(input("Enter an integer grade in the range 0 to 100: "))
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100.")
if 0 < number < 39:
    print(f"Fail")
elif 40 < number < 69:
    print(f"Pass")
elif 70 < number < 100:
    print(f"Distinction")
    