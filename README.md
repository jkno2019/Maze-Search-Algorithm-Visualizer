# Maze Search Algorithm Visualizer

A Python-based maze-solving program that generates random mazes and compares three search algorithms: Breadth-First Search (BFS), Greedy Best-First Search (GBFS), and A* Search**.

The program visualizes the resulting paths using Matplotlib, making it easy to compare how different search strategies navigate the same maze.

## Features

- Generates random **25×25 mazes**
- Configurable wall probability
- Supports three search algorithms:
  - Breadth-First Search (BFS)
  - Greedy Best-First Search (GBFS)
  - A* Search
- Uses **Manhattan distance** as the heuristic for GBFS and A*
- Displays the generated maze and calculated paths
- Prints the maze and paths to the console
- Visually compares the paths produced by each algorithm

## Technologies

- **Python 3**
- **NumPy** — maze representation and numerical operations
- **Matplotlib** — maze and path visualization
- **heapq** — priority queues for GBFS and A*
- **collections.deque** — queue implementation for BFS

## How It Works

### 1. Maze Generation

The program creates a 25×25 grid using NumPy.

Each cell is randomly assigned as either:

- `0` — Open space
- `1` — Wall

The default wall probability is `20%`.

The starting position is:

(0, 0)

The goal position is:

(24, 24)
