# Part 1 - split on arbitrary number of whitespace
print("PART 1")
with open("day6/input.txt", 'r') as f:
    input = [line.strip().split() for line in f]

    nums = input[:-1]
    operands = input[-1]

    results = []

    for i, operand in enumerate(operands):
        working_nums = [nums[j][i] for j in range(len(nums))]

        acc = 0
        if operand == '*':
            acc = 1
        for n in working_nums:
            if operand == '+':
                acc += int(n)
            else:
                acc *= int(n)

        results.append(acc)

    print(sum(results))

# Part 2 - track index of operands to determine starting pos for string manipulations
# pain
print("\nPART 2")
with open("day6/input.txt", 'r') as f:
    input = [line.rstrip('\n') for line in f]
    nums = input[:-1]
    operands = input[-1]
    
    print(nums)
    print(operands)
    ops = []
    for i, c in enumerate(operands):
        if c != ' ':
            ops.append((i, c))
    print(ops)

    padded_nums = [[] for _ in range(len(nums))]
    for i, num_str in enumerate(nums):
        for j, op in enumerate(ops):
            to_append = ''
            next = j+1
            if next >= len(ops):
                to_append = num_str[op[0]:]
            else:
                to_append = num_str[op[0]:ops[next][0]-1]

            padded_nums[i].append(to_append)

    print(padded_nums)
    print("---")

    results = []
    for i, op_tup in enumerate(ops):
        op = op_tup[1]
        working_nums = [padded_nums[j][i] for j in range(len(padded_nums))]
        
        print(working_nums)
        print(op)
        print("---")

        acc = 0
        if op == '*':
            acc = 1
        for j in range(len(working_nums[0])):
            num = ''
            for k in range(len(working_nums)):
                num += working_nums[k][j]
            if op == '*':
                acc *= int(num)
            else:
                acc += int(num)
        results.append(acc)

    print(sum(results))