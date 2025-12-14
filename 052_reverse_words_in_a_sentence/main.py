# Exercise 52: Reverse Words in a Sentence

sentence = "Lkhibra Academy is great"

# Step 1: Split the sentence into a list of words
word_list = sentence.split()

# Step 2: Reverse the order of the words using slicing [::-1]
reversed_list = word_list[::-1]

# Step 3: Join the words back into a single string, using a space (' ') as the separator
reversed_sentence = " ".join(reversed_list)

# Print the final result
print(reversed_sentence)