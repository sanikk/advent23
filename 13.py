def blockify(filename):
    with open(filename) as f:
        return [osa.split() for osa in f.read().split("\n\n")]


def poikittain(kartta:list):
    for i, rivi in enumerate(kartta):
        if i == 0:
            continue
        if rivi == kartta[i - 1]:
            mahdollinen = True
            for j in range(1, min(i, len(kartta) - i)):
                if kartta[i - j - 1] != kartta[i + j]:
                    mahdollinen = False
            if mahdollinen:
                return i
    return 0


def pitkittain(kartta:list):
    kaannetty = list(zip(*kartta))
    return poikittain(kaannetty)


def part_one(filename):
    blocks = blockify(filename)
    print(sum(poikittain(block) * 100 + pitkittain(block) for block in blocks))


def converter(merkki:str):
    if merkki == ".":
        return '0'
    if merkki == "#":
        return '1'


def testi_numeroina(kartta:list[str]):
    for testattava, arvo in enumerate(kartta):
        erotus = 0
        for tarkistus in range(min(testattava, len(kartta) - testattava)):
            erotus += sum(1 for a, b in zip(list(str(kartta[testattava + tarkistus])), list(str(kartta[testattava - tarkistus - 1]))) if a != b)
            if erotus > 1:
                break
        if erotus == 1:
            return testattava
    return 0


def valmistus_numeroina(kartta:list[str]):
    palautusarvo = 0
    kartta_numeroiksi = [[converter(merkki) for merkki in rivi] for rivi in kartta]
    rivit_lukuina = ["".join(rivi) for rivi in kartta_numeroiksi]
    palautusarvo += testi_numeroina(rivit_lukuina) * 100
    kaannetty = list(zip(*kartta_numeroiksi))
    sarakkeet_lukuina = ["".join(rivi) for rivi in kaannetty]
    if palautusarvo:
        return palautusarvo
    palautusarvo += testi_numeroina(sarakkeet_lukuina)

    # jotain taisi mennä pieleen jos palautusarvo on 0
    if palautusarvo == 0:
        with open("virheet.txt", "a") as f:
            for rivi in kartta:
                f.write(rivi+"\n")
            f.write("\n")
        print("TYHJÄ!!!")

    return palautusarvo


def part_two(filename):
    vastaus = 0
    blocks = blockify(filename)
    for block in blocks:
        vastaus += valmistus_numeroina(block)
    print(f"{vastaus=}")


if __name__ == "__main__":
    # part_one("13-test-input.txt")
    # part_one("13-input.txt")
    part_two("13-test-input.txt")
    part_two("13-input.txt")
