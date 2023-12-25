from operator import itemgetter, attrgetter, methodcaller


def read_file(filename):
    with open(filename) as f:
        return f.read().strip().split("\n")


def pretty_lines(lines, parttwo=False):
    if parttwo:
        return [(type_hand_for_part_two(x), x, int(y)) for x, y in [x.split() for x in lines]]
    return [(type_hand(x), x, int(y)) for x, y in [x.split() for x in lines]]


def numerize_hand(hand, parttwo=False):
    hand = [merkki for merkki in hand[1]]
    palautettava = 0
    i = 5
    for card in hand:
        if card == "T":
            card = 10
        if card == "J":
            if parttwo:
                card = 1
            else:
                card = 11
        elif card == "Q":
            card = 12
        elif card == "K":
            card = 13
        elif card == "A":
            card = 14
        else:
            card = int(card)
        palautettava += 15**i * card
        i -= 1
    return palautettava


def sort_this_one(feed, parttwo=False):
    return sorted(sorted(feed, key=lambda x: numerize_hand(x, parttwo), reverse=True), key=itemgetter(0))


def type_hand(hand):
    card_counts = sorted([hand.count(x) for x in set(hand)], reverse=True)
    if card_counts[0] == 5:
        hand_type = 1
    elif card_counts[0] == 4:
        hand_type = 2
    elif card_counts[0] == 3 and card_counts[1] == 2:
        hand_type = 3
    elif card_counts[0] == 3:
        hand_type = 4
    elif card_counts[0] == 2 and card_counts[1] == 2:
        hand_type = 5
    elif card_counts[0] == 2:
        hand_type = 6
    else:
        hand_type = 7
    return hand_type


def type_hand_for_part_two(hand):
    card_counts = sorted([(hand.count(x), x) for x in set(hand)], reverse=True)
    jokerit = hand.count("J")
    if card_counts[0][1] == "J":
        if jokerit == 5:
            return 1
        card_counts = card_counts[1:]
    elif card_counts[1][1] == "J":
        card_counts = [card_counts[0]] + card_counts[2:]
    if card_counts[0][0] + jokerit == 5:
        hand_type = 1
    elif card_counts[0][0] + jokerit == 4:
        hand_type = 2
    elif card_counts[0][0] + jokerit == 3 and card_counts[1][0] == 2:
        hand_type = 3
    elif card_counts[0][0] == 3 and card_counts[1][0] + jokerit == 2:
        hand_type = 3
    elif jokerit == 2 and card_counts[0][0] + 1 == 3 and card_counts[1][0] + 1 == 2:
        hand_type = 3
    elif jokerit == 3 and card_counts[0][0] + 2 == 3 and card_counts[1][0] + 1 == 2:
        hand_type = 3
    elif card_counts[0][0] + jokerit == 3:
        hand_type = 4
    elif card_counts[0][0] == 2 and card_counts[1][0] + jokerit == 2:
        hand_type = 5
    elif jokerit == 2 and card_counts[0][0] + 1 == 2 and card_counts[1][0] + 1 == 2:
        hand_type = 5
    elif card_counts[0][0] + jokerit == 2:
        hand_type = 6
    else:
        hand_type = 7
    return hand_type


def part_one(filename):
    tulos = 0
    rounds = pretty_lines(read_file(filename))
    rounds = sort_this_one(rounds)
    rank = len(rounds)
    # print(f"Total Ranks: {rank}")
    for rundi in rounds:
        tulos += rank * rundi[2]
        rank -= 1
    print(f"{tulos=}")


def part_two(filename):
    tulos = 0
    blocks = read_file(filename)
    rounds = pretty_lines(blocks, parttwo=True)
    rounds = sort_this_one(rounds, parttwo=True)
    rank = len(rounds)
    # print(f"Total Ranks: {rank}")
    for rundi in rounds:
        tulos += rank * rundi[2]
        rank -= 1
    print(f"{tulos=}")


if __name__ == "__main__":
    # part_one("07-test-input.txt")
    # part_one("07-input.txt")
    part_two("07-test-input.txt")
    part_two("07-input.txt")