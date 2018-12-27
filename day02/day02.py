dirs = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}


def part1(instructions):
    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    pos = (1, 1)
    code = ''
    for i in instructions:
        for c in i:
            x = min(max(0, pos[0] + dirs[c][0]), 2)
            y = min(max(0, pos[1] + dirs[c][1]), 2)
            pos = (x, y)
        code += keypad[pos[0]][pos[1]]
    return code


def part2(instructions):
    keypad = [[None, None, '1', None, None], [
        None, '2', '3', '4', None], ['5', '6', '7', '8', '9'], [None, 'A', 'B', 'C', None], [None, None, 'D', None, None]]
    pos = (2, 0)
    code = ''
    for i in instructions:
        for c in i:
            x = min(max(0, pos[0] + dirs[c][0]), 4)
            y = min(max(0, pos[1] + dirs[c][1]), 4)
            if keypad[x][y]:
                pos = (x, y)
        code += keypad[pos[0]][pos[1]]
    return code


def main():
    with open('input.txt') as f:
        instructions = [line.strip() for line in f]
    p1 = part1(instructions)
    print(f'Part 1: {p1}')
    p2 = part2(instructions)
    print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
