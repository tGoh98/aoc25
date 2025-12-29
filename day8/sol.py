import math
import heapq
from itertools import combinations

# Part 1 - relearn union find. also read the problem carefully (10 vs 1000)
print("PART 1")
with open("day8/input.txt", 'r') as f:
    input = [line.strip() for line in f]
    points = [tuple(map(int, x.split(","))) for x in input]
    
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, a, b):
            ra = self.find(a)
            rb = self.find(b)
            if ra == rb:
                return # already joined
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]

    n = len(points)
    edges = []

    for (i, p1), (j, p2) in combinations(enumerate(points), 2):
        d = math.dist(p1, p2)
        edges.append((d, i, j))

    edges.sort(key=lambda x: x[0])

    uf = UnionFind(n)

    for _, i, j in edges[:1000]: # use 10 for the sample problem
        uf.union(i, j)

    counts = {}
    for i in range(n):
        root = uf.find(i)
        counts[root] = counts.get(root, 0) + 1

    top3 = []
    for size in counts.values():
        heapq.heappush(top3, size)
        if len(top3) > 3:
            heapq.heappop(top3)

    res = 1
    for s in top3:
        res *= s

    print(res)

# Part 2 - track the last merge
print("PART 2")
with open("day8/input.txt", 'r') as f:
    input = [line.strip() for line in f]
    points = [tuple(map(int, x.split(","))) for x in input]
    
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
            self.num_components = n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, a, b):
            ra = self.find(a)
            rb = self.find(b)
            if ra == rb:
                return False
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            self.num_components -= 1
            return True

    n = len(points)
    edges = []

    for (i, p1), (j, p2) in combinations(enumerate(points), 2):
        d = math.dist(p1, p2)
        edges.append((d, i, j))

    edges.sort(key=lambda x: x[0])

    uf = UnionFind(n)

    last_pair = None
    for _, i, j in edges:
        merged = uf.union(i, j)
        if merged:
            if uf.num_components == 1:
                last_pair = (points[i], points[j])
                break

    print(last_pair[0][0] * last_pair[1][0])
