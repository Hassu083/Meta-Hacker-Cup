from collections import defaultdict, Counter
from functools import lru_cache
import math

f = open("walk_the_line_input.txt", "r")
f2 = open("output.txt", "a+")

def solve():
    # n = int(f.readline())  #int
    n, k = map(int, f.readline().strip().split())  #list
    mini = float("inf")
    for _ in range(n):
        mini = min(mini, int(f.readline()))
    if n in [1, 2]:
        return mini <= k
    return ((mini*(n-2)*2) + mini) <= k

t = int(f.readline())
for i in range(t):
    f2.write(f'Case #{i+1}: {"YES" if solve() else "NO"}\n')

f.close()
f2.close()