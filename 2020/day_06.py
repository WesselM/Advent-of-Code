# https://adventofcode.com/2020/day/6

import string


def main():
    with open("2020\examples\ex_06.txt", "r") as f:
        ex = list(map(str, f.read().split("\n\n")))

    assert part_one(ex) == 11
    assert part_two(ex) == 6

    with open("2020\data\input_06.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(answers):
    count_sum = 0
    questions = string.ascii_lowercase
    for answer in answers:
        for question in questions:
            if question in answer:
                count_sum += 1

    return count_sum


def part_two(answers):
    count_sum = 0
    groups = []
    questions = string.ascii_lowercase
    for answer in answers:
        groups.append(answer.split('\n'))

    for question in questions:
        for group in groups:
            cnt = 0
            for person in group:
                if question in person:
                    cnt += 1
            if cnt == len(group):
                count_sum += 1

    return count_sum


if __name__ == '__main__':
    main()
