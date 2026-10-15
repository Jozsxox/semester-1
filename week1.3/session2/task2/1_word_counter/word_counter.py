# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210

with open("story.txt","r") as f:
    content = f.readlines()
    char_total=[]
    for content in content:
        words = content.split()
        char_total.extend(words)
    print(len(char_total))


with open("story2.txt","r") as f:
    content2= f.read()
    words2 = content2.split()
    word_count = len(words2)
    print(word_count)