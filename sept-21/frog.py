"""
There are n stones, each with height. Height difference incurs cost.
Frog will jump one stone to another. He can jump to next stone, or skip it. 
Find minimum cost frog can jump from one stone to another.

E.g. [10, 30, 40, 20]
"""

n = int(input())
jumps = list(map(int, input().split()))

prev = 0
curr = abs(jumps[1] - jumps[0])

for i in range(2, n):
    curr_stone = jumps[i]
    jump = abs(curr_stone - jumps[i-1]) + curr 
    skip = abs(curr_stone - jumps[i-2]) + prev
    prev = curr
    curr = min(jump, skip)
print(curr)