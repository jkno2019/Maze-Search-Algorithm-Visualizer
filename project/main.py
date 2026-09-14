import numpy as np
import matplotlib.pyplot as plt
import heapq

# Generate a random maze and set wall probability
def generate_maze(wall_prob=0.2):
    # ALTER MAZE SIZE IF NEEDED <--------------------------------
    size = 25
    maze = np.zeros((size, size), dtype=int)

    # Randomly place walls (1 = wall, 0 = open)
    for i in range(size):
        for j in range(size):
            if (i, j) not in [(0, 0), (size - 1, size - 1)]:
                if np.random.rand() < wall_prob:
                    maze[i][j] = 1
    return maze


def get_neighbors(pos, maze):
    x, y = pos
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and maze[nx, ny] == 0:
            neighbors.append((nx, ny))
    return neighbors


def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


from collections import deque

def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        for nx, ny in get_neighbors((x, y), maze):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return None


def greedy_best_first(maze, start, goal):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start, [start]))
    visited = set()

    while pq:
        _, current, path = heapq.heappop(pq)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic(neighbor, goal), neighbor, path + [neighbor]))
    return None


def astar(maze, start, goal):
    pq = []
    heapq.heappush(pq, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current, maze):
            new_g = g + 1
            new_f = new_g + heuristic(neighbor, goal)
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    return None


def plot_maze(maze, start, goal, paths):
    plt.imshow(maze, cmap='binary')
    plt.scatter(start[1], start[0], marker='o', color='green', s=200, label='Start')
    plt.scatter(goal[1], goal[0], marker='x', color='red', s=200, label='Goal')

    colors = {'BFS': 'blue', 'Greedy': 'orange', 'A*': 'purple'}
    for label, path in paths.items():
        if path:
            xs, ys = zip(*path)
            plt.plot(ys, xs, color=colors[label], label=f'{label} Path', linewidth=3, alpha=0.7)

    plt.legend()
    plt.title("Search Algorithm Visualization")
    plt.show()


if __name__ == "__main__":
    start = (0, 0)

    # CHANGE GOAL POSITION IF NEEDED BASED ON MAZE SIZE <----------------
    goal = (24, 24)

    maze = generate_maze(wall_prob=0.2)

    print("Generated Maze:")
    print(maze)

    bfs_path = bfs(maze, start, goal)
    greedy_path = greedy_best_first(maze, start, goal)
    astar_path = astar(maze, start, goal)

    print("\nBFS Path:", bfs_path)
    print("Greedy Path:", greedy_path)
    print("A* Path:", astar_path)

    paths = {'BFS': bfs_path, 'Greedy': greedy_path, 'A*': astar_path}
    plot_maze(maze, start, goal, paths)
