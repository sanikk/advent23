def blockify(filename):
    with open(filename) as f:
        return f.read().split("\n")


def part_one(filename):
    blocks = blockify(filename)


def part_two(filename):
    blocks = blockify(filename)


if __name__ == "__main__":
    part_one("input.txt")
    part_two("input.txt")