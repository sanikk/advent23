def blockify(filename):
    all_blocks = []
    with open(filename) as tiedosto:
        block = []
        for rivi in tiedosto:
            rivi = rivi.strip()
            if rivi == "":
                all_blocks.append(block)
                block = []
            else:
                block.append(rivi)
    all_blocks.append(block)                
    return all_blocks


def prettify_my_block(block):
    block = [(int(x), int(y), int(z)) for x, y, z in [rivi.split() for rivi in block[1:]]]
    block = sorted(block, key=lambda x: x[1], reverse=True)
    return block


# def testeri(seed, filename) -> None:
#     data = []
#     with open(filename) as tiedosto:
#         for rivi in tiedosto:
#             data.append(rivi.strip())
#     print(f"{handle_otherwise(seed, data)}")

def evaluator(source, rule):
    ready = []
    rule_end = rule[1] + rule[2]
    source_end = sum(source)
    if rule_end - 1< source[0]:
        return (source_end - 1, 0), [source]
    if source[0] < rule[1]:
        if source_end - 1< rule[1]:
            return (source_end - 1, 0), [source]
        else:
            etaisyys = rule[1] - source[0]
            ready.append((source[0], etaisyys))
            source = (rule[1], source[1] - etaisyys)
    if source[1]:
        mista = source[0]
        mihin = min(source_end, rule_end)
        kaytetty_matka = mihin - mista
        kayttamaton_matka = source[1] - kaytetty_matka
        korjaus = rule[0] - rule[1]
        return (mihin, kayttamaton_matka), [(mista + korjaus, kaytetty_matka)] + ready
    return source, ready


def handle_block(seed, block):
    palautettava = []
    all_rules = prettify_my_block(block)
    source = seed.pop()
    rule = all_rules.pop()
    while seed or source[1]:
        if seed and not source[1]:
            source = seed.pop()
        rule_end = rule[1] + rule[2] - 1
        while all_rules and rule_end < source[0]:
            rule = all_rules.pop()
            rule_end = rule[1] + rule[2] - 1
        if not all_rules and rule[1] + rule[2] < source[0]:
            palautettava.append(source)
            source = (source[0], 0)
        else:
            source, handled = evaluator(source, rule)
            palautettava += handled

    return palautettava


def part_two(filename):
    blocks = blockify(filename)
    seeds = blocks[0][0].split()[1:]
    tilanne = sorted([(int(seeds[i]), int(seeds[i + 1])) for i in range(0, len(seeds), 2)], reverse=True)
    for block in blocks[1:]:
        print(str(tilanne))
        tilanne = sorted(handle_block(tilanne, block), reverse=True)
    print(str(tilanne))
    print(sorted(tilanne)[0])
    print(sorted(tilanne, reverse=True)[0])
    print(sorted(tilanne, key=lambda x: x[1])[0])
    print(sorted(tilanne, key=lambda x: x[1], reverse=True)[0])


# part_two("05-test-input.txt")
part_two("05-input.txt")


def jotain_luonnosta():
    k_alku, k_range = None, None
    r_maali, r_alku, r_range = None, None, None
    # mistä lähtien kuitataan
    mista = max(k_alku, r_alku)
    # mihin asti
    mihin = min(k_alku + k_range - 1, r_alku+r_range)
    # kuitattu matka
    kuitattu_matka = mihin - mista
    # jaannos matka
    jaannos_matka = k_range - kuitattu_matka
