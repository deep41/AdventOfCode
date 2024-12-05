def read_data(file_name):
  with open(file_name, 'r') as file:
      for line in file.readlines():
          yield line

def read_matrix():
  _matrix = [[ch for ch in line.strip()] for line in read_data('day4.input') ]
  return _matrix

matrix = read_matrix()

M, N = len(matrix), len(matrix[0])

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1),  (-1, 1), (-1, -1))

def isValid(x, y):
  return not (x < 0 or y < 0 or x >= M or y >= N)

target_string = 'XMAS'

res = [0]
def dfs(x, y):
  for dx, dy in dirs:
    pos = 0
    while pos < 4:
      new_x, new_y = x + dx * pos, y + dy * pos
      if not isValid(new_x, new_y) or matrix[new_x][new_y] != target_string[pos]:
        break
      pos += 1
    res[0] += pos == 4

for i in range(M):
  for j in range(N):
    if matrix[i][j] == 'X':
      dfs(i, j)

print("Part 1:", res[0])

# ----------------------------------
# part 2
opposite_pairs = (((1,1), (-1, -1)), ((1, -1), (-1, 1)))

def x_mas(x, y):
  found = False
  for pair in opposite_pairs:
    found_list = set()
    for dx, dy in pair:
      new_x, new_y = x + dx, y + dy
      found_list.add(matrix[new_x][new_y])
    if 'M' in found_list and 'S' in found_list:
      res[0] += found
      found = True

res = [0]
for i in range(1, M - 1):
  for j in range(1, N - 1):
    if matrix[i][j] == 'A':
      x_mas(i, j)
print(res[0])
      
      