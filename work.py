import math
import itertools


def blockify(filename):
    with open(filename) as f:
        return f.read().split("\n")


def tulosta_kartta(kartta, filename):
    with open(filename, 'w') as f:
        for rivi in kartta:
            rivi.append('\n')
            f.write(str(''.join(rivi)))


def find_galaxies(kartta):
    galaxit = []
    for i, rivi in enumerate(kartta):
        for j, sarake in enumerate(kartta[i]):
            if kartta[i][j] == "#":
                galaxit.append((i,j))

    return galaxit


def scan_stuff(kartta):
    # tyhjat_rivit = [i for i, v in enumerate(kartta) if v.count(".") == len(v)]
    galaxies = find_galaxies(kartta)
    x_sarake = [x[0] for x in galaxies]
    tyhjat_rivit = [rivi for rivi in range(len(kartta)) if rivi not in x_sarake]
    y_sarake = [y[1] for y in galaxies]
    tyhjat_sarakkeet = [sarake for sarake in range(len(kartta[0])) if sarake not in y_sarake]
    return galaxies, tyhjat_rivit, tyhjat_sarakkeet


def expand_space(kartta, tyhjat_rivit, tyhjat_sarakkeet):
    uusi_kartta = []
    uusi_tyhja_rivi = (len(kartta[0]) + len(tyhjat_sarakkeet)) * ["."]
    kartta = [list(line) for line in kartta]
    for rivi in range(len(kartta)):
        if rivi in tyhjat_rivit:
            uusi_kartta.append(uusi_tyhja_rivi)
            uusi_kartta.append(uusi_tyhja_rivi)
        else:
            alku = 0
            uusi_rivi = []
            for sarake in tyhjat_sarakkeet:
                uusi_rivi += kartta[rivi][alku:sarake + 1]
                # lisätään toi sarake kahdesti niin se tuplautuu
                alku = sarake
            uusi_rivi += kartta[rivi][alku:]
            uusi_kartta.append(uusi_rivi)
    return uusi_kartta


def expand_space_with_numbers(galaxies, tyhjat_rivit, tyhjat_sarakkeet):
    uudet_galaxit = {}

    for galaxy in galaxies:
        indeksi = len(uudet_galaxit.keys())
        rivi, sarake = galaxy
        sarakelisa = sum(1 for tyhja_sarake in tyhjat_sarakkeet if tyhja_sarake < sarake)
        rivilisa = sum(1 for tyhja_rivi in tyhjat_rivit if tyhja_rivi < rivi)
        uudet_galaxit[indeksi] = (rivi + rivilisa, sarake + sarakelisa)
    return uudet_galaxit


def shortest_paths(galaxit:dict):
    summa = 0
    toiset_parit = [(x, y) for x in galaxit.keys() for y in galaxit.keys() if x < y]
    print(f"{len(toiset_parit)=}")
    for eka,toka in toiset_parit:
        eka_sijainti = galaxit[eka]
        toka_sijainti = galaxit[toka]
        etaisyys = abs(eka_sijainti[0] - toka_sijainti[0]) + abs(eka_sijainti[1] - toka_sijainti[1])
        summa += etaisyys
    return summa


def part_one(filename):
    kartta = [line for line in blockify(filename) if line]
    galaxies, tyhjat_rivit, tyhjat_sarakkeet = scan_stuff(kartta)
    # uusi_kartta = ["".join(rivi) for rivi in expand_space(kartta, tyhjat_rivit, tyhjat_sarakkeet)]
    # vertailu, *roskaa = scan_stuff(uusi_kartta)
    uudet_galaxit = expand_space_with_numbers(galaxies, tyhjat_rivit, tyhjat_sarakkeet)
    komboja = math.comb(len(uudet_galaxit.keys()), 2)
    print(f"{komboja=}")
    print(shortest_paths(uudet_galaxit))


def part_two(filename):
    kartta = [line for line in blockify(filename) if line]
    tyhjat_rivit = [i for i, v in enumerate(kartta) if v.count(".") == len(v)]
    print(tyhjat_rivit)


if __name__ == "__main__":
    part_one("11-test-input-1.txt")
    part_one("11-input.txt")
    # part_two("input.txt")