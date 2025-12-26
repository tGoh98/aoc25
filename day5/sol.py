# Part 1 - line sweep
print("PART 1")
with open("day5/input.txt", 'r') as f:
    events = []

    parsing_ranges = True
    for line in f:
        line = line.strip()
        if not line:
            parsing_ranges = False
            continue

        if parsing_ranges:
            rng = line.split('-')
            start, end = int(rng[0]), int(rng[1])
            events.append((start, 1))
            events.append((end + 1, -1))
        else:
            events.append((int(line), 'query'))

    events.sort()
    
    res = 0
    fresh = 0
    for n, event in events:
        if event == 'query':
            if fresh > 0:
                res += 1
            continue

        fresh += event

    print(res)

# Part 2 - I should've merged the ranges for part 1
print("\nPART 2")
with open("day5/input.txt", 'r') as f:
    ranges = []

    for line in f:
        line = line.strip()
        if not line:
            break
        
        rng = line.split('-')
        start, end = int(rng[0]), int(rng[1])
        ranges.append((start, end))

    ranges.sort()

    i = 0
    while i < len(ranges)-1:
        if ranges[i][1] >= ranges[i+1][0]:
            ranges[i] = (ranges[i][0], max(ranges[i][1], ranges[i+1][1]))
            del ranges[i+1]
            continue
    
        i += 1
    
    res = 0
    for r in ranges:
        res += r[1] - r[0] + 1
    
    print(res)