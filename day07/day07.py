import regex as re


def abba(ip):
    for seq in ip:
        for i in range(0, len(seq) - 3):
            s1 = seq[i: i + 2]
            s2 = seq[i + 2: i + 4]
            if s1[::-1] == s2 and s1[0] != s1[1]:
                return True
    return False


def aba_bab(ip):
    string = ','.join(ip[1])
    for seq in ip[0]:
        for i in range(0, len(seq) - 2):
            c1, c2, c3 = seq[i: i + 3]
            if c1 == c3 and c1 != c2:
                bab_s = c2 + c1 + c2
                if bab_s in string:
                    return True
    return False


def part1(ip_addresses):
    return len([ip for ip in ip_addresses if abba(ip[0]) and not abba(ip[1])])


def part2(ip_addresses):
    return len([ip for ip in ip_addresses if aba_bab(ip)])


def main():
    ip_addresses = []
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            a = re.findall(r'\](\w+)', line)
            b = re.findall(r'(\w+)\[', line)
            hypernet_seq = re.findall(r'\[(\w+)\]', line)
            ip_addresses.append((a + b, hypernet_seq))
    p1 = part1(ip_addresses)
    print(f'Part 1: {p1}')
    p2 = part2(ip_addresses)
    print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
