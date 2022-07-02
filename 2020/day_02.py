# https://adventofcode.com/2020/day/2

def main():
    with open("2020\examples\ex_02.txt", "r") as f:
        ex = list(map(str, f.read().split("\n")))

    assert part_one(ex) == 2
    assert part_two(ex) == 1

    with open("2020\data\input_02.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(passwords):
    valids = 0
    for i in passwords:
        # if password.count(char) >= min and password.count(char) <= max:
        if i.split(': ')[1].count(i.split(': ')[0].split(' ')[1]) >= int(i.split(': ')[0].split(' ')[0].split('-')[0]) and \
                i.split(': ')[1].count(i.split(': ')[0].split(' ')[1]) <= int(i.split(': ')[0].split(' ')[0].split('-')[1]):
            valids += 1

    return valids


def part_two(passwords):
    valids = 0
    for i in passwords:
        # if  (password[first_pos] == char) != (password[second_pos] == char):
        if (i.split(': ')[1][int(i.split(': ')[0].split(' ')[0].split('-')[0]) - 1] == i.split(': ')[0].split(' ')[1]) != \
                (i.split(': ')[1][int(i.split(': ')[0].split(' ')[0].split('-')[1]) - 1] == i.split(': ')[0].split(' ')[1]):
            valids += 1

    return valids


if __name__ == '__main__':
    main()
