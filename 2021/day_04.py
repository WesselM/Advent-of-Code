# https://adventofcode.com/2021/day/4


def main():
    with open("2021\examples\ex_04.txt", "r") as f:
        ex = list(map(str, f.read().split("\n\n")))

    assert part_one(ex) == 4512
    assert part_two(ex) == 1924

    with open("2021\data\input_04.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(subsystem):
    draws = [int(number) for number in subsystem[0].split(",")]
    boards = [[[int(number) for number in row.split()]
               for row in board.split("\n")] for board in subsystem[1:]]
    for i in range(len(draws)):
        for board in boards:
            unmarked = has_bingo(board, draws[:i])
            if unmarked:
                return unmarked * draws[i - 1]


def part_two(subsystem):
    draws = [int(number) for number in subsystem[0].split(",")]
    boards = [[[int(number) for number in row.split()]
               for row in board.split("\n")] for board in subsystem[1:]]
    finished = []
    for board in boards:
        for i in range(len(draws)):
            unmarked = has_bingo(board, draws[:i])
            if unmarked:
                finished.append([unmarked, draws[i - 1], i])
                break

    finished = sorted(finished, key=lambda x: x[2], reverse=True)

    return finished[0][0] * finished[0][1]


def has_bingo(board, drawn):
    for i, row in enumerate(board):
        column = [number[i] for number in board]
        if set(row).issubset(set(drawn)) or set(column).issubset(set(drawn)):
            # Return the sum of the unmarked numbers using a squashed board
            return sum([number for number in [row for row in board for row in row] if number not in drawn])

    return None


if __name__ == '__main__':
    main()
