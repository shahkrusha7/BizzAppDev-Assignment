"""
Problem: Circular Seating Arrangement

You are given a list of N guests, where each guest has exactly two preferred neighbors they
want to sit next to at a circular dinner table. The goal is to determine a seating arrangement
where every guest is seated between their two preferred neighbors.

Input:
A dictionary mapping each guest's name to a list of exactly two preferred neighbors.

Output:
A valid circular seating arrangement (as a tuple), or a message stating no valid arrangement is possible.

Approach:
- Generate all possible permutations of guest names (all possible seatings).
- For each arrangement, check that each guest's left and right neighbors are both in their preference list.
- Because the table is circular, neighbors wrap around at the ends.
- Return the first valid arrangement found, or a message if none are valid.
"""

from itertools import permutations

guests = {
    'Jay': ['Sakshi', 'Nikky'],
    'Sakshi': ['Jay', 'Manasvi'],
    'Nikky': ['Jay', 'Manasvi'],
    'Manasvi': ['Sakshi', 'Nikky']
}

def finding_seats(guests):
    people=list(guests)

    for arrangement in permutations(people):
        okay=True
        for i,person in enumerate(arrangement):
            left=arrangement[i-1]
            right=arrangement[(i+1)%len(arrangement)]
            if left not in guests[person] or right not in guests[person]:
                okay=False
                break
        if okay:
            return arrangement
    return "No valid seating arrangement possible."


print(finding_seats(guests))