# https://adventofcode.com/2020/day/0

def main():
    with open("2020\examples\ex_00.txt", "r") as f:
        ex = list(map(str, f.read().split()))

    assert part_one(ex) == 0
    assert part_two(ex) == 0

    with open("2020\data\input_00.txt", "r") as f:
        inp = list(map(str, f.read().strip().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(entries):
    return entries[0]


def part_two(entries):
    return entries[1]


if __name__ == '__main__':
    main()
