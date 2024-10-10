from collections import defaultdict, Counter, deque
from sortedcontainers import SortedList
from functools import lru_cache
import math
import sys

sys.setrecursionlimit(10**6)

f = open("prime_subtractorization_input.txt", "r")
f2 = open("output.txt", "a+")


N = 10_000_000
is_prime = [True] * (N + 1)
is_prime[0], is_prime[1] = False, False

for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False




def solve():
    n = int(f.readline()) 
    primes  = [i for i in range(2, n + 1) if is_prime[i]]
    ans_set = set()
    B = False
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            p1 = primes[i]
            p2 = primes[j]
            if p1+p2 > n:
                B = True
                break
            elif is_prime[p1+p2]:
                ans_set.add(p1)
                ans_set.add(p2)
        if B:
            break
    return len(ans_set)


t = int(f.readline())
for i in range(t):
    f2.write(f"Case #{i+1}: {solve()}\n")

f.close()
f2.close()
