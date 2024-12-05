from collections import defaultdict

l_list = []
r_list = []
l_counter = defaultdict(int)
r_counter = defaultdict(int)

ans_1 = 0

with open(r"day1.input", 'r') as file:
  for line in file.readlines():
    data = line.strip().split("   ")
    l, r = int(data[0]), int(data[1])
    l_list.append(l)
    r_list.append(r)
    l_counter[l] += 1
    r_counter[r] += 1

r_list.sort()
l_list.sort()
for i in range(len(l_list)):
  ans_1 += abs(l_list[i] - r_list[i])

print("Part 1:", ans_1)

ans_2 = 0
for num, l_times in l_counter.items():
  ans_2 += r_counter[num] * l_times * num

print("Part 2:", ans_2)
