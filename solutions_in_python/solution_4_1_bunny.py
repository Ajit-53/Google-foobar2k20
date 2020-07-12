"""This problem is a based on combinatorics. To make to notation clear, let us consider that there are b bunnies and r are required. Let us now consider this simple situation, let us say we have chosen r-1 bunnies at random, and we were to choose 1 more bunny to get the complete set of keys to open the prison door. We know that these r-1 bunnies cannot open the door by themselves and hence the remaining b-r+1 bunnies must have a key that these r-1 bunnies don’t. We can exploit this property to solve the problem. We need to generate all combinations of size b-r+1 bunnies and add a unique key to each of these bunnies. The code for this in python is as below."""

from itertools import combinations

def solution(num_buns, num_required):
    buns = [[] for i in range(num_buns)]
    if num_required == 0:
        return buns
    start = 0
    for c in combinations(buns, num_buns - num_required + 1):
        for item in c:
            item.append(start)
        start += 1
    return buns