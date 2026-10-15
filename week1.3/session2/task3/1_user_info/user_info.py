# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
name = input("What's your name?")
age = input("How old are you?")
favoriate_colour = input("What's your favoriate colour?")

# Open a file called 'user_info.txt' for reading

# Write each piece of information to the file, each on a new line.
with open("user_info.txt","w") as f:
    f.write(name +"\n")
    f.write(age +"\n")
    f.write(favoriate_colour + "\n")
# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
