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
    [1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,1],
    [1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1],
    [1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
start = (1,1)
goal = (11,18)

def print_maze(maze, flood, pos=None, discovered=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if discovered and not discovered[i][j]:
                char = '?'
            elif (i, j) == pos:
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
            yield (ni, nj)

def flood_fill(goal, discovered, known_maze):
    flood = [[float('inf') for _ in row] for row in known_maze]
    queue = []
    # Si el objetivo está descubierto y es camino libre, inicializa el flood
    if discovered[goal[0]][goal[1]] and known_maze[goal[0]][goal[1]] == 0:
        flood[goal[0]][goal[1]] = 0
        queue.append(goal)
    else:
        # Si no, inicializa flood en todas las celdas libres descubiertas
        for i in range(len(known_maze)):
            for j in range(len(known_maze[0])):
                if discovered[i][j] and known_maze[i][j] == 0:
                    flood[i][j] = 0
                    queue.append((i, j))
    while queue:
        i, j = queue.pop(0)
        for ni, nj in neighbors((i, j)):
            if discovered[ni][nj] and known_maze[ni][nj] == 0:
                if flood[ni][nj] > flood[i][j] + 1:
                    flood[ni][nj] = flood[i][j] + 1
                    queue.append((ni, nj))
    return flood

def solve_maze_exploring():
    discovered = [[False for _ in row] for row in maze]
    known_maze = [[1 for _ in row] for row in maze]
    pos = start
    discovered[pos[0]][pos[1]] = True
    known_maze[pos[0]][pos[1]] = 0
    moves = 0
    path = [pos]
    visited = set()
    visited.add(pos)

    while pos != goal:
        # Descubre vecinos
        for ni, nj in neighbors(pos):
            discovered[ni][nj] = True
            known_maze[ni][nj] = maze[ni][nj]
        flood = flood_fill(goal, discovered, known_maze)
        print_maze(maze, flood, pos, discovered)
        print(f"Movimientos realizados: {moves}")
        time.sleep(0.7)
        # Si el objetivo es alcanzable, ir hacia él
        if flood[goal[0]][goal[1]] != float('inf'):
            min_val = float('inf')
            next_pos = None
            for n in neighbors(pos):
                if discovered[n[0]][n[1]] and known_maze[n[0]][n[1]] == 0:
                    if flood[n[0]][n[1]] < min_val:
                        min_val = flood[n[0]][n[1]]
                        next_pos = n
            if next_pos is not None:
                path.append(next_pos)
        else:
            # Explorar: prioriza vecinos no visitados
            min_dist = float('inf')
            next_pos = None
            for n in neighbors(pos):
                if discovered[n[0]][n[1]] and known_maze[n[0]][n[1]] == 0 and n not in visited:
                    dist = abs(n[0] - goal[0]) + abs(n[1] - goal[1])
                    if dist < min_dist:
                        min_dist = dist
                        next_pos = n
            # Si todos los vecinos ya fueron visitados, retrocede en el path
            if next_pos is None and len(path) > 1:
                next_pos = path[-2]
                path.pop()
            elif next_pos is not None:
                path.append(next_pos)
        if next_pos is None:
            print("No hay camino al objetivo con lo descubierto.")
            return
        pos = next_pos
        visited.add(pos)
        moves += 1
    print_maze(maze, flood, pos, discovered)
    print(f"¡Laberinto resuelto en {moves} movimientos!")
    print("Ruta:", path)

if __name__ == "__main__":
    solve_maze_exploring()