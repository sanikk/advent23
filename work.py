from enum import Enum


def blockify(filename):
    with open(filename) as f:
        return f.read().split("\n")


def find_animal(blocks):
    animal = None
    rivinro = 0
    for rivi in blocks:
        if "S" in rivi:
            return rivinro, rivi.find("S")
        rivinro += 1


def ensi_askel(location, blocks):
    rivi, sarake = location
    if rivi > 0 and blocks[rivi - 1][sarake] in "F|7":
        return rivi - 1, sarake
    elif rivi < len(blocks) and blocks[rivi + 1][sarake] in "L|J":
        return rivi + 1, sarake
    elif sarake > 0 and blocks[rivi][sarake - 1] in "7-J":
        return rivi, sarake - 1
    elif sarake < len(blocks[0]) - 1 and blocks[rivi][sarake + 1] in "L-F":
        return rivi, sarake + 1
    else:
        print(f"{rivi=}, {sarake=}")
    return None


def seuraa_putkea(sijainti, blocks, eka, vika):
    rivi, sarake = sijainti
    map_symbols = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}
    nykyinen = blocks[sijainti[0]][sijainti[1]]
    suunnat = map_symbols[nykyinen]
    for suunta in suunnat:
        tutkailtava = (rivi - 1, sarake)
        if suunta == "N" and (tutkailtava != vika or tutkailtava == eka):
            return rivi - 1, sarake
        tutkailtava = (rivi + 1, sarake)
        if suunta == "S" and (tutkailtava != vika or tutkailtava == eka):
            return tutkailtava
        tutkailtava = (rivi, sarake - 1)
        if suunta == "W" and (tutkailtava != vika or tutkailtava == eka):
            return rivi, sarake - 1
        tutkailtava = (rivi, sarake + 1)
        if suunta == "E" and (tutkailtava != vika or tutkailtava == eka):
            return rivi, sarake + 1


def actually_follow(start, blocks):
    sijainti = ensi_askel(start, blocks)
    reitti = [start]
    while sijainti != start:
        reitti.append(sijainti)
        if len(reitti) > 2:
            sijainti = seuraa_putkea(sijainti, blocks, reitti[0], reitti[-2])
        else:
            sijainti = seuraa_putkea(sijainti, blocks, None, reitti[-2])
    return [(sijainti, blocks[sijainti[0]][sijainti[1]]) for sijainti in reitti]


def part_one(filename):
    blocks = blockify(filename)
    animal = find_animal(blocks)
    reitti = actually_follow(animal, blocks)
    tulos = int(len(reitti) / 2)
    print(f"{tulos=}")

#    map_symbols = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}
#        tutkailtava = (rivi - 1, sarake)


def poista_ulkopuoli(kartta, reitin_pisteet):
    # Oletetaan että ulkopuoli on yhtänäinen, kuten tehtävissä, jokaisesta pisteestä on pääsy jokaiseen pisteeseen.
    # Ison kartan alue rajoittuu oikeasta reunasta seinään, mutta jokaiseen ulkopuolen pisteeseen pääsee edelleen
    # kiertämällä.

    # tjaahas tuo squeeze unohtui, eli pitää vähän lisätä sinne sääntöä. tarkistetaan onko reitin putkea vai ei,
    # piirtämisen varalta, mutta tungetaan kuitenkin pinoon kun se tunkee sieltä välistä
    # pistelasku myös väärin, ilmeisesti lasketaan myös ruudut joissa on luuppiin liittämättömiä putkia.

    pino = [(0, 0)]
    maski = [[0 for merkki in kartta[0]] for rivi in kartta]
    while pino:
        rivi, sarake = pino.pop()
        maski[rivi][sarake] = 1
        ylhaalla = (rivi - 1, sarake)
        vasemmalla = (rivi, sarake - 1)
        oikealla = (rivi, sarake + 1)
        alhaalla = (rivi + 1, sarake)
        if rivi > 0 and ylhaalla not in reitin_pisteet and maski[rivi - 1][sarake] != 1:
            pino.append(ylhaalla)
        if sarake > 0 and vasemmalla not in reitin_pisteet and maski[rivi][sarake - 1] != 1:
            pino.append(vasemmalla)
        if rivi < len(kartta) - 1 and alhaalla not in reitin_pisteet and maski[rivi + 1][sarake] != 1:
            pino.append(alhaalla)
        if sarake < len(kartta[0]) - 1 and oikealla not in reitin_pisteet and maski[rivi][sarake + 1] != 1:
            pino.append(oikealla)
    return maski


def siisti_kartta(reitin_pisteet, kartta):
    kartta = [[merkki for merkki in rivi] for rivi in kartta]
    siistimpi_kartta = poista_ulkopuoli(kartta, reitin_pisteet)
    loppukartta = [['.' for merkki in kartta[0]] for rivi in kartta]
    for rivi in range(len(kartta)):
        for sarake in range(len(kartta[0])):
            if siistimpi_kartta[rivi][sarake] == 1:
                loppukartta[rivi][sarake] = '0'
            else:
                loppukartta[rivi][sarake] = kartta[rivi][sarake]
    return loppukartta

def part_two(filename):
    blocks = blockify(filename)
    blocks = [rivi for rivi in blocks if rivi]
    animal = find_animal(blocks)
    reitti = actually_follow(animal, blocks)
    loppukartta = siisti_kartta([x[0] for x in reitti], blocks)
    tulos = 0
    for rivi in loppukartta:
        tulos += rivi.count(".")
    print(f"{tulos=}")


if __name__ == "__main__":
    # part_one("10-test-input1.txt")
    # part_one("10-test-input2.txt")
    # part_one("10-test-input3.txt")
    # part_one("10-test-input4.txt")
    # part_one("10-input.txt")
    part_two("10-test-input-5.txt")
    # part_two("10-input.txt")
# map_symbols = {"|": "N-S", "-": "E-W", "L": "N-E", "J": "N-W", "7": "S-W", "F": "S-E"}
# .     No pipe
# S     Animal starts here
