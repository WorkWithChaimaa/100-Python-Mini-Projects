# Exercise 43: Find the Most Frequent Word in a List

reviews = [
    "excellent service",
    "good quality",
    "excellent product",
    "excellent quality",
    "good service",
    "excellent experience"
]

counter = {}
for review in reviews:
    string_sentence = review.split()
    for word in string_sentence:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
highest_frequency = max(counter, key= counter.get)
print(f"Most frequent word: {highest_frequency}")
