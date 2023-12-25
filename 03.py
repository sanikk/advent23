NUMBERS = {}
SYMBOLS = {}
STARS = []


def map_things(filename):
    rivinro = 0
    with open(filename) as tiedosto:
        for rivi in tiedosto:
            rivin_symbolit = []
            rivin_numerot = []
            rivi = rivi.strip()
            i = 0
            while i < len(rivi):
                lisays_per_kierros = 1
                if rivi[i] != ".":
                    patka = None
                    if rivi[i].isnumeric():
                        for j in range(1, 5):
                            if not patka and i+j == len(rivi):
                                patka = rivi[i:]
                            if not patka and i+j < len(rivi) and not rivi[i+j].isnumeric():
                                patka = rivi[i:i+j]
                        rivin_numerot.append((rivinro, i, i+len(patka) - 1, int(patka)))
                        lisays_per_kierros = len(patka)
                    else:
                        rivin_symbolit.append(i)
                        if rivi[i] == "*":
                            STARS.append((rivinro, i, rivi[i]))
                i += lisays_per_kierros
            NUMBERS[rivinro] = rivin_numerot
            SYMBOLS[rivinro] = rivin_symbolit
            rivinro += 1
    rivien_range = rivinro


def validoi_numero(rivinro, alku, loppu, arvo):
    for rivi in range(max(0, rivinro - 1), min(len(SYMBOLS.keys()), rivinro + 2)):
        for sarake in range(alku - 1, loppu + 2):
            if sarake in SYMBOLS[rivi]:
                return True
    return False


def kaydaan_numerot_lapi():
    vastaus = 0
    for i in range(len(SYMBOLS.keys())):
        kasiteltava_rivi = NUMBERS[i]
        for roska, alku, loppu, arvo in kasiteltava_rivi:
            if validoi_numero(i, alku, loppu, arvo):
                vastaus += arvo 
    print(f"{vastaus=}")


def part_one(filename):
    map_things(filename)
    kaydaan_numerot_lapi()


def kaydaan_tahdet_lapi():
    vastaus = 0
    for tahden_rivi,tahden_sarake,tahden_arvo in STARS:
        osumat = []
        for numeron_rivi in range(max(0,tahden_rivi-1), min(len(NUMBERS.keys()),tahden_rivi + 2)):
            for roska, alku, loppu, arvo in NUMBERS[numeron_rivi]:
                if alku - 2 < tahden_sarake < loppu + 2:
                    osumat.append(arvo)
        if len(osumat) == 2:
            vastaus += osumat[0] * osumat[1]
    print(f"{vastaus=}")


def part_two(filename):
    map_things(filename)
    kaydaan_tahdet_lapi()


# main("03-test-input.txt")
# part_one("03-input.txt")
part_two("03-input.txt")
# part_two("03-test-input.txt")
