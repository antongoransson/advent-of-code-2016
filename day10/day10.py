
from collections import defaultdict
import regex as re


def part1(instructions):
    bots = defaultdict(list)
    i = 0
    outputs = defaultdict(int)
    while instructions:
        line = instructions[i % len(instructions)]
        if line[0:3] == 'bot':
            l = line.split()
            bot = int(l[1])
            coins = bots[bot]
            if len(coins) != 2:
                i += 1 % len(instructions)
                continue
            if 61 in coins and 17 in coins:
                return bot
            low_is_bot = l[5] == 'bot'
            low_id = int(l[6])
            if low_is_bot:
                bots[low_id].append(min(coins))
            else:
                outputs[low_id] = (min(coins))
            high_is_bot = l[10] == 'bot'
            high_id = int(l[11])
            if high_is_bot:
                bots[high_id].append(max(coins))
            else:
                outputs[high_id] = (max(coins))
            bots[bot] = []
            instructions.remove(line)
        else:
            value, bot = map(int, re.findall(r'\d+', line))
            bots[bot].append(value)
            instructions.remove(line)
        i += 1 % len(instructions)


def part2(instructions):
    bots = defaultdict(list)
    i = 0
    outputs = defaultdict(int)
    while instructions:
        line = instructions[i % len(instructions)]
        if line[0:3] == 'bot':
            l = line.split()
            bot = int(l[1])
            coins = bots[bot]
            if len(coins) != 2:
                i += 1
                continue
            low_is_bot = l[5] == 'bot'
            low_id = int(l[6])
            if low_is_bot:
                bots[low_id].append(min(coins))
            else:
                outputs[low_id] = (min(coins))
            high_is_bot = l[10] == 'bot'
            high_id = int(l[11])
            if high_is_bot:
                bots[high_id].append(max(coins))
            else:
                outputs[high_id] = (max(coins))
            bots[bot] = []
            instructions.remove(line)
        else:
            value, bot = map(int, re.findall(r'\d+', line))
            bots[bot].append(value)
            instructions.remove(line)
        i += 1
    return outputs[0] * outputs[1] * outputs[2]


def main():
    with open('input.txt') as f:
        instructions = [line.strip() for line in f]
        p1 = part1(list(instructions))
        print(f'Part 1: {p1}')
        p2 = part2(instructions)
        print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
