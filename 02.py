RED = 12
GREEN = 13
BLUE = 14

def kasittele_tulokset(input:str):
    for era in input.split(";"):
        red,green,blue = laske_era(era)
        if red > RED or green > GREEN or blue > BLUE:
            return False
    return True


def kasittele_tulokset_minimit(input:str):
    reds = 0
    greens = 0
    blues = 0
    for era in input.split(";"):
        red,green,blue = laske_era(era)
        reds = max(reds, red)
        greens = max(greens, green)
        blues = max(blues, blue)
    return reds * greens * blues


def laske_era(syote):
    red = 0
    green = 0
    blue = 0
    for pallot in syote.split(","):
        palat = pallot.strip().split()
        if palat[1] == "red":
            red = int(palat[0])
        elif palat[1] == "green":
            green = int(palat[0])
        elif palat[1] == "blue":
            blue = int(palat[0])
    return red, green, blue


def part_one(input_file):
    vastaus = 0
    with open(input_file) as tiedosto:
        for line in tiedosto:
            peli, tulokset = line.split(":")
            if kasittele_tulokset(tulokset):
                vastaus += int(peli.split(" ")[1])
    print(f"{vastaus=}")


def part_two(input_file):
    vastaus = 0
    with open(input_file) as tiedosto:
        for line in tiedosto:
            peli, tulokset = line.split(":")
            vastaus += kasittele_tulokset_minimit(tulokset)
    print(f"{vastaus=}")


# part_two("02-test-input.txt")
part_two("02-input.txt")