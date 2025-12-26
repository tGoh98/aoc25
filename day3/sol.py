# Part 1 - find first largest number then subsequent largest num (greedy sliding window)
print("PART 1")
with open("day3/input.txt", 'r') as f:
    input = [line.strip() for line in f]

    def max_digit(num: str):
        max = '0'
        idx = 0
        for i, d in enumerate(num):
            if d > max:
                max = d
                idx = i
        
        return max, idx
        
    def max_joltage(bank: str) -> int:
        first, i = max_digit(bank[:-1])
        second, _ = max_digit(bank[i+1:])
        return int(first+second)

    res = 0
    for bank in input:
        n = max_joltage(bank)
        res += n

    print(res)

# Part 2 - sliding window
print("PART 2")
with open("day3/input.txt", 'r') as f:
    input = [line.strip() for line in f]

    def max_digit(num: str):
        max = '0'
        idx = 0
        for i, d in enumerate(num):
            if d > max:
                max = d
                idx = i
        
        return max, idx
        
    def max_joltage(bank: str) -> int:
        acc = ''
        working_str = bank
        i = 12
        # Off by 1's are tough
        while i > 0:
            if len(working_str) < i:
                raise Exception("Bad len", len(working_str), i, working_str)
            
            d, idx = max_digit(working_str[:len(working_str)-i+1])
            acc += d
            working_str = working_str[idx+1:]
            i -= 1
        return int(acc)

    res = 0
    for bank in input:
        n = max_joltage(bank)
        res += n

    print(res)