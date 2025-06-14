import time
import os

# 0 = camino libre, 1 = pared
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1],
    [1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1],
    [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,1],
    [1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
start = (1,1)
goal = (11,18)

def print_maze(maze, flood, pos=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if (i, j) == pos:
                char = 'R'
            elif (i, j) == goal:
                char = 'G'
            elif (i, j) == start:
                char = 'S'
            elif val == 1:
                char = '#'
            else:
                cell = flood[i][j]
                char = '.' if cell == float('inf') else str(int(cell))
            print(char.center(3), end='')
        print()
    print()


def neighbors(pos):
    i, j = pos
    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]):
            if maze[ni][nj] == 0:
                yield (ni, nj)

def flood_fill(goal):
    flood = [[float('inf') for _ in row] for row in maze]
    queue = [goal]
    flood[goal[0]][goal[1]] = 0
    while queue:
        i, j = queue.pop(0)
        for ni, nj in neighbors((i, j)):
            if flood[ni][nj] > flood[i][j] + 1:
                flood[ni][nj] = flood[i][j] + 1
                queue.append((ni, nj))
    return flood

def solve_maze():
    flood = flood_fill(goal)
    pos = start
    path = [pos]
    moves = 0
    while pos != goal:
        print_maze(maze, flood, pos)
        print(f"Movimientos realizados: {moves}")
        time.sleep(0.5)
        min_val = float('inf')
        next_pos = None
        for n in neighbors(pos):
            if flood[n[0]][n[1]] < min_val:
                min_val = flood[n[0]][n[1]]
                next_pos = n
        if next_pos is None:
            print("No hay camino al objetivo.")
            return
        pos = next_pos
        path.append(pos)
        moves += 1
    print_maze(maze, flood, pos)
    print(f"¡Laberinto resuelto en {moves} movimientos!")
    print("Ruta:", path)

if __name__ == "__main__":
    solve_maze()
