import itertools


def blockify(filename):
    with open(filename) as f:
        return f.read().split("\n")


def poimi_kysymysmerkit(rivi: str) -> list[int]:
    return [i for i, v in enumerate(rivi) if v == '?']


def poimi_pituudet(patka: str) -> list[int]:
    return [int(x) for x in patka.split(",")]


def poimi_lohkot(rivi: str) -> list[int]:
    lohkot = [i for i, v in enumerate(rivi) if v == '#']
    return lohkot


def preppaa_rivi(rivi: str):
    alku,loppu = rivi.split(" ")
    kysymysmerkit = poimi_kysymysmerkit(alku)
    alku = list(alku) + [loppu]
    return alku, sorted(kysymysmerkit, reverse=True)


def tarkista_rivi(rivi: list[str], pituudet: list[int]):
    itt = itertools.groupby(rivi)
    tarkistus = [len(list(group[1])) for group in itertools.groupby(rivi) if group[0] == "#"]
    return pituudet == tarkistus


def tarkista_rivi_ii(rivi: list[str], tuote, pituudet: list[int], kysymysmerkit):
    itt = itertools.groupby(rivi)
    for i, indeksi in enumerate(kysymysmerkit):
        rivi[indeksi] = tuote[i]
    tarkistus = [len(list(group[1])) for group in itertools.groupby(rivi) if group[0] == "#"]
    return pituudet == tarkistus


def rekursiivinen(rivi: list[str], kysymysmerkit: list[int]):
    if len(kysymysmerkit) == 0:
        arvo = tarkista_rivi(rivi[:-1], poimi_pituudet(rivi[-1]))
        return int(arvo)
    eka_kysymysmerkki = kysymysmerkit.pop()

    rivi[eka_kysymysmerkki] = "#"
    palautettava = rekursiivinen(rivi, kysymysmerkit)
    rivi[eka_kysymysmerkki] = "."
    palautettava += rekursiivinen(rivi, kysymysmerkit)
    rivi[eka_kysymysmerkki] = '?'
    kysymysmerkit.append(eka_kysymysmerkki)

    return palautettava


def suora(rivi: str):
    rivi, kysymysmerkit = preppaa_rivi(rivi)
    *alku, pituudet = rivi
    pituudet = [int(x) for x in pituudet.split(",")]
    merkit = ['#', '.']
    kysymysmerkit = poimi_kysymysmerkit(alku)
    summa = sum(tarkista_rivi_ii(rivi, tuote, pituudet, kysymysmerkit) for tuote in itertools.product(merkit, repeat=len(kysymysmerkit)))
    return summa


def ratko_rivi(rivi: str) -> int:
    rivi, kysymysmerkit = preppaa_rivi(rivi)
    return rekursiivinen(list(rivi), kysymysmerkit)


def part_one(filename):
    blocks = [rivi for rivi in blockify(filename) if rivi]
    # rekursiivisella
    print(f"vastaus = {sum(ratko_rivi(rivi) for rivi in blocks)}")
    # suoralla
    print(f"suoralla vastaus = {sum(suora(rivi) for rivi in blocks)}")


def part_two(filename):
    blocks = blockify(filename)


if __name__ == "__main__":
    part_one("12-test-input-1.txt")
    part_one("12-input.txt")
