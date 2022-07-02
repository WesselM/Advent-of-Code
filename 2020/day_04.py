# https://adventofcode.com/2020/day/4

from re import match


def main():
    with open("2020\examples\ex_04.txt", "r") as f:
        ex = list(map(str, f.read().split("\n\n")))

    assert part_one(ex) == 2
    assert part_two(ex) == 2

    with open("2020\data\input_04.txt", "r") as f:
        inp = list(map(str, f.read().strip().split("\n\n")))

    print("Part one:", part_one(inp))
    print("Part two:", part_two(inp))


def part_one(passports):
    valids = 0
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in passports:
        cnt = 0
        for field in req_fields:
            if field in passport:
                cnt += 1
        if cnt == 7:
            valids += 1

    return valids


def part_two(passports):
    valids = 0
    for passport in passports:
        field = dict(fields.split(":")
                     for fields in passport.replace("\n", " ").split(" "))
        if "byr" in field and 1920 <= int(field["byr"]) <= 2002 and \
            "iyr" in field and 2010 <= int(field["iyr"]) <= 2020 and \
            "eyr" in field and 2020 <= int(field["eyr"]) <= 2030 and \
            "hgt" in field and ((field["hgt"][-2:] == "cm" and 150 <= int(field["hgt"][0:-2]) <= 193) or (field["hgt"][-2:] == "in" and 59 <= int(field["hgt"][0:-2]) <= 76)) and \
            "hcl" in field and match(r"^#[0-9a-f]{6}$", field["hcl"]) and \
            "ecl" in field and field["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth") and \
                "pid" in field and len(field["pid"]) == 9 and field["pid"].isnumeric():
            valids += 1

    return valids


if __name__ == '__main__':
    main()
