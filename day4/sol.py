# Part 1 - 8-direction adjacency
print("PART 1")
with open("day4/input.txt", 'r') as f:
    grid = [list(line.strip()) for line in f]

    len_rows = len(grid)
    len_cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    def num_adjacent(row, col) -> int:
        ret = 0
        for dir_row, dir_col in directions:
            n_row = dir_row + row
            n_col = dir_col + col
            if 0 <= n_row and n_row < len_rows and 0 <= n_col and n_col < len_cols:
                if grid[n_row][n_col] == '@':
                    ret += 1
        return ret
    
    res = 0
    for row in range(len_rows):
        for col in range(len_cols):
            if grid[row][col] != '@':
                continue
            if num_adjacent(row, col) < 4:
                res += 1
        
    print(res)

# Part 2 - greedy (hope it works)
print("\nPART 2")
with open("day4/input.txt", 'r') as f:
    grid = [list(line.strip()) for line in f]

    len_rows = len(grid)
    len_cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    def num_adjacent(row, col) -> int:
        ret = 0
        for dir_row, dir_col in directions:
            n_row = dir_row + row
            n_col = dir_col + col
            if 0 <= n_row and n_row < len_rows and 0 <= n_col and n_col < len_cols:
                if grid[n_row][n_col] == '@':
                    ret += 1
        return ret
    
    res = 0
    while True:
        can_remove = []
        for row in range(len_rows):
            for col in range(len_cols):
                if grid[row][col] != '@':
                    continue
                if num_adjacent(row, col) < 4:
                    can_remove.append((row, col))

        if len(can_remove) == 0:
            break
        
        res += len(can_remove)
        for r, c in can_remove:
            grid[r][c] = '.'

    print(res)