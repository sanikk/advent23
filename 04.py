OIKEAT = {}
KORTIN_NUMEROT = {}


def map_numbers(filename):
    with open(filename) as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.strip()
            alku, loppu = rivi.split(":")
            kortti = int(alku.split()[1])
            oikeat, kortin_numerot = loppu.split("|")
            oikeat = oikeat.split()
            kortin_numerot = kortin_numerot.split()
            OIKEAT[kortti] = oikeat
            KORTIN_NUMEROT[kortti] = kortin_numerot


def pisteyta():
    vastaus = 0
    for peli in OIKEAT.keys():
        score = 0
        for numero in OIKEAT[peli]:
            if numero in KORTIN_NUMEROT[peli]:
                score += 1
        if score > 0:
            vastaus += 2**(score - 1)
    print(f"{vastaus=}")


def part_one(filename):
    map_numbers(filename)
    pisteyta()


def pisteyta_toisin():
    lukumaarat = {}
    for i in range(1,len(OIKEAT.keys())+1):
        lukumaarat[i] = 1
    vastaus = 0
    for peli in OIKEAT.keys():
        maara = lukumaarat[peli]
        vastaus += maara
        score = 0
        for numero in OIKEAT[peli]:
            if numero in KORTIN_NUMEROT[peli]:
                score += 1
        if score > 0:
            for i in range(int(peli) + 1, int(peli)+score + 1):
                lukumaarat[i] += maara
    print(f"{vastaus=}")
    print(f"{sum(lukumaarat.values())}")


def part_two(filename):
    map_numbers(filename)
    pisteyta_toisin()


# part_one("04-test-input.txt")
# part_one("04-input.txt")
# part_two("04-test-input.txt")
part_two("04-input.txt")
