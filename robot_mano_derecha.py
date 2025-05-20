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

# Direcciones: arriba, derecha, abajo, izquierda
DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

def print_maze(maze, pos):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if (i, j) == pos:
                print('R', end=' ')
            elif (i, j) == goal:
                print('G', end=' ')
            elif (i, j) == start:
                print('S', end=' ')
            elif val == 1:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print()
    print()

def right_hand_rule():
    pos = start
    dir_idx = 1  # Empieza mirando a la derecha
    moves = 0
    path = [pos]

    while pos != goal:
        print_maze(maze, pos)
        print(f"Movimientos realizados: {moves}")
        time.sleep(0.1)

        # Intenta girar a la derecha
        right_dir = (dir_idx + 1) % 4
        ni, nj = pos[0] + DIRS[right_dir][0], pos[1] + DIRS[right_dir][1]
        if maze[ni][nj] == 0:
            dir_idx = right_dir
            pos = (ni, nj)
        else:
            # Si no puede, intenta avanzar de frente
            ni, nj = pos[0] + DIRS[dir_idx][0], pos[1] + DIRS[dir_idx][1]
            if maze[ni][nj] == 0:
                pos = (ni, nj)
            else:
                # Si no puede, intenta girar a la izquierda
                left_dir = (dir_idx - 1) % 4
                ni, nj = pos[0] + DIRS[left_dir][0], pos[1] + DIRS[left_dir][1]
                if maze[ni][nj] == 0:
                    dir_idx = left_dir
                    pos = (ni, nj)
                else:
                    # Si no puede, gira atrás
                    dir_idx = (dir_idx + 2) % 4
                    pos = (pos[0] + DIRS[dir_idx][0], pos[1] + DIRS[dir_idx][1])
        path.append(pos)
        moves += 1

    print_maze(maze, pos)
    print(f"¡Laberinto resuelto en {moves} movimientos!")
    print("Ruta:", path)

if __name__ == "__main__":
    right_hand_rule()