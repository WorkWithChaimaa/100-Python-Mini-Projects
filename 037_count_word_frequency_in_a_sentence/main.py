# Exercise 37: Word Frequency Counter

sentence = "Python is great and Python is fun"

# 1. Prepare the Text: Split the string into a list of words
word_list = sentence.split() # ['Python', 'is', 'great', 'and', 'Python', 'is', 'fun']

# 2. Initialize the counter dictionary
word_counts = {}

# 3. Loop and Count (The Core Logic)
for word in word_list:
    if word in word_counts:
        # If the word exists, increase its count by 1
        word_counts[word] += 1
    else:
        # If the word is new, add it to the dictionary and set its count to 1
        word_counts[word] = 1

print(word_counts)
