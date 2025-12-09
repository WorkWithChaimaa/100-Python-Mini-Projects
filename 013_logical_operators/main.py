# Exercise 13: Use Logical Operators

# 1. Define two boolean variables to use in the logical expressions
# We use the built-in keywords True and False
condition_a = True
condition_b = False

# 2. Use the 'and' operator (Logical Conjunction)
# Result is True only if BOTH sides are True.
print(f"{condition_a} and {condition_b}: {condition_a and condition_b}")

# 3. Use the 'or' operator (Logical Disjunction)
# Result is True if AT LEAST ONE side is True.
print(f"{condition_a} or {condition_b}: {condition_a or condition_b}")

# 4. Use the 'not' operator (Logical Negation)
# The 'not' operator reverses the Boolean value.
print(f"Not {condition_a}: {not condition_a}")