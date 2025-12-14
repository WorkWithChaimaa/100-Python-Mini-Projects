# Exercise 55: Remove Extra Spaces from a String

messy_string = "   \n\t  Hello   World !  This  is messy. \t "
stripped_string = messy_string.strip()
split_string = stripped_string.split()
joined_list = " ".join(split_string)
print(joined_list)