import re


def get_digits(s):
    return re.findall(r'-?\d+', s)


def part1(triangles):
    n = 0
    for t in triangles:
        a, b, c = map(int, t)
        if a + b > c and a + c > b and b + c > a:
            n += 1
    return n


def part2(triangles):
    n = 0
    for i in range(0, len(triangles), 3):
        for j in range(0, 3):
            a, b, c = map(int, [triangles[i + k][j] for k in(range(0, 3))])
            if a + b > c and a + c > b and b + c > a:
                n += 1
    return n


def main():
    with open('input.txt') as f:
        triangles = [get_digits(line.strip()) for line in f]
    p1 = part1(triangles)
    print(f'Part 1: {p1}')
    p2 = part2(triangles)
    print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
