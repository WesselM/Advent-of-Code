# https://adventofcode.com/2020/day/1

def main():
    with open("2020\examples\ex_01.txt", "r") as f:
        ex = list(map(int, f.read().split()))

    assert part_one(ex) == 514579
    assert part_two(ex) == 241861950

    with open("2020\data\input_01.txt", "r") as f:
        inp = list(map(int, f.read().split()))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(entries):
    for i in entries:
        for j in entries:
            if i + j == 2020:
                return i * j


def part_two(entries):
    for i in entries:
        for j in entries:
            for k in entries:
                if i + j + k == 2020:
                    return i * j * k


if __name__ == '__main__':
    main()
