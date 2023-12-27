MAP_SYMBOLS = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}


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


def onko_validi_suunnasta(location, kartta, suunta_edellisessa):
    # suuntina NESW
    validit = {"N": "F|7", "S": "L|J", "W": "7-J", "E": "L-F" }
    rivi, sarake = location
    # arvot on kartalla
    if 0 <= rivi < len(kartta) and 0 <= sarake < len(kartta[0]):
        if kartta[rivi][sarake] in validit[suunta_edellisessa]:
            return True
    return False


def ensi_askel(location, blocks):
    rivi, sarake = location
    for suunta_tassa, uusi_sijainti in [("N", (rivi - 1, sarake)), ("S", (rivi + 1, sarake)), ("E", (rivi, sarake + 1)), ("W", (rivi, sarake + 1))]:
        if onko_validi_suunnasta(uusi_sijainti, blocks, suunta_tassa):
            return uusi_sijainti


def seuraa_putkea(blocks, start):
    sijainti = ensi_askel(start, blocks)
    reitti = [start]
    while sijainti != start:
        reitti.append(sijainti)
        rivi, sarake = sijainti
        nykyinen = blocks[sijainti[0]][sijainti[1]]
        suunnat = MAP_SYMBOLS[nykyinen]
        suuntaohje = {"N": (rivi - 1, sarake), "S": (rivi + 1, sarake), "E": (rivi, sarake + 1),
                      "W": (rivi, sarake - 1)}
        for suunta in suunnat:
            tutkailtava = suuntaohje[suunta]
            if tutkailtava != reitti[-2] or (len(reitti) > 2 and tutkailtava == reitti[0]):
                sijainti = tutkailtava
                break
    return reitti


def part_one(filename):
    blocks = blockify(filename)
    animal = find_animal(blocks)
    reitti = seuraa_putkea(blocks, animal)
    tulos = int(len(reitti) / 2)
    print(f"{tulos=}")


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
        suunnat = [(rivi - 1, sarake), (rivi + 1, sarake), (rivi, sarake + 1), (rivi, sarake - 1)]
        for suunta in suunnat:
            if 0 <= suunta[0] < len(kartta) and 0 <= suunta[1] < len(kartta[0]) and suunta not in reitin_pisteet and maski[suunta[0]][suunta[1]] != 1:
                pino.append(suunta)
    return maski


def siisti_kartta(reitin_pisteet, kartta):
    kartta = [[merkki for merkki in rivi] for rivi in kartta]
    siistimpi_kartta = poista_ulkopuoli(kartta, reitin_pisteet)
    maski = [['.' for merkki in kartta[0]] for rivi in kartta]
    for rivi in range(len(kartta)):
        for sarake in range(len(kartta[0])):
            if siistimpi_kartta[rivi][sarake] == 1:
                maski[rivi][sarake] = '0'
            else:
                maski[rivi][sarake] = kartta[rivi][sarake]
    return maski


def tulosta_kartta(kartta, filename):
    with open(filename, 'w') as f:
        for rivi in kartta:
            rivi.append('\n')
            f.write(str(''.join(rivi)))


def part_two(filename):
    blocks = [rivi for rivi in blockify(filename) if rivi]
    animal = find_animal(blocks)
    reitti = seuraa_putkea(blocks, animal)
    loppukartta = siisti_kartta(reitti, blocks)
    tulos = 0
    tulosta_kartta(loppukartta, "output4.txt")
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

