# Part 1 - brute force :P
print("PART 1")
with open("day2/input.txt", 'r') as f:
    input = f.readline().split(",")

    # any ID which is made only of some sequence of digits repeated twice
    def is_invalid(num: str) -> bool:
        if len(num) % 2 != 0:
            return False
        
        midpoint = int(len(num) / 2)
        for i in range(midpoint):
            if num[i] != num[midpoint + i]:
                return False
        return True

    def sum_invalid_ids_in_range(prod_range: str) -> int:
        ranges = prod_range.split("-")
        start = int(ranges[0])
        end = int(ranges[1])
        
        ret = 0
        for i in range(start, end+1):
            if is_invalid(str(i)):
                ret += i
        return ret
    
    res = 0
    for prod_range in input:
        res += sum_invalid_ids_in_range(prod_range)

    print(res)

# Part 2 - still brute force :P
print("PART 2")
with open("day2/input.txt", 'r') as f:
    input = f.readline().split(",")

    # any ID which is made only of some sequence of digits repeated AT LEAST twice
    def is_invalid(s: str) -> bool:
        return s in (s + s)[1:-1]

    def sum_invalid_ids_in_range(prod_range: str) -> int:
        ranges = prod_range.split("-")
        start = int(ranges[0])
        end = int(ranges[1])
        
        ret = 0
        for i in range(start, end+1):
            if is_invalid(str(i)):
                ret += i
        return ret
    
    res = 0
    for prod_range in input:
        res += sum_invalid_ids_in_range(prod_range)

    print(res)