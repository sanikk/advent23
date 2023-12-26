from enum import Enum


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


def ensi_askel(location, blocks):
    rivi, sarake = location
    if rivi > 0 and blocks[rivi - 1][sarake] in "F|7":
        return rivi - 1, sarake
    elif rivi < len(blocks) and blocks[rivi + 1][sarake] in "L|J":
        return rivi + 1, sarake
    elif sarake > 0 and blocks[rivi][sarake - 1] in "7-J":
        return rivi, sarake - 1
    elif sarake < len(blocks[0]) - 1 and blocks[rivi][sarake + 1] in "L-F":
        return rivi, sarake + 1
    else:
        print(f"{rivi=}, {sarake=}")
    return None


def seuraa_putkea(sijainti, blocks, eka, vika):
    rivi, sarake = sijainti
    map_symbols = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}
    nykyinen = blocks[sijainti[0]][sijainti[1]]
    suunnat = map_symbols[nykyinen]
    for suunta in suunnat:
        tutkailtava = (rivi - 1, sarake)
        if suunta == "N" and (tutkailtava != vika or tutkailtava == eka):
            return rivi - 1, sarake
        tutkailtava = (rivi + 1, sarake)
        if suunta == "S" and (tutkailtava != vika or tutkailtava == eka):
            return tutkailtava
        tutkailtava = (rivi, sarake - 1)
        if suunta == "W" and (tutkailtava != vika or tutkailtava == eka):
            return rivi, sarake - 1
        tutkailtava = (rivi, sarake + 1)
        if suunta == "E" and (tutkailtava != vika or tutkailtava == eka):
            return rivi, sarake + 1


def actually_follow(start, blocks):
    sijainti = ensi_askel(start, blocks)
    reitti = [start]
    while sijainti != start:
        reitti.append(sijainti)
        # eka mukaan vaan jos reittiä on tarpeeks
        if len(reitti) > 2:
            sijainti = seuraa_putkea(sijainti, blocks,reitti[0], reitti[-2])
        else:
            sijainti = seuraa_putkea(sijainti, blocks, None, reitti[-2])
    return [(sijainti, blocks[sijainti[0]][sijainti[1]]) for sijainti in reitti]


def part_one(filename):
    blocks = blockify(filename)
    animal = find_animal(blocks)
    reitti = actually_follow(animal, blocks)
    tulos = int(len(reitti) / 2)
    print(f"{tulos=}")

def etsi_torit(reitti, blocks):
    map_symbols = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}
    sijainti = reitti[0]
    while sijainti != reitti[-1]:
        rivi, sarake = sijainti
        nykyinen = blocks[sijainti[0]][sijainti[1]]
        suunnat = map_symbols[nykyinen]
        if "N" not in suunnat and blocks[sijainti[0] - 1][sijainti[1]] == ".":
            pass
        tutkailtava = (rivi - 1, sarake)

        tutkailtava = (rivi + 1, sarake)


        tutkailtava = (rivi, sarake - 1)


        tutkailtava = (rivi, sarake + 1)

def piirra_kartta(reitti, blocks):
    pienin_x = min([x[0][1] for x in reitti])

    isoin_x = max([x[0][1] for x in reitti])
    pienin_y = min([x[0][0] for x in reitti])
    isoin_y = max([x[0][0] for x in reitti])
    print(f"{pienin_y=}, {isoin_y=}")
    kartta = blocks[pienin_y:isoin_y + 1]
    kartta = [rivi[pienin_x:isoin_x+1] for rivi in kartta]
    with open("output.txt", 'w') as f:
        for rivi in kartta:
            print(rivi)
            f.write(rivi+"\n")

def part_two(filename):
    blocks = blockify(filename)
    animal = find_animal(blocks)
    reitti = actually_follow(animal, blocks)
    piirra_kartta(reitti, blocks)

if __name__ == "__main__":
    # part_one("10-test-input1.txt")
    # part_one("10-test-input2.txt")
    # part_one("10-test-input3.txt")
    # part_one("10-test-input4.txt")
    # part_one("10-input.txt")
    part_two("10-test-input-5.txt")
# map_symbols = {"|": "N-S", "-": "E-W", "L": "N-E", "J": "N-W", "7": "S-W", "F": "S-E"}
# .     No pipe
# S     Animal starts here
