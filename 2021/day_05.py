# https://adventofcode.com/2021/day/5


def main():
    with open("2021\examples\ex_05.txt", "r") as f:
        ex = list(map(str, f.read().split("\n")))

    assert part_one(ex) == 5
    assert part_two(ex) == 12

    with open("2021\data\input_05.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(lines):
    field = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        point1, point2 = list(line.split(' -> '))
        x1, y1 = map(int, point1.split(','))
        x2, y2 = map(int, point2.split(','))
        # Horizontal
        if (y1 == y2):
            for i in range(max(x1, x2) + 1 - min(x1, x2)):
                field[y1][min(x1, x2) + i] += 1
        # Vertical
        elif (x1 == x2):
            for i in range(max(y1, y2) + 1 - min(y1, y2)):
                field[min(y1, y2) + i][x1] += 1

    return len([point for point in [points for row in field for points in row] if point > 1])


def part_two(lines):
    field = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        point1, point2 = list(line.split(' -> '))
        x1, y1 = map(int, point1.split(','))
        x2, y2 = map(int, point2.split(','))
        # Horizontal
        if (y1 == y2):
            for i in range(max(x1, x2) + 1 - min(x1, x2)):
                field[y1][min(x1, x2) + i] += 1
        # Vertical
        elif (x1 == x2):
            for i in range(max(y1, y2) + 1 - min(y1, y2)):
                field[min(y1, y2) + i][x1] += 1
        # Diagonal
        if (x1 != x2 and y1 != y2):
            if (x1 < x2 and y1 < y2):
                for i in range(x2 + 1 - x1):
                    field[y1 + i][x1 + i] += 1
            elif (x1 > x2 and y1 < y2):
                for i in range(x1 + 1 - x2):
                    field[y1 + i][x1 - i] += 1
            elif (x1 < x2 and y1 > y2):
                for i in range(x2 + 1 - x1):
                    field[y1 - i][x1 + i] += 1
            elif (x1 > x2 and y1 > y2):
                for i in range(x1 + 1 - x2):
                    field[y1 - i][x1 - i] += 1

    print_board(field)

    return len([point for point in [points for row in field for points in row] if point > 1])


def print_board(board):
    file = open("2021\output_2021_05.txt", "w")
    for row in board:
        for item in row:
            file.write(". ") if item == 0 else file.write(str(item) + " ")
        file.write("\n")
    file.close


if __name__ == '__main__':
    main()
