import re
from collections import Counter
from string import ascii_lowercase


def part1(rooms):
    tot = 0
    for room in rooms:
        letters = room['letters'].replace('-', '')
        room_id = room['room_id']
        check_sum = room['check_sum']
        c = Counter(letters)
        min_val = c.most_common(5)[-1][1]
        vals = [k for k, v in c.items() if v == min_val]
        s = ''.join([k for k, v in c.items() if v > min_val])
        s += ''.join(sorted(vals)[:5 - len(s)])
        if sorted(s) == sorted(check_sum):
            tot += room_id
    return tot


def part2(rooms):
    for room in rooms:
        letters = list(room['letters'].replace('-', ' '))
        room_id = room['room_id']
        for i, c in enumerate(letters):
            if c is ' ':
                continue
            a_i = ascii_lowercase.index(c)
            letters[i] = ascii_lowercase[(
                a_i + room_id) % len(ascii_lowercase)]
        s = ''.join(letters)
        if 'object' in s:
            return room_id


def main():
    rooms = []
    with open('input.txt') as f:
        for line in f:
            l = line.strip()
            letters = re.search(r'([a-z]+)(-[a-z]+)*',
                                l).group()
            room_id = re.search(r'\d+', l).group()
            check_sum = l.split('[')[1][:-1]
            rooms.append(
                {'letters': letters, 'room_id': int(room_id), 'check_sum': check_sum})
    p1 = part1(rooms)
    print(f'Part 1: {p1}')
    p2 = part2(rooms)
    print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
