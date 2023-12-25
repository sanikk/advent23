from operator import itemgetter, attrgetter, methodcaller


def read_file(filename):
    with open(filename) as f:
        return f.read().strip().split("\n")


def pretty_lines(lines):
    return [(type_hand(x), x, int(y)) for x, y in [x.split() for x in lines]]


def numerize_hand(hand):
    hand = [merkki for merkki in hand[1]]
    palautettava = 0
    i = 5
    for card in hand:
        if card == "T":
            card = 10
        if card == "J":
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


def sort_this_one(feed):
    return sorted(sorted(feed, key=lambda x: numerize_hand(x), reverse=True), key=itemgetter(0))


def type_hand(hand):
    card_counts = sorted([hand.count(x) for x in set(hand)], reverse=True)
    # jaa nää oli väärinpäin
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


def sort_this_one_for_part_two(feed):
    return sorted(sorted(feed, key=lambda x: numerize_hand(x), reverse=True), key=itemgetter(0))


def type_hand_for_part_two(hand):
    card_counts = sorted([hand.count(x) for x in set(hand)], reverse=True)
    # jaa nää oli väärinpäin
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
    blocks = read_file(filename)


if __name__ == "__main__":
    part_one("07-test-input.txt")
    part_one("07-input.txt")
    # part_two("input.txt")
