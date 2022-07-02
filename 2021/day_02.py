# https://adventofcode.com/2021/day/2


def main():
    with open("2021\examples\ex_02.txt", "r") as f:
        ex = list(map(str, f.read().split("\n")))

    assert part_one(ex) == 150
    assert part_two(ex) == 900

    with open("2021\data\input_02.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(commands):
    horizonal_pos = depth = 0
    for command in commands:
        action = command.split(" ")[0]
        units = int(command.split(" ")[1])
        match action:
            case 'forward':
                horizonal_pos += units
            case 'down':
                depth += units
            case 'up':
                depth -= units

    return horizonal_pos * depth


def part_two(commands):
    horizonal_pos = depth = aim = 0
    for command in commands:
        action = command.split(" ")[0]
        units = int(command.split(" ")[1])
        match action:
            case 'forward':
                horizonal_pos += units
                depth += aim * units
            case 'down':
                aim += units
            case 'up':
                aim -= units

    return horizonal_pos * depth


if __name__ == '__main__':
    main()
