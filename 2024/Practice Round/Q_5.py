from sortedcontainers import SortedList

f = open("line_of_delivery_part_2_input.txt", "r")
f2 = open("output.txt", "a+")

def solve():
    
    n, G = map(int, f.readline().strip().split())  #list
    lst = [int(f.readline()) for _ in range(n)]
    prefix_difference_array = SortedList([0])
    last_pos = lst[0] - 1
    for i in range(1, n):
        if lst[i] < last_pos:
            increment_val = last_pos - lst[i]
            prefix_difference_array = SortedList([val+increment_val for val in prefix_difference_array])
            prefix_difference_array.add(0)
            last_pos = lst[i] - 1
        else:
            value = lst[i] - last_pos
            prefix_difference_array.add(value)
            last_pos -= 1
    
    last_pos += 1
    final_pos = []
    for j in range(n):
        final_pos.append(last_pos+prefix_difference_array[j]+j)
    # print(final_pos)
    final_pos.reverse()
    # print(final_pos)

    ans_dis = float("inf")
    ans_point = None
    for i in range(n):
        dis = abs(final_pos[i]-G)
        # print(dis, i+1)
        if dis < ans_dis:
            ans_point = i + 1
            ans_dis = dis
    return ans_point, ans_dis

t = int(f.readline())
for i in range(t):
    point, dis = solve()
    # print(f'Case #{i+1}: {point} {dis}\n')
    f2.write(f'Case #{i+1}: {point} {dis}\n')

f.close()
f2.close()