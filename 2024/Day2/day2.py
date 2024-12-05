
def read_data():
  with open('day2.input', 'r') as file:
    for line in file.readlines():
      yield line


def generate_arrays(array):
  yield array
  for i in range(len(array)):
    yield array[:i] + array[i + 1:]


def check_increasing(levels):
  for i in range(1, len(levels)):
    if levels[i - 1] >= levels[i] or levels[i] - levels[i - 1] > 3:
      return False
  return True


def check_decreasing(levels):
  for i in range(1, len(levels)):
    if levels[i - 1] <= levels[i] or levels[i - 1] - levels[i] > 3:
      return False
  return True


def check_level(levels):
  return check_increasing(levels) or check_decreasing(levels)


# part 1
count = 0
for record in read_data():
  levels = [int(i) for i in record.strip().split(" ")]
  if check_level(levels):
    count += 1
print("Part 1:", count)

# part 2
count = 0
for record in read_data():
  levels = [int(i) for i in record.strip().split(" ")]
  for arr in generate_arrays(levels):
    if check_level(arr):
      count += 1
      break
print("Part 2:", count)
