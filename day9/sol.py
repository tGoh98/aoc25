from itertools import combinations

# Part 1 - good thing i learned itertools in day8?
print("PART 1")
with open("day9/input.txt", 'r') as f:
    points = [tuple(map(int, line.strip().split(','))) for line in f]
    # print(points)

    max_area = 0
    for p1, p2 in combinations(points, 2):
        w = abs(p1[0] - p2[0]) + 1
        l = abs(p1[1] - p2[1]) + 1
        max_area = max(max_area, w*l)
    print(max_area)

# Part 2 - flood fill + 2d prefix sum seemed good. but need chatgpt to help optimize it
print("\nPART 2")
import time
from collections import deque
from itertools import combinations

start_total = time.time()

print("Reading input...")
t0 = time.time()
with open("day9/input.txt") as f:
    red = [tuple(map(int, line.split(","))) for line in f]
print(f"  Loaded {len(red)} red tiles in {time.time() - t0:.2f}s")

# -------------------------
# Build boundary
# -------------------------
print("Building boundary...")
t0 = time.time()

boundary = set(red)
n = len(red)

for i in range(n):
    x1, y1 = red[i]
    x2, y2 = red[(i + 1) % n]

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            boundary.add((x1, y))
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            boundary.add((x, y1))

print(f"  Boundary tiles: {len(boundary)} ({time.time() - t0:.2f}s)")

# -------------------------
# Coordinate compression
# -------------------------
print("Compressing coordinates...")
t0 = time.time()

xs = sorted({x for x, _ in boundary})
ys = sorted({y for _, y in boundary})

x_id = {x: i for i, x in enumerate(xs)}
y_id = {y: i for i, y in enumerate(ys)}

W, H = len(xs), len(ys)

print(f"  Compressed grid: {W} x {H} ({W*H} cells) in {time.time() - t0:.2f}s")

# -------------------------
# Build grid
# -------------------------
print("Building grid...")
t0 = time.time()

grid = [[0] * H for _ in range(W)]
for x, y in boundary:
    grid[x_id[x]][y_id[y]] = 1

print(f"  Grid built in {time.time() - t0:.2f}s")

# -------------------------
# Flood fill exterior
# -------------------------
print("Flood-filling exterior...")
t0 = time.time()

outside = [[False] * H for _ in range(W)]
q = deque()

for i in range(W):
    for j in (0, H - 1):
        if grid[i][j] == 0:
            outside[i][j] = True
            q.append((i, j))

for j in range(H):
    for i in (0, W - 1):
        if grid[i][j] == 0 and not outside[i][j]:
            outside[i][j] = True
            q.append((i, j))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H:
            if grid[nx][ny] == 0 and not outside[nx][ny]:
                outside[nx][ny] = True
                q.append((nx, ny))

print(f"  Flood fill completed in {time.time() - t0:.2f}s")

# -------------------------
# Build allowed grid
# -------------------------
print("Building allowed grid...")
t0 = time.time()

allowed = [[0] * H for _ in range(W)]
for i in range(W):
    for j in range(H):
        if grid[i][j] == 1 or not outside[i][j]:
            allowed[i][j] = 1

print(f"  Allowed grid built in {time.time() - t0:.2f}s")

# -------------------------
# Prefix sum
# -------------------------
print("Building prefix sums...")
t0 = time.time()

S = [[0] * H for _ in range(W)]
for i in range(W):
    for j in range(H):
        S[i][j] = allowed[i][j]
        if i > 0:
            S[i][j] += S[i - 1][j]
        if j > 0:
            S[i][j] += S[i][j - 1]
        if i > 0 and j > 0:
            S[i][j] -= S[i - 1][j - 1]

print(f"  Prefix sums built in {time.time() - t0:.2f}s")

def rect_sum(x1, y1, x2, y2):
    res = S[x2][y2]
    if x1 > 0:
        res -= S[x1 - 1][y2]
    if y1 > 0:
        res -= S[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        res += S[x1 - 1][y1 - 1]
    return res

# -------------------------
# Rectangle search
# -------------------------
print("Searching rectangles...")
t0 = time.time()

red_c = [(x_id[x], y_id[y]) for x, y in red]
max_area = 0
checked = 0

for (x1, y1), (x2, y2) in combinations(red_c, 2):
    if x1 == x2 or y1 == y2:
        continue

    xa, xb = sorted((x1, x2))
    ya, yb = sorted((y1, y2))

    area = (xs[xb] - xs[xa] + 1) * (ys[yb] - ys[ya] + 1)
    if rect_sum(xa, ya, xb, yb) == area:
        max_area = max(max_area, area)

    checked += 1
    if checked % 1_000_000 == 0:
        print(f"  Checked {checked:,} rectangle pairs...")

print(f"  Rectangle search finished in {time.time() - t0:.2f}s")

# -------------------------
# Result
# -------------------------
print("\nRESULT")
print("Max area:", max_area)
print(f"Total runtime: {time.time() - start_total:.2f}s")
