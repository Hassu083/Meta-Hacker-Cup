from collections import defaultdict, Counter, deque
from sortedcontainers import SortedList
from functools import lru_cache
# import heappq
import math
import sys

sys.setrecursionlimit(10**6)

f = open("subsonic_subway_input.txt", "r")
f2 = open("output.txt", "a+")

def solve():
    n = int(f.readline())  #int
    lst = [map(int, f.readline().split()) for _ in range(n)]
    mspeed, mxspeed = -math.inf, math.inf
    for distance in range(1, n+1):
        mntime, mxtime = lst[distance-1]
        if mxtime == 0:
            return -1
        mspeed = max(mspeed, distance/mxtime)
        mxspeed = min(mxspeed, distance/(mntime if mntime else 0.1))
        if mspeed >= mxspeed:
            return -1
    return mspeed if mspeed != -math.inf else -1

t = int(f.readline())
for i in range(t):
    f2.write(f"Case #{i+1}: {solve()}\n")

f.close()
f2.close()
