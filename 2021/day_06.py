# https://adventofcode.com/2021/day/6


def main():
    with open("2021\examples\ex_06.txt", "r") as f:
        ex = list(map(int, f.read().split(",")))

    assert part_one(ex) == 5934
    assert part_two(ex) == 26984457539

    with open("2021\data\input_06.txt", "r") as f:
        inp = list(map(int, f.read().strip().split(",")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(school):
    school = school.copy()
    for _ in range(80):
        for i in range(len(school)):
            school[i] -= 1
            if school[i] == -1:
                school[i] = 6
                school.append(8)

    return len(school)


def part_two(school):
    ages = {i: school.count(i) for i in range(9)}
    for _ in range(256):
        birhts = ages[0]
        for i in range(1, len(ages)):
            ages[i-1] = ages[i]
        ages[8] = birhts
        ages[6] = ages[6] + birhts

    return(sum(ages.values()))


if __name__ == '__main__':
    main()
