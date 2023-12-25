from operator import itemgetter


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


def poimi_alut_ja_loput(kartta):
    alut = [x for x in kartta.keys() if x[2] == 'A']
    loput = [x for x in kartta.keys() if x[2] == 'Z']
    return alut, loput


def tarkista_tilanne(tilanne, maalit):
    for kohta in tilanne:
        if kohta not in maalit:
            return False
    return True


def part_two_analyze_cycles(filename):
    joku = []
    reitti, kartta = blockify(filename)
    kartta = kartoita(kartta)
    alut, loput = poimi_alut_ja_loput(kartta)
    for yksi_reitti in alut:
        step = 0
        kohta = yksi_reitti
        osumat = 0
        eka = 0
        toka = 0
        # while osumat < 2:
        while osumat == 0:
            askel = reitti[step % len(reitti)]
            if askel == "L":
                askel = 0
            else:
                askel = 1
            kohta = kartta[kohta][askel]
            step += 1
            if kohta in loput:
                osumat += 1
                if not eka:
                    eka = step
        joku.append((yksi_reitti, eka))
    return joku


def part_two_checker(vertailuluku:int, reitit):

    for reitti in reitit:
        if vertailuluku % reitti[1] != 0:
            return False
    return True


def anna_luvun_tekijat(luku:int):
    return [i for i in range(2, luku) if luku % i == 0]


def part_two_solver(filename):
    cycles = part_two_analyze_cycles(filename)
    sortatut = sorted(cycles, key=itemgetter(1))
    tekijat = [anna_luvun_tekijat(x[1]) for x in sortatut]
    flatlist = sum(tekijat, [])
    lukumaarat = sorted([(flatlist.count(luku), luku) for luku in set(flatlist)], key=itemgetter(1), reverse=True)
    tulo = 1
    if lukumaarat[0][0] == len(tekijat):
        tulo = lukumaarat[0][1]
    divided_by_common = [int(x[1] / tulo) for x in sortatut]
    for luku in tekijat:
        tulo *= luku[0]
    print(f"{tulo=}")


if __name__ == "__main__":
    # part_one("08-test-input1.txt")
    # part_one("08-test-input2.txt")
    # part_one("08-input.txt")
    # part_two_solver("08-test-input3.txt")
    part_two_solver("08-input.txt")

