# Exercise 44: Find the Unique Visitors on a Website

visitors = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.1",
    "192.168.1.3",
    "192.168.1.2",
]
unique_visitors = set(visitors)
num_unique_visitors = len(unique_visitors)
print(f"Unique visitors: {num_unique_visitors}")