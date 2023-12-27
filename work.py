def blockify(filename):
    with open(filename) as f:
        return f.read().split("\n")


def scan_stuff(kartta):
    galaxies = []
    empty_lines, empty_cols = [], []
    return galaxies, empty_lines, empty_cols
def expand_space(kartta):
    pass
    #if rivi on tyhja, lisaa uuteen toinen rivi, sarakkeille sama, ensin kartotetaan missä tyhjiä jne,
    # sitten tehdään uus, ja palautetaa se

def shortest_paths(galaxit:list):
    pass


def part_one(filename):
    blocks = blockify(filename)


def part_two(filename):
    blocks = blockify(filename)


if __name__ == "__main__":
    part_one("input.txt")
    part_two("input.txt")