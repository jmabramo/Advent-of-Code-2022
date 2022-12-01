def parse_data(filename):
    ret_val = []
    with open(filename) as f:
        for line in f.readlines():
            ret_val.append(line.rstrip())
    return ret_val

def create_array(input):
    parsing_array = [0]

    for value in input:
        if value == "":
            parsing_array.append(0)
        else:
            parsing_array[len(parsing_array) - 1] += int(value)
    
    return parsing_array

def part_one(input):
    return max(create_array(input))

def part_two(input):
    array = create_array(input)
    array.sort(reverse=True)
    return sum(array[:3])

if __name__ == "__main__":
    test_data = parse_data("test_input_1.txt")

    expected_result_1 = 24000
    assert(part_one(test_data)==expected_result_1)

    expected_result_2 = 45000
    assert(part_two(test_data)==expected_result_2)

    data = parse_data('input.txt')

    print(f'Part 1 Answer: {part_one(data)}')
    print(f'Part 2 Answer: {part_two(data)}')