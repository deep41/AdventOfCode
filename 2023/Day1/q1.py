counter = 0

with open('day1/input.file', 'r') as file:
  for line in file:
    first, last = -1, len(line) - 1

    for pos in range(len(line)):
      if line[pos].isnumeric():
        if (first == -1):
          first = pos
        last = pos
    number = int(line[first]) * 10 + int(line[last])
    counter += number

print(counter)