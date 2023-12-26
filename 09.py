def blockify(filename):
    with open(filename) as f:
        return f.read().split("\n")


def handle_rivi(rivi):
    rivi = [int(x) for x in rivi.split()]
    erotukset = rivi
    kasa = []
    while not erotukset or [x for x in erotukset if x != 0]:
        erotukset = [erotukset[i] - erotukset[i - 1] for i in range(1, len(erotukset))]
        kasa.append(erotukset[-1])
    lisays = sum(kasa)
    rivin_tulos = rivi[-1] + lisays
    return rivin_tulos


def handle_rivi_for_part_two(rivi):
    rivi = [int(x) for x in rivi.split()]
    erotukset = rivi
    kasa = []
    while not erotukset or [x for x in erotukset if x != 0]:
        erotukset = [erotukset[i] - erotukset[i - 1] for i in range(1, len(erotukset))]
        kasa.append(erotukset[0])
    poisto = 0
    for arvo in reversed(kasa):
        poisto = arvo - poisto
    rivin_tulos = rivi[0] - poisto
    return rivin_tulos


def part_one(filename):
    blocks = blockify(filename)
    tulos = 0
    for rivi in blocks:
        if not rivi:
            continue
        rivin_tulos = handle_rivi(rivi)
        tulos += rivin_tulos
    print(f"{tulos=}")


def part_two(filename):
    blocks = blockify(filename)
    tulos = 0
    for rivi in blocks:
        if not rivi:
            continue
        rivin_tulos = handle_rivi_for_part_two(rivi)
        tulos += rivin_tulos
    print(f"{tulos=}")


if __name__ == "__main__":
    # part_one("09-test-input.txt")
    # part_one("09-input.txt")
    part_two("09-test-input.txt")
    part_two("09-input.txt")
