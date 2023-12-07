import collections


def is_five_of_a_kind(s):
    return all(c == s[0] for c in s)

def is_four_of_a_kind(s):
    ct = collections.Counter(s)
    occurences = sorted(ct.values())
    return occurences == [1, 4]

def is_full_house(s):
    ct = collections.Counter(s)
    occurences = sorted(ct.values())
    return occurences == [2, 3]

def is_three_of_a_kind(s):
    ct = collections.Counter(s)
    occurences = sorted(ct.values())
    return occurences == [1, 1, 3]

def is_two_pair(s):
    ct = collections.Counter(s)
    occurences = sorted(ct.values())
    return occurences == [1, 2, 2]

def is_one_pair(s):
    ct = collections.Counter(s)
    occurences = sorted(ct.values())
    return occurences == [1, 1, 1, 2]

def is_high_card(s):
    ct = collections.Counter(s)
    occurences = sorted(ct.values())
    return occurences == [1, 1, 1, 1, 1]

card_to_score = {
    "A": "M",
    "K": "L",
    "Q": "K",
    "J": "1",
    "T": "I",
    "9": "H",
    "8": "G",
    "7": "F",
    "6": "E",
    "5": "D",
    "4": "C",
    "3": "B",
    "2": "A",
}

def get_score(hand: str):
    return "".join(card_to_score[c] for c in hand)

def replace_joker(hand):
    ct = collections.Counter(hand)
    del ct["J"]
    if len(ct) == 0:
        return "AAAAA"
    most_common_card, _ = max(ct.items(), key=lambda x: x[1])
    return hand.replace("J", most_common_card)

def get_hand_key(hand):
    score = get_score(hand)
    if "J" in hand:
        hand = replace_joker(hand)
    if is_five_of_a_kind(hand):
        return 7, score
    if is_four_of_a_kind(hand):
        return 6, score
    if is_full_house(hand):
        return 5, score
    if is_three_of_a_kind(hand):
        return 4, score
    if is_two_pair(hand):
        return 3, score
    if is_one_pair(hand):
        return 2, score
    if is_high_card(hand):
        return 1, score
    raise Exception(f"Hand {hand} is not expected")

def part1():
    with open("advent_of_code/2023/day7/in_sample.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    hands_and_bids = []
    for line in lines:
        hand, bid = line.split()
        hands_and_bids.append((hand, int(bid)))
    hands_and_bids.sort(key=lambda x: get_hand_key(x[0]))
    return sum((i+1)*bid for i, (_, bid) in enumerate(hands_and_bids))


print(part1())


