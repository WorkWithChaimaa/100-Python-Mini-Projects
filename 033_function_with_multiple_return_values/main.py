# Exercise 33: Function with Multiple Return Values
def calculate(x, y):
    s = x + y
    p = x * y
    return s, p
total, product = calculate(5, 3)

print(f"Sum: {total}, Product: {product}")

