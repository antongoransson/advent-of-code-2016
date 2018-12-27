dirs = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}


def dist(p, q):
    return sum([abs(x - y) for x, y in zip(p, q)])


def part1(instructions):
    d = 0
    pos = (0, 0)
    for i in instructions:
        c, *steps = i
        steps = int(''.join(steps))
        if c == 'R':
            d = (d + 1) % 4
        elif c == 'L':
            d = (d - 1) % 4
        pos = (pos[0] + dirs[d][0] * steps, pos[1] + dirs[d][1] * steps)
    return dist(pos, (0, 0))


def part2(instructions):
    visited = set()
    d = 0
    pos = (0, 0)
    for i in instructions:
        c, *steps = i
        steps = int(''.join(steps))
        if c == 'R':
            d = (d + 1) % 4
        elif c == 'L':
            d = (d - 1) % 4
        for _ in range(steps):
            pos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
            if pos in visited:
                return dist(pos, (0, 0))
            visited.add(pos)


def main():
    with open('input.txt') as f:
        instructions = f.readline().split(', ')
    p1 = part1(instructions)
    print(f'Part 1: {p1}')
    p2 = part2(instructions)
    print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
