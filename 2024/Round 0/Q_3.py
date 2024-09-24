from collections import defaultdict
import random
import time
import math

f = open("fall_in_line_input.txt", "r")
f2 = open("output.txt", "a+")

SAMPLE_SIZE = 1000
NO_OF_EXPERIMENT = 2

def random_selection(lst):
	if len(lst) > SAMPLE_SIZE:
		return random.sample(lst, min(len(lst), SAMPLE_SIZE))
	return lst

def normalized_slope(a, b):
	
	run = b[0] - a[0]

	if run == 0:
		return (1, 0)

	if run < 0:
		a, b = b, a
		run = b[0] - a[0]

	rise = b[1] - a[1]

	g = math.gcd(abs(rise), abs(run))
	
	return (
		rise//g, run//g, 
	)


def maximum_points_on_same_line(points):
	
	n = len(points)
	if n < 3:
		return n
	
	average = 1
	for _ in range(NO_OF_EXPERIMENT if n > SAMPLE_SIZE else 1):
		random_points = random_selection(points)
		m = len(random_points)
		max_val = 0
		for a_index in range(0, m - 1):
			a = random_points[a_index]
			slope_counts = defaultdict(lambda: 1)
			for b_index in range(a_index + 1, m):
				b = random_points[b_index]
				slope_counts[normalized_slope(a, b)] += 1
			max_val = max(
                max_val,
                max(slope_counts.values()),
            )
		average *= (max_val/m)
	return average

def solve():
	n = int(f.readline())
	lst = [list(map(int, f.readline().split())) for _ in range(n)]
	ans = math.inf
	for i in range(5):
		ans = min(ans, int(len(lst)*(maximum_points_on_same_line(lst))))
	return len(lst) - ans

t = int(f.readline())
for i in range(t):
	st = time.time()
	f2.write(f"Case #{i+1}: {solve()}\n")
	print("time taken:", math.ceil(time.time()-st))


f.close()
f2.close()

