def blockify(filename):
    with open(filename) as f:
        return f.read().split("\n")


# suunnat
#    1
#  4   2    \
#    3
# niin peilit yms kääntää helposti suuntaa

def the_slash_mirror(rivi, sarake, suunta, the_slash):
    if suunta == 1:
        if the_slash:
            return rivi, sarake + 1, 2
        return rivi, sarake - 1, 4
    if suunta == 2:
        if the_slash:
            return rivi - 1, sarake, 1
        return rivi + 1, sarake, 3
    if suunta == 3:
        if the_slash:
            return rivi, sarake - 1, 4
        return rivi, sarake + 1, 2
    if suunta == 4:
        if the_slash:
            return rivi + 1, sarake, 3
        return rivi - 1, sarake, 1


def poimi_kaikki(kartta: list):
    peilit = [(rivinro, sarakenro) for rivinro, rivi in enumerate(kartta) for sarakenro, sarake in
              enumerate(kartta[rivinro]) if sarake == "/" or sarake == "\\"]
    jakajat = [(rivinro, sarakenro) for rivinro, rivi in enumerate(kartta) for sarakenro, sarake in
               enumerate(kartta[rivinro]) if sarake == "|" or sarake == "-"]
    return peilit, jakajat


def beam_on_you_brute(kartta, rivi, sarake, suunta):
    valaistuskartta = [[[] for merkki in rivi] for rivi in kartta]
    pino = [(rivi, sarake, suunta)]
    while pino:
        rivi, sarake, suunta = pino.pop()
        jatkaa = True
        while jatkaa:
            if not (0 <= rivi < len(kartta)) or not (0 <= sarake < len(kartta[0])) or suunta in valaistuskartta[rivi][sarake]:
                jatkaa = False
                continue
            valaistuskartta[rivi][sarake].append(suunta)
            merkki = kartta[rivi][sarake]
            # PEILIT
            if merkki == "/":
                rivi, sarake, suunta = the_slash_mirror(rivi, sarake, suunta, True)
            elif merkki == "\\":
                rivi, sarake, suunta = the_slash_mirror(rivi, sarake, suunta, False)
            # JAKAJAT JAKAESSAAN
            elif (merkki == "|" and suunta % 2 == 0) or (merkki == "-" and suunta % 2 == 1):
                if suunta % 2 == 0:
                    rivi, sarake, suunta = rivi - 1, sarake, 1
                    pino.append((rivi + 1, sarake, 3))
                elif suunta % 2 == 1:
                    rivi, sarake, suunta = rivi, sarake + 1, 2
                    pino.append((rivi, sarake - 1, 4))
                # handle jakaja
            # KAIKKI MUU
            else:
                if suunta == 1:
                    rivi, sarake = rivi - 1, sarake
                elif suunta == 2:
                    rivi, sarake = rivi, sarake + 1
                elif suunta == 3:
                    rivi, sarake = rivi + 1, sarake
                elif suunta == 4:
                    rivi, sarake = rivi, sarake - 1
    score = 0
    for rivi in valaistuskartta:
        # uusi_rivi = []
        for lista in rivi:
            if lista:
                # uusi_rivi.append("#")
                score += 1
            # else:
            #     uusi_rivi.append(".")
        # print("".join(uusi_rivi))
    return score


def part_one(filename):
    kartta = [line for line in blockify(filename) if line]
    print(beam_on_you_brute(kartta, 0, 0, 2))


def anna_reunatiilet_ja_suunnat(kartta):
    palautettava = []
    korkeus = len(kartta)
    leveys = len(kartta[0])
    palautettava += [(0, x, 3) for x in range(leveys)]
    palautettava += [(korkeus - 1, x, 1) for x in range(leveys)]
    palautettava += [(y, 0, 2) for y in range(korkeus)]
    palautettava += [(y, leveys - 1, 4) for y in range(korkeus)]
    return palautettava


def part_two(filename):
    kartta = [line for line in blockify(filename) if line]
    reunatiilet_ja_suunnat = anna_reunatiilet_ja_suunnat(kartta)
    palautusarvot = []
    for tupletti in reunatiilet_ja_suunnat:
        # print(tupletti)
        palautusarvot.append(beam_on_you_brute(kartta, *tupletti))
    print(sorted(palautusarvot)[-1])


if __name__ == "__main__":
    # part_one("16-test-input-1.txt")
    # part_one("16-input.txt")
    part_two("16-test-input-1.txt")
    part_two("16-input.txt")
# suunnat
#    1
#  4   2    \
#    3
