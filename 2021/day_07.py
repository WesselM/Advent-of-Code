# https://adventofcode.com/2021/day/7


from sys import maxsize


def main():
    with open("2021\examples\ex_07.txt", "r") as f:
        ex = list(map(int, f.read().split(",")))

    assert part_one(ex) == 37
    assert part_two(ex) == 168

    with open("2021\data\input_07.txt", "r") as f:
        inp = list(map(int, f.read().strip().split(",")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(positions):
    cheapest_fuel = maxsize
    for i in range(max(max(positions), len(positions))):
        fuel = 0
        for position in positions:
            fuel += abs(position - i)
        if fuel <= cheapest_fuel:
            cheapest_fuel = fuel

    return cheapest_fuel


def part_two(positions):
    cheapest_fuel = maxsize
    for i in range(max(max(positions), len(positions))):
        fuel = 0
        for position in positions:
            distance = abs(position - i)
            fuel += distance * (distance + 1) // 2
        if fuel < cheapest_fuel:
            cheapest_fuel = fuel

    return cheapest_fuel


if __name__ == '__main__':
    main()
