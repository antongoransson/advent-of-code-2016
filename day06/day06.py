from collections import defaultdict, Counter


def part1(messages):
    d = defaultdict(Counter)
    for m in messages:
        for i, c in enumerate(m):
            d[i][c] += 1
    return ''.join([d[i].most_common()[0][0] for i in range(len(messages[0]))])


def part2(messages):
    d = defaultdict(Counter)
    for m in messages:
        for i, c in enumerate(m):
            d[i][c] += 1
    return ''.join([d[i].most_common()[-1][0] for i in range(len(messages[0]))])


def main():
    with open('input.txt') as f:
        messages = [line.strip() for line in f]
    p1 = part1(messages)
    print(f'Part 1: {p1}')
    p2 = part2(messages)
    print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
