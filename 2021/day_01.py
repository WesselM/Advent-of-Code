# https://adventofcode.com/2021/day/1


def main():
    with open("2021\examples\ex_01.txt", "r") as f:
        ex = list(map(int, f.read().split("\n")))

    assert part_one(ex) == 7
    assert part_two(ex) == 5

    with open("2021\data\input_01.txt", "r") as f:
        inp = list(map(int, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(sweeps):
    depth_increases = 0
    for i, sweep in enumerate(sweeps):
        if sweep > sweeps[i - 1]:
            depth_increases += 1

    return depth_increases


def part_two(sweeps):
    larger_sums = 0
    for i in range(len(sweeps)):
        if sum(sweeps[i-3:i]) > sum(sweeps[i-4:i-1]):
            larger_sums += 1

    return larger_sums


if __name__ == '__main__':
    main()
