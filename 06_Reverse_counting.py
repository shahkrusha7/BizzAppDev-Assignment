"""
Reverse Counting (Recursion Check)

Problem:
Print numbers from 1000 down to 1 without using loops or built-in functions like range().

Approach:
Use a recursive function that prints the current number, then calls itself with the number minus one.
"""

def reverse_count(n):
    if n<1:
        return
    print(n)
    reverse_count(n-1)

reverse_count(1000)