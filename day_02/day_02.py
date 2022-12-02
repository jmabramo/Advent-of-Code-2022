def parse_data(filename):
    ret_val = []
    with open(filename) as f:
        for line in f.readlines():
            a, b = line.rstrip().split(" ")
            ret_val.append((a,b))
    return ret_val

def round_score(p1, p2):
    score = 0
    score += ord(p2) - ord("W")
    
    if ord(p1)-ord("@") == ord(p2)-ord("W"):
        score += 3

    if (p1=="A" and p2=="Y") or (p1=="B" and p2=="Z") or (p1=="C" and p2=="X"):
        score += 6

    return score


def part_one(input):
    total = 0
    for (a,b) in input:
        total += round_score(a,b)
    return total

def part_two(input):
    moves = {
        "X": {"A": "Z", "B": "X", "C": "Y"},
        "Y": {"A": "X", "B": "Y", "C": "Z"},
        "Z": {"A": "Y", "B": "Z", "C": "X"}
    }
    total = 0
    for (a,b) in input:
        total += round_score(a,moves[b][a])
    return total

if __name__ == "__main__":
    test_data = parse_data("test_input_1.txt")

    expected_result_1 = 15
    assert(part_one(test_data)==expected_result_1)

    expected_result_2 = 12
    assert(part_two(test_data)==expected_result_2)

    data = parse_data('input.txt')

    print(f'Part 1 Answer: {part_one(data)}')
    print(f'Part 2 Answer: {part_two(data)}')