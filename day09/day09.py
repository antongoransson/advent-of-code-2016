
from collections import deque
import regex as re


def part1(seq):
    stack = deque(seq)
    l = 0
    while stack:
        c = stack.popleft()
        if c == '(':
            stack_str = ''.join(stack)
            n_chars = int(re.search(r'(\d+)x', stack_str).group(1))
            n_times = int(re.search(r'x(\d+)\)', stack_str).group(1))
            while stack.popleft() != ')':
                pass
            stack_str = ''.join(stack)
            l += min(n_chars, len(stack_str)) * n_times
            for _ in range(n_chars):
                stack.popleft()

        else:
            l += 1
    return l



def part2(seq):
    stack = deque(seq)
    val = 0
    while stack:
        c = stack.popleft()
        if c == '(':
            n_char = ''
            x = stack.popleft()
            while x != 'x':
                n_char += x
                x = stack.popleft()
            x = stack.popleft()
            n_times = ''
            while x != ')':
                n_times += x
                x = stack.popleft()
            val += int(n_times) * part2(list(stack)[:int(n_char)])
            stack = deque(list(stack)[int(n_char):])
        else:
           val += 1
    return val

def main():
    with open('input.txt') as f:
        seq = f.readline()
    p1 = part1(seq)
    print(f'Part 1: {p1}')
    # seq = 'XABCABCABCABCABCABCY'
    # seq = '(3x3)XYZ'  # 9
    # seq = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'  # 445
    # seq = '(27x12)(20x12)(13x14)(7x10)(1x12)A'  # 241920
    p2 = part2(seq)
    print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
