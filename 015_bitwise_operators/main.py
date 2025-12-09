# Exercise 15: Use Bitwise Operators

# 1. Define two numbers for the bitwise operations
# Binary representations: 5 (0101) and 3 (0011)
num1 = 5
num2 = 3

# 2. Bitwise AND (&)
# Compares bits: 1 & 1 = 1, otherwise 0.
# 0101 & 0011 = 0001 (1)
print(f"{num1} & {num2} = {num1 & num2}")

# 3. Bitwise OR (|)
# Compares bits: 1 | 0 = 1. Result is 1 if either bit is 1.
# 0101 | 0011 = 0111 (7)
print(f"{num1} | {num2} = {num1 | num2}")

# 4. Bitwise XOR (^)
# Compares bits: 1 ^ 1 = 0. Result is 1 only if the bits are DIFFERENT.
# 0101 ^ 0011 = 0110 (6)
print(f"{num1} ^ {num2} = {num1 ^ num2}")

# 5. Bitwise Left Shift (<< 1)
# Shifts bits one position left (equivalent to multiplying by 2).
# 0101 << 1 = 1010 (10)
print(f"{num1} << 1 = {num1 << 1}")

# 6. Bitwise Right Shift (>> 1)
# Shifts bits one position right (equivalent to integer dividing by 2).
# 0101 >> 1 = 0010 (2)
print(f"{num1} >> 1 = {num1 >> 1}")