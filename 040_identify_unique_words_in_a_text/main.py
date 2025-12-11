# Exercise 40: Identify Unique Words in a Text
# Objective: Demonstrate that Python sets automatically remove duplicate elements.

# 1. Input Text
text = "Python is amazing and Python is powerful"

# 2. Preparation (Conversion)
# The .split() method breaks the string into a list of words, using spaces as separators.
word_list = text.split()
# Example: ['Python', 'is', 'amazing', 'and', 'Python', 'is', 'powerful']

# 3. Core Logic: Convert the list of words into a set.
# The set() constructor automatically processes the list and discards all duplicates,
# leaving only the unique words.
unique_words = set(word_list)

# 4. Output
# Note: Sets are UNORDERED, so the output sequence may change between runs,
# but the contents (the unique words) will always be correct.
print(unique_words)