
from collections import defaultdict
import regex as re


def get_val(x, registers):
    if x in registers:
        return int(registers[x])
    else:
        return int(x)


def solve(instructions, registers):
    ip = 0
    while ip < len(instructions):
        i = instructions[ip].split()
        code = i[0]
        ip += 1
        if code == 'cpy':
            _, x, y = i
            registers[y] = get_val(x, registers)
        elif code == 'inc':
            _, x = i
            registers[x] += 1
        elif code == 'dec':
            _, x = i
            registers[x] -= 1
        elif code == 'jnz':
            _, x, y = i
            if get_val(x, registers) != 0:
                ip += int(y) - 1
    return registers['a']


def part1(instructions):
    registers = {c: 0 for c in "abcd"}
    return solve(instructions, registers)


def part2(instructions):
    registers = {c: 0 for c in "abcd"}
    registers['c'] = 1
    return solve(instructions, registers)


def main():
    with open('input.txt') as f:
        instructions = [line.strip() for line in f]
        p1 = part1(instructions)
        print(f'Part 1: {p1}')
        p2 = part2(instructions)
        print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
