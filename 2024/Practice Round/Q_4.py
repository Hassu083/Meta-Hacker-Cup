from collections import defaultdict, Counter
from functools import lru_cache
import math

f = open("line_of_delivery_part_1_input.txt", "r")
f2 = open("output.txt", "a+")

def solve():
    
    n, G = map(int, f.readline().strip().split())  #list
    lst = []
    for _ in range(n):
        lst.append(int(f.readline()))
    final_pos = sorted(lst)
    ans_dis = math.inf
    ans_point = -1
    for i in range(n):
        dis = abs(final_pos[n-i-1]-G)
        if dis < ans_dis:
            ans_point = i + 1
            ans_dis = dis
    return ans_point, ans_dis

t = int(f.readline())
for i in range(t):
    point, dis = solve()
    f2.write(f'Case #{i+1}: {point} {dis}\n')

f.close()
f2.close()
