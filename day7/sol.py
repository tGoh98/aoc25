# Part 1 - traverse and recurse
print("PART 1")
with open("day7/input.txt", 'r') as f:
    grid = [list(line.strip()) for line in f]
    
    visited = set([])
    dirs = [-1, 1]

    starting_pos = (0, 0)
    for i, c in enumerate(grid[0]):
        if c == 'S':
            starting_pos = (i, 0)

    def traverse(pos) -> int:
        if pos in visited:
            return 0
        else:
            visited.add(pos)
        
        # check out of bounds
        if pos[0] < 0 or pos[0] >= len(grid[pos[0]]) or pos[1] >= len(grid):
            return 0
        
        c = grid[pos[1]][pos[0]]
        
        if c == '.' or c == 'S':
            return traverse((pos[0], pos[1]+1))
        elif c == '^':
            # split
            res = 1
            for dir in dirs:
                to_visit = (pos[0]+dir, pos[1]+1)
                res += traverse(to_visit)
            return res
        else:
            raise Exception("Unrecognized char", c)

    print(traverse(starting_pos))
    
# Part 2 - same but no dedupe
print("PART 2")
with open("day7/input.txt", 'r') as f:
    grid = [list(line.strip()) for line in f]

    H = len(grid)
    W = len(grid[0])

    # find start
    for x, c in enumerate(grid[0]):
        if c == 'S':
            start = (x, 0)
            break

    memo = {}

    def timelines(pos):
        x, y = pos

        # exit manifold
        if y >= H or x < 0 or x >= W:
            return 1

        # Return cached result if exists
        if pos in memo:
            return memo[pos]
        
        c = grid[y][x]

        res = 0
        if c == '.' or c == 'S':
            res = timelines((x, y + 1))
        elif c == '^':
            res = timelines((x - 1, y + 1)) + timelines((x + 1, y + 1))
        else:
            raise Exception("Unknown char", c)
        
        memo[pos] = res
        return res

    print(timelines(start))
