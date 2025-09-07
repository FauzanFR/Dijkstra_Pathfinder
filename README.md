# Dijkstra Pathfinder
A Python implementation of Dijkstra's algorithm with step-by-step visualization using NetworkX and Matplotlib.

## Overview
This project demonstrates Dijkstra's algorithm for finding the shortest path between two nodes in a graph. The implementation includes an animated visualization that shows each step of the algorithm's execution, making it easier to understand how the algorithm works.

# Features
- Interactive Input: Users can specify start and goal nodes
- Step-by-Step Animation: Visual representation of the algorithm's progress
- Color-Coded Nodes:
   - Light blue: Unvisited nodes
   - Green: Visited nodes
   - Orange: Currently processing node
- Path Highlighting: The current shortest path is shown in red
- Final Result Display: Shows the complete shortest path after algorithm completion

## Requirements
- Python 3.x
- NetworkX
- Matplotlib
- Heapq (included in Python standard library)

## Installation

1. Clone or download this repository
```bash
git clone https://github.com/FauzanFR/Dijkstra_Pathfinder
cd Dijkstra_Pathfinder
```

2. Install the required dependencies:
```bash
pip install networkx matplotlib
```

## Usage
Run the script:
```bash
python dijkstra_animation.py
```
When prompted, enter the start and goal nodes (e.g., "Oradea" and "Neamt" for the provided graph).

## Algorithm Explanation

Dijkstra's algorithm is a graph search algorithm that solves the single-source shortest path problem for a graph with non-negative edge weights. The algorithm works by:

1. Initializing all nodes with infinite distance except the start node (distance 0)
2. Using a priority queue to always process the node with the smallest known distance
3.For each node, updating the distances of its neighbors if a shorter path is found
4. Continuing until the goal node is reached or all nodes have been processed

## Code Structure
- Graph Setup: Creates a graph with 20 nodes and 23 edges with weights
- Dijkstra Implementation:
  - Uses a priority queue (heap) to select the next node to process
  - Maintains distance and previous node dictionaries
  - Includes animation at each step
- Visualization:
  - Draws the graph with NetworkX
  - Highlights nodes and edges based on their state
  - Shows the current step and distance information

## Customization
You can modify the graph by changing the `edges` list in the code:
```python
edges = [
("Oradea", "Zerind", 71),
("Zerind", "Arad", 75),
("Arad", "Sibiu", 140),
("Arad", "Timisoara", 118),
("Timisoara", "Lugoj", 111),
("Lugoj", "Mehadia", 70),
("Mehadia", "Dobreta", 75),
("Dobreta", "Craiova", 120),
("Craiova", "Rimnicu Vilcea", 146),
("Craiova", "Pitesti", 138),
("Sibiu", "Fagaras", 99),
("Sibiu", "Rimnicu Vilcea", 80),
("Rimnicu Vilcea", "Pitesti", 97),
("Fagaras", "Bucharest", 211),
("Pitesti", "Bucharest", 101),
("Bucharest", "Giurgiu", 90),
("Bucharest", "Urziceni", 85),
("Urziceni", "Hirsova", 98),
("Hirsova", "Eforie", 86),
("Urziceni", "Vaslui", 142),
("Vaslui", "Iasi", 92),
("Iasi", "Neamt", 87),
]
```
You can also adjust the animation speed by changing the `plt.pause()` value.

License
This project is open source and available under the MIT License.
