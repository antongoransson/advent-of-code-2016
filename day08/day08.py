import regex as re
from collections import deque


def part1(instructions):
    grid = [deque(['.'] * 50) for i in range(6)]
    for instruction in instructions:
        y = instruction['y']
        x = instruction['x']
        if instruction['name'] == 'rect':
            for i in range(y):
                for j in range(x):
                    grid[i][j] = '#'
        else:
            dist = instruction['dist']
            if instruction['name'] == 'rotate_row':
                grid[y].rotate(dist)
            elif instruction['name'] == 'rotate_col':
                for _ in range(dist):
                    prev = grid[-1][x]
                    for i, row in enumerate(grid):
                        curr = row[x]
                        row[x] = prev
                        prev = curr
    tot = 0
    for row in grid:
        tot += row.count('#')
    return tot, grid


def part2(grid):
    s = ''
    for row in grid:
        s += ''.join(row) + '\n'
    return s


def main():
    instructions = []
    with open('input.txt') as f:
        for line in f:
            l = line.strip()
            if 'rect' in l:
                x, y = map(int, re.findall(r'-?\d+', l))
                instructions.append({'name': 'rect', 'y': y, 'x': x})
            else:
                dist = int(re.findall(r'by (\d+)', l)[0])
                if 'y=' in l:
                    x = 0
                    y = int(re.findall(r'y=(\d+)', l)[0])
                    name = 'rotate_row'
                else:
                    y = 0
                    x = int(re.findall(r'x=(\d+)', l)[0])
                    name = 'rotate_col'
                instructions.append(
                    {'name': name, 'y': y, 'x': x, 'dist': dist})
    p1, grid = part1(instructions)
    print(f'Part 1: {p1}')
    p2 = part2(grid)
    print(f'Part 2: \n{p2}')


if __name__ == "__main__":
    main()
