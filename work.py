def blockify(filename):
    with open(filename) as f:
        return f.read()


def HASHfunction_ii(feed: str):
    current = 0
    for merkki in feed:
        current += ord(merkki)
        current *= 17
        current = current % 256
        yield current

def HASHfunction(feed: str):
    current = 0
    for merkki in feed:
        if merkki == ",":
            continue
        current += ord(merkki)
        current *= 17
        current = current % 256
        yield current


def kasittele_patka(patka: str):
    current = 0
    for merkki in patka:
        current += ord(merkki)
        current *= 17
        current = current % 256
    return current


def part_one(filename):
    blocks = blockify(filename)
    print(sum(kasittele_patka(patka) for patka in blocks.split(',')))


def part_two(filename):
    blocks = blockify(filename)


if __name__ == "__main__":
    part_one("15-test-input-1.txt")
    part_one("15-input.txt")


