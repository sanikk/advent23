def blockify(filename):
    with open(filename) as f:
        return f.read()


def kasittele_patka(patka: str):
    current = 0
    for merkki in patka:
        current += ord(merkki)
        current *= 17
        current = current % 256
    return current


def part_one(filename):
    blocks = blockify(filename).strip('\n')
    patkat = blocks.split(',')
    print(sum(kasittele_patka(patka) for patka in patkat))
    print(blocks.find('\n'))
    # hngh newline tosiaa


def count_score(boxes: dict):
    vastaus = 0
    for i in range(256):
        boxi = boxes.get(i, [])
        multiplier = i + 1
        for slot, lense in enumerate(boxi):
            arvo = multiplier * (slot + 1) * int(lense.split(" ")[1])
            # print(f"lense {lense.split(' ')[0]} in box {i}: {arvo=}")
            vastaus += arvo
    return vastaus


def part_two(filename):
    blocks = blockify(filename).strip('\n')
    patkat = blocks.split(',')
    boxes = {}
    for patka in patkat:
        label = ""
        operation_is_minus = False
        rest = ""
        if patka.endswith('-'):
            operation_is_minus = True
            label = patka[:-1]
        elif '=' in patka:
            operation_is_minus = False
            label, rest = patka.split('=')
        which_box = kasittele_patka(label)
        boxi = boxes.get(which_box, [])
        if operation_is_minus:
            for i, lense in enumerate(boxi):
                if lense.startswith(label):
                    boxi.remove(lense)
                    break
        else:
            teksti = f"{label} {int(rest)}"
            for i, lense in enumerate(boxi):
                if lense.startswith(label):
                    boxi[i] = teksti
                    break
            else:
                boxi.append(teksti)
        boxes[which_box] = boxi
    print(count_score(boxes))


if __name__ == "__main__":
    # part_one("15-test-input-1.txt")
    # part_one("15-input.txt")
    part_two("15-test-input-1.txt")
    part_two("15-input.txt")
