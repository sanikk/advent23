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


def tulosta_kartta(kartta, filename):
    with open(filename, 'w') as f:
        for rivi in kartta:
            rivi.append('\n')
            f.write(str(''.join(rivi)))


def kenkis(reitti):
    # lasketaan ala tästä
    summa = 0
    for i, v in enumerate(reitti):
        if i == 0: continue
        rivi, sarake = v
        summa += reitti[i - 1][0] * sarake - reitti[i - 1][1] * rivi
    summa += reitti[-1][0] * reitti[0][1] - reitti[-1][1] * reitti[0][0]
    return abs(summa)


def reitin_merkit(reitti, kartta):
    return [kartta[rivi][sarake] for rivi,sarake in reitti]


def part_two(filename):
    blocks = [rivi for rivi in blockify(filename) if rivi]
    animal = find_animal(blocks)
    reitti = seuraa_putkea(blocks, animal)
    #testataan
    kolmioala = kenkis(reitti) / 2
    merkit = reitin_merkit(reitti, blocks)
    pisteita = 0
    for merkki in "7FLJ|-S":
        pisteita += merkit.count(merkki)
    vastaus = kolmioala - pisteita / 2 + 1
    print(f"{vastaus=}")
    # A = i + b/2 -1
    # i = A - b/2 + 1
    # kolmioala - pisteita / 2 + 1
    # missä i on sisäpisteet ja b reunalla


if __name__ == "__main__":
    part_two("10-test-input-last.txt")
    part_two("10-input.txt")
