# https://adventofcode.com/2021/day/3


def main():
    with open("2021\examples\ex_03.txt", "r") as f:
        ex = list(map(str, f.read().split("\n")))

    assert part_one(ex) == 198
    assert part_two(ex) == 230

    with open("2021\data\input_03.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(consumption):
    gamma = epsilon = ""
    for i in range(len(consumption[0])):
        vertical = [item[i] for item in consumption]
        gamma += max(vertical, key=vertical.count)
        epsilon += min(vertical, key=vertical.count)

    return int(gamma, 2) * int(epsilon, 2)


def part_two(consumption):
    oxygen = get_rating(consumption, True)
    co2 = get_rating(consumption, False)

    return int(oxygen, 2) * int(co2, 2)


def get_rating(consumption, isOxygen):
    for i in range(len(consumption[0])):
        if len(consumption) == 1:
            return consumption[0]
        vertical = [item[i] for item in consumption]
        zeros = vertical.count('0')
        ones = vertical.count('1')
        common = 1 if ((isOxygen and ones >= zeros)
                       or (not isOxygen and ones < zeros)) else 0
        consumption = [j for j in consumption if j[i] == str(common)]

    return consumption[0]


if __name__ == '__main__':
    main()
