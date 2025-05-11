"""
Solve in Fewest Steps

Problem:
Given a string consisting of letters and digits, separate and sort the letters and digits individually,
then concatenate the sorted letters first and sorted digits after.

Approach:
1. Separate letters and digits.
2. Sort each group.
3. Concatenate letters first and digits after.
"""

def solve_string(s):
    return ''.join(sorted([c for c in s if c.isalpha()])) + ''.join(sorted([c for c in s if c.isdigit()]))

print(solve_string("B4A1D3"))

