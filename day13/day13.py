from collections import deque
WALL = "#"
OPEN_SPACE = "."


def setup_grid(magic_number):
    size = 100
    grid = [[0 for i in range(size)] for j in range(size)]
    for y in range(size):
        for x in range(size):
            n = x*x + 3*x + 2*x*y + y + y*y
            n += magic_number
            if bin(n)[2:].count('1') % 2 == 0:
                grid[y][x] = OPEN_SPACE
            else:
                grid[y][x] = WALL
    return grid


def get_neighbours(grid):
    n = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pos = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            pos = [p for p in pos if p[0] >= 0 and p[1] >=
                   0 and p[0] < len(grid) and p[1] < len(grid[i])]
            n[i, j] = pos
    return n


def bfs(graph, grid, start, goal=None):
    found = False
    # keep track of explored nodes
    explored = {}
    # keep track of all the paths to be checked
    queue = deque([[start]])
    explored1 = {}
    # keeps looping until all possible paths have been checked
    while queue:
        if found:
            break
        path = queue.popleft()
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                if grid[neighbour[0]][neighbour[1]] is OPEN_SPACE:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if goal is not None and node == goal:
                        found = True
                explored[node] = len(path)
    return explored


def part1():
    grid = setup_grid(1358)
    graph = get_neighbours(grid)
    explored = bfs(graph, grid, (1, 1), (39, 31))
    return explored[(39, 31)] - 1


def part2():
    grid = setup_grid(1358)
    graph = get_neighbours(grid)
    explored = bfs(graph, grid, (1, 1))
    return len([p for p, steps in explored.items() if steps <= 51])


def main():
    p1 = part1()
    print(f'Part 1: {p1}')
    p2 = part2()
    print(f'Part 2: {p2}')


if __name__ == "__main__":
    main()
