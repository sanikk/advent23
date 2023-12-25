from math import floor, ceil


def blockify(filename) -> list:
    with open(filename) as f:
        return f.read().split("\n")


def pretty_blocks(blocks) -> list[tuple[int, int]]:
    ajat = [int(x) for x in blocks[0].split(":")[1].split()]
    matkat = [int(x) for x in blocks[1].split(":")[1].split()]
    return [(x, y) for x, y in zip(ajat, matkat)]


def pretty_blocks_for_part_two(blocks) -> tuple[int, int]:
    aika = int("".join([x for x in blocks[0].split(":")[1].split()]))
    matka = int("".join([x for x in blocks[1].split(":")[1].split()]))
    return aika, matka


def laske_ajat(mihin_asti:int, raja: int) -> int:
    osumat = 0
    for i in range(mihin_asti):
        vertailuluku = (mihin_asti - i) * i
        if vertailuluku > raja:
            osumat += 1
        if osumat and vertailuluku < raja:
            return osumat
    return osumat


def laske_ajat_ii(mihin_asti:int, raja: int) -> int:
    osumat = 0
    for i in range(mihin_asti):
        vertailuluku = (mihin_asti - i) * i
        print(f"{i}: {vertailuluku=}, {vertailuluku - raja =}")
        if vertailuluku > raja:
            osumat += 1
        if osumat and vertailuluku < raja:
            return osumat
    return osumat


def laske_nollakohdat(aika, matka):
    x1 = (-aika + (aika**2 - 4 * matka)**0.5) / -2
    x2 = (-aika - (aika**2 - 4 * matka)**0.5) / -2
    return x1, x2


def part_one(filename) -> None:
    races = pretty_blocks(blockify(filename))
    tulokset = [laske_ajat(x, y) for x, y in races]
    tulos = 1
    for x in tulokset:
        tulos *= x
    print(f"{tulos=}")


def part_two(filename) -> None:
    blocks = blockify(filename)
    aika,matka = pretty_blocks_for_part_two(blockify(filename))

    x1, x2 = laske_nollakohdat(aika, matka)
    print(f"{x1=}, {x2=}, {x2 - x1 =}")
    print(f"{ceil(x2) - ceil(x1)}, {ceil(x2) - floor(x1) - 1}, {floor(x2)- floor(x1)}")


if __name__ == "__main__":
    # part_one("06-test-input.txt")
    # part_one("06-input.txt")
    # part_two("06-test-input.txt")
    part_two("06-input.txt")
