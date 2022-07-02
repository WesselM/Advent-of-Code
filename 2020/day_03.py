# https://adventofcode.com/2020/day/3

def main():
    with open("2020\examples\ex_03.txt", "r") as f:
        ex = list(map(str, f.read().split("\n")))

    assert part_one(ex) == 7
    assert part_two(ex) == 336

    with open("2020\data\input_03.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(path):
    return tree_encounter(path, 3, 1)


def part_two(path):
    return (tree_encounter(path, 1, 1) * tree_encounter(path, 3, 1) * tree_encounter(path, 5, 1) *
            tree_encounter(path, 7, 1) * tree_encounter(path, 1, 2))


def tree_encounter(path, right, down):
    trees = 0
    for i in range(0, len(path), down):
        x = right * i // down % len(path[i])
        if path[i][x] == '#':
            trees += 1

    return trees


if __name__ == '__main__':
    main()
