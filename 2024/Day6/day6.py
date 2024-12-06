def read_data(file_name):
  with open(file_name, 'r') as file:
    for line in file.readlines():
      yield line


guard_dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1),}

def turn_guard(ch):
    return list(guard_dirs.keys())[(list(guard_dirs.keys()).index(ch) + 1) % 4]

def main():
    grid = [[ch for ch in line.strip()] for line in read_data('day6.input')]
    result = 0
    # Determine start position
    curr_pos = None
    prev_loc_item = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in guard_dirs:
                curr_pos = (i, j)
                break
    print("starting at", curr_pos)

    # traverse
    while True:
        x, y = curr_pos
        dx, dy = guard_dirs[grid[x][y]]
        new_x, new_y = x + dx, y + dy
        if new_x < 0 or new_y < 0 or new_x >= len(grid) or new_y >= len(grid[0]):
            if prev_loc_item == '.':
                result += 1
            grid[x][y] = 'X'
            break
        
        if grid[new_x][new_y] == '#':
            grid[x][y] = turn_guard(grid[x][y])
        elif grid[new_x][new_y] in ['.', 'X']:
            if grid[new_x][new_y] == '.':
                result += 1
            prev_loc_item = grid[new_x][new_y]
            grid[new_x][new_y] = grid[x][y]
            grid[x][y] = 'X'
            curr_pos = (new_x, new_y)
        
    for line in grid:
        print("".join(line))
    print(result)


if __name__ == '__main__':
    main()