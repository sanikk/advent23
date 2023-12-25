from enum import Enum


def part_one_worker(syote):
    tulos = 0
    for line in syote:
        eka = ""
        vika = ""
        for merkki in line:
            if merkki.isnumeric():
                eka = int(merkki)
                break
        for merkki in reversed(line):
            if merkki.isnumeric():
                vika = int(merkki)
                break
        tulos += 10 * eka + vika
    return tulos


def part_one():
    # with open("01-test-input.txt") as tiedosto:
    with open("01-input.txt") as tiedosto:
        print(part_one_worker(tiedosto))


SANAT = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]
WORDS = Enum('words', SANAT)


def part_two_worker(syote):
    tulos = 0
    for line in syote:
        line = line.strip()
        eka = None
        vika = None
        i = 0
        while not eka and i < len(line):
            if line[i].isnumeric():
                eka = 10 * int(line[i])
            else:
                for sana in SANAT:
                    if line[i:].startswith(sana):
                        eka = 10 * WORDS[sana].value
            i += 1
        i = len(line) - 1
        while not vika and i >= 0:
            if line[i].isnumeric():
                vika = int(line[i])
            else:
                for sana in SANAT:
                    if line[:i+1].endswith(sana):
                        vika = WORDS[sana].value
            i -= 1
        value = eka + vika
        tulos += value
    return tulos


def part_two():
    with open("01-input.txt") as tiedosto:
        print(part_two_worker(tiedosto))

part_two()
