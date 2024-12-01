import heapq
from collections import Counter

l_heap = []
r_heap = []

ans_1 = 0

with open(r"input.data", 'r') as file:
  for line in file.readlines():
    data = line.strip().split("   ")

    heapq.heappush(l_heap, int(data[0]))
    heapq.heappush(r_heap, int(data[1]))

l_counter = Counter(l_heap)
r_counter = Counter(r_heap)

while l_heap:
  l_item, r_item = heapq.heappop(l_heap), heapq.heappop(r_heap)
  ans_1 += abs(l_item - r_item)

print("Part 1:", ans_1)

ans_2 = 0
for num, l_times in l_counter.items():
  ans_2 += r_counter[num] * l_times * num

print("Part 2:", ans_2)
