# Exercise 53: Extract Hashtags from a Social Media Post

social_media_post_string = "Loving #Python and #Coding at #LkhibraAcademy"

# Step 1: Split the sentence into a list of words
list_of_words = social_media_post_string.split(" ")
# Result: ['Loving', '#Python', 'and', '#Coding', 'at', '#LkhibraAcademy']

# Step 2: Initialize an empty list to store the results
hashtags = []

# Step 3: Loop through each word and check the starting character
for word in list_of_words:
    # Check if the word starts with the '#' symbol (using index 0)
    if word[0] == "#":
        # If it does, add the word to the hashtags list
        hashtags.append(word)

# Step 4: Print the final result
print(f"Hashtags: {hashtags}")