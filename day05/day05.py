import hashlib


def part1(code):
    h = hashlib.md5(code.encode('utf-8'))
    i = 0
    password = ''
    while len(password) < 8:
        while h.hexdigest()[:5] != '00000':
            h = hashlib.md5((code + str(i)).encode('utf-8'))
            i += 1
        password += h.hexdigest()[5]
        h = hashlib.md5(('abc' + str(i)).encode('utf-8'))
        i += 1
    return password


def part2(code):
    h = hashlib.md5(code.encode('utf-8'))
    i = 0
    password = [''] * 8
    while not all(password):
        while h.hexdigest()[:5] != '00000':
            h = hashlib.md5((code + str(i)).encode('utf-8'))
            i += 1
        k = h.hexdigest()[5]
        try:
            k = int(k)
        except ValueError:
            k = 100
        if k < 8 and not password[k]:
            password[k] = h.hexdigest()[6]
        h = hashlib.md5(('abc' + str(i)).encode('utf-8'))
        i += 1
    return ''.join(password)


def main():
    with open('input.txt') as f:
        code = f.readline().strip()
    p1 = part1(code)
    print(f'Part 1: {p1}')
    p2 = part2(code)
    print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
