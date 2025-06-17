import matplotlib.pyplot as plt
import numpy as np

from test_maze import maze


def grap_path_taken(maze, path):
    maze_array = np.array(maze)
    color_maze = np.ones((len(maze), len(maze[0]), 3))
    color_maze[maze_array == 1] = [0, 0, 0]

    for r, c in path:
        color_maze[r, c] = [0, 0, 1]

    color_maze[path[0]] = [0, 1, 0]
    color_maze[path[-1]] = [1, 0, 0]

    plt.figure(figsize=(10, 6))
    plt.imshow(color_maze)
    plt.title("Maze Path with Arrows")
    plt.axis('off')

    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]
        dr, dc = r2 - r1, c2 - c1
        plt.arrow(
            c1, r1, dc * 0.6, dr * 0.6,
            head_width=0.3, head_length=0.3, fc='yellow', ec='yellow'
        )

    plt.tight_layout()
    plt.show()

def graph_maze(maze):
    maze_array = np.array(maze)
    maze_image = np.ones((len(maze), len(maze[0]), 3))
    maze_image[maze_array == 1] = [0, 0, 0]

    plt.figure(figsize=(10, 6))
    plt.imshow(maze_image)
    plt.title("Maze (No Path)")
    plt.axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    graph_maze(maze)
