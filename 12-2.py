from itertools import product, groupby


def blockify(filename):
    with open(filename) as f:
        return f.read().split("\n")


def poimi_kysymysmerkit(rivi: str) -> list[int]:
    return [i for i, v in enumerate(rivi) if v == '?']


def poimi_pituudet(patka: str) -> list[int]:
    return [int(x) for x in patka.split(",")]


def poimi_lohkot(rivi: str) -> list[int]:
    # [len(list(group[1])) for group in groupby(rivi) if group[0] == "#"]
    lohkot = [i for i, v in enumerate(rivi) if v == '#']
    return lohkot


def preppaa_rivi(rivi: str):
    alku,loppu = rivi.split(" ")
    kysymysmerkit = poimi_kysymysmerkit(alku)
    palautettava_rivi = list(alku) + [loppu]
    return palautettava_rivi, sorted(kysymysmerkit, reverse=True)


def tarkista_rivi(rivi: list[str], pituudet: list[int]):
    tarkistusrivi = [len(list(group[1])) for group in groupby(rivi) if group[0] == "#"]
    return pituudet == tarkistusrivi


def tarkista_rivi_ii(rivi: list[str], tuote, pituudet: list[int], kysymysmerkit):
    itt = groupby(rivi)
    for i, indeksi in enumerate(kysymysmerkit):
        rivi[indeksi] = tuote[i]
    tarkistus = [len(list(group[1])) for group in groupby(rivi) if group[0] == "#"]
    return pituudet == tarkistus


def rekursiivinen(rivi: list[str], kysymysmerkit: list[int]):
    if not kysymysmerkit:
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
    summa = sum(tarkista_rivi_ii(rivi, tuote, pituudet, kysymysmerkit) for tuote in product(merkit, repeat=len(kysymysmerkit)))
    return summa


def ratko_rivi(rivi: str) -> int:
    rivi, kysymysmerkit = preppaa_rivi(rivi)
    return rekursiivinen(list(rivi), kysymysmerkit)


def prosessoi_rivi(rivi: str):
    alku, loppu = rivi.split(" ")
    ryhmat = groupby(alku)
    lista = []
    indeksi = 0
    for merkki, group in ryhmat:
        ryhma = list(group)
        lista.append((indeksi, merkki, ryhma))
        indeksi += len(ryhma)

    kysymysmerkit = [(indeksi, ryhma) for indeksi, merkki, ryhma in lista if merkki == '?']
    lohkot = [(indeksi, ryhma) for indeksi, merkki, ryhma in lista if merkki == "#"]
    pituudet = poimi_pituudet(loppu)

    return kysymysmerkit, lohkot, pituudet


def oo_n(rivi:str):
    # kysymysmerkit, lohkot, pituudet = prosessoi_rivi(rivi)
    pituudet = poimi_pituudet(rivi.split(" ")[1])
    vastaus = 1
    kysymysmerkkeja = 0
    lohkon_pituus = 0
    pituus_plus_kysymysmerkit = 0
    for kohta, merkki in enumerate(rivi):
        if merkki == '?':
            monellako += 1
        elif monellako > 0:
            vastaus += monellako
            monellako = 0
        if merkki == '#':
            lohkon_pituus += 1
        else:
            # lohko loppui!
            pass

def laskennallinen(rivi: str):
    # yhteispaino = [1,1,3]
    # tekis mieli ottaa tuolta toi 3 ja 3 pois
    # ja katsoa loppua: ??? ja 1,1...hmm
    #
    #
    #
    vastaus = 1
    kysymysmerkit, lohkot, pituudet = prosessoi_rivi(rivi)
    lohkojen_pituudet = [len(x[1]) for x in lohkot]

    print(f"{lohkot=}")
    print(f"{lohkojen_pituudet=}")
    for pituus in sorted(pituudet, reverse=True):
        if pituus in lohkojen_pituudet:
            vastaus *= pituus # joo sain toisen idean, katotaan kohta
        print(pituus)
    return vastaus

def part_one(filename):
    blocks = [rivi for rivi in blockify(filename) if rivi]
    # rekursiivisella
    # print(f"vastaus = {sum(ratko_rivi(rivi) for rivi in blocks)}")
    # suoralla
    # print(f"suoralla vastaus = {sum(suora(rivi) for rivi in blocks)}")
    print(laskennallinen(blocks[0]))

def part_two(filename):
    blocks = blockify(filename)


if __name__ == "__main__":
    part_one("12-test-input-1.txt")
    # part_one("12-input.txt")
