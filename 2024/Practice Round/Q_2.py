from collections import defaultdict, Counter
from functools import lru_cache
import math

f = open("line_by_line_input.txt", "r")
f2 = open("output.txt", "a+")

def solve():
    # n = int(f.readline())  #int
    n, p = (map(int, f.readline().strip().split()))  #list
    req_success = p/100
    success = math.exp(math.log(req_success)*(n-1)/n)
    success = success*100   
    return success-p

t = int(f.readline())
for i in range(t):
    f2.write(f"Case #{i+1}: {solve()}\n")

f.close()
f2.close()