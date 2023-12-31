import math


def blockify(filename):
    with open(filename) as f:
        return f.read().split("\n")


def muuta_suuntaan(suunta:str, rivi:int, sarake:int, korkeus:int, leveys:int):
    if suunta == "N":
        if rivi == 0:
            return None
        return rivi - 1, sarake
    if suunta == "S":
        if rivi == korkeus - 1:
            return None
        return rivi + 1, sarake
    if suunta == "W":
        if sarake == 0:
            return None
        return rivi, sarake - 1
    if suunta == "E":
        if sarake == leveys - 1:
            return None
        return rivi, sarake + 1


def jarjestetyt(kivet, suunta):
    if suunta == "N":
        return sorted(kivet)
    if suunta == "S":
        return sorted(kivet, reverse=True)
    if suunta == "E":
        return sorted(kivet, key=lambda x: x[1], reverse=True)
    if suunta == "W":
        return sorted(kivet, key=lambda x: x[1])


def tilt(suunta: str, pyoreat: list, kiinteat: list, korkeus: int, leveys: int):
    lopulliset = []
    for kivi in jarjestetyt(pyoreat, suunta):
        valmis = False
        while not valmis:
            ehdokas = muuta_suuntaan(suunta, kivi[0], kivi[1], korkeus, leveys)
            if not ehdokas or ehdokas in kiinteat or ehdokas in lopulliset:
                valmis = True
            else:
                kivi = ehdokas
        lopulliset.append(kivi)
    return lopulliset


def etsi_kivet(kartta: list):
    pyoreat = [(rivinro, sarakenro) for rivinro, rivi in enumerate(kartta) for sarakenro, sarake in
               enumerate(kartta[rivinro]) if sarake == "O"]
    kiinteat = [(rivinro, sarakenro) for rivinro, rivi in enumerate(kartta) for sarakenro, sarake in
                enumerate(kartta[rivinro]) if sarake == "#"]
    return pyoreat, kiinteat


def score(kivet:list, korkeus:int):
    return sum(korkeus - x[0] for x in kivet)


def korvaa_kivet_maalla(merkki:str):
    if merkki == "O":
        return "."
    return merkki


def piirra_kivet_pohjaan(pohja, kivet:list[tuple]):
    kopio = [[merkki for merkki in rivi] for rivi in pohja]
    for kivi in kivet:
        kopio[kivi[0]][kivi[1]] = "O"
    for rivi in kopio:
        print("".join(rivi))


def etsi_luuppi(kartta, laskuri, lista=[]):
    #tehdään joku hash tosta kartasta, lyödään listaan.
    hasa = hash(str(kartta))
    if hasa not in lista:
        lista.append(hasa)

    else:
        print(f"Hasa oli aiemmin indeksissä {lista.index(hasa)}, nyt {laskuri=}.")
        return False
    return True


def repeater(kartta:list, cycles: int):
    toistoja = 10
    korkeus = len(kartta)
    leveys = len(kartta[0])
    kasiteltava, kiinteat = etsi_kivet(kartta)
    pohja = [[korvaa_kivet_maalla(merkki) for merkki in rivi] for rivi in kartta]
    edelliset = []
    jatketaan = True
    laskuri = 0
    luupin_alku, luupin_pituus = None, None
    while jatketaan:
        if laskuri == toistoja:
            print(f"{laskuri=}")
            toistoja *= 10
        for suunta in "NWSE":
            kasiteltava = tilt(suunta, kasiteltava, kiinteat, korkeus, leveys)
        laskuri += 1
        if not luupin_alku:
            kartta_yhtena_stringina = "".join([str(10 * a + b) for a, b in kasiteltava])
            if kartta_yhtena_stringina in edelliset:
                luupin_alku = edelliset.index(kartta_yhtena_stringina)
                luupin_pituus = laskuri - luupin_alku - 1
                print(f"{luupin_alku=}, {luupin_pituus=}, {laskuri=}")
                laskuri += luupin_pituus * math.floor((cycles - laskuri) / luupin_pituus)
            else:
                edelliset.append(kartta_yhtena_stringina)
        if laskuri >= cycles:
            jatketaan = False
    return score(kasiteltava, korkeus)


def part_one(filename):
    blocks = [line for line in blockify(filename) if line]
    pyoreat, kiinteat = etsi_kivet(blocks)
    lopulliset = tilt("N", pyoreat, kiinteat, len(blocks), len(blocks[0]))
    print(score(lopulliset, len(blocks)))


def part_two(filename):
    blocks = [line for line in blockify(filename) if line]
    cycles = 1000000000
    lopulliset = repeater(blocks, cycles)
    print(lopulliset)


if __name__ == "__main__":
    # part_one("14-test-input-1.txt")
    # part_one("14-input.txt")
    # part_two("14-test-input-1.txt")
    part_two("14-input.txt")
