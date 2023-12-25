def blockify(filename):
    with open(filename) as f:
        data = f.read()
        data = data.split("\n")
        return data[0], data[2:]


def kartoita(kartta):
    lista = [x.split() for x in kartta]
    palautettava = {yksi_kartta[0]: (yksi_kartta[2][1:-1], yksi_kartta[3][:-1]) for yksi_kartta in lista if yksi_kartta}
    return palautettava


def part_one(filename):
    reitti, kartta = blockify(filename)
    kartta = kartoita(kartta)
    step = 0
    kohta = 'AAA'
    while kohta != 'ZZZ':
        askel = reitti[step % len(reitti)]
        ohje = kartta[kohta]
        if askel == 'L':
            kohta = ohje[0]
        elif askel == 'R':
            kohta = ohje[1]
        else:
            print("WUT")
        step += 1
    print(f"{step=}")


def part_two(filename):
    blocks = blockify(filename)


if __name__ == "__main__":
    part_one("08-test-input1.txt")
    part_one("08-test-input2.txt")
    part_one("08-input.txt")
    # part_two("input.txt")
