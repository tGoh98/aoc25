# Part 1 - use mod
print("PART 1")
with open("day1/input.txt", 'r') as f:
    input = [line.strip() for line in f]
    
    res = 0
    pos = 50
    for line in input:
        dir = line[:1]
        amt = int(line[1:])
        if dir == 'R':
            pos += amt
        elif dir == 'L':
            pos -= amt
        else:
            raise Exception("Unrecognized pos", pos)
        
        pos = pos % 100
        if pos == 0:
            res += 1
    
    print(res)

# Part 2 - compute the loops then account for the remainder (this tripped me up for too long :/ )
print("\nPART 2")
with open("day1/input.txt", 'r') as f:
    input = [line.strip() for line in f]
    
    res = 0
    pos = 50
    for line in input:
        dir = line[:1]
        amt = int(line[1:])

        res += int(amt / 100)
        
        prev_pos = pos
        if dir == 'R':
            pos += amt
        elif dir == 'L':
            pos -= amt
        else:
            raise Exception("Unrecognized pos", pos)
        pos = pos % 100
        
        if prev_pos == 0:
            continue

        if pos == 0 or (dir == 'R' and pos < prev_pos) or (dir == 'L' and pos > prev_pos):
            res += 1
    
    print(res)