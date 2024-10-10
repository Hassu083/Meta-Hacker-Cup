from collections import defaultdict, Counter, deque
from sortedcontainers import SortedList
from functools import lru_cache
# import heappq
import math
import sys

sys.setrecursionlimit(10**6)

f = open("wildcard_submissions_input.txt", "r")
f2 = open("output.txt", "a+")

@lru_cache(None)
def count(lst):
    
    groupby = defaultdict(set)
    for word in lst:
        if not len(word): continue
        groupby[word[0]].add(word[1:])
    
    ans = 0
    for char in list(groupby.keys()):
        if char == "?":
            ans += 26 - len(groupby) + 1 + (26 - len(groupby)+1)*count(tuple(sorted(groupby[char])))
        else:
            ans += 1 + count(tuple(sorted(groupby[char] | groupby['?'])))
    
    return ans



def solve():
    n = int(f.readline())  #int
    lst = [f.readline().strip() for _ in range(n)] #list[int]
    return (count(tuple(lst)) + 1)%998244353

t = int(f.readline())
for i in range(t):
    f2.write(f"Case #{i+1}: {solve()}\n")

f.close()
f2.close()
