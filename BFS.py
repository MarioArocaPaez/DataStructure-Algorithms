from collections import defaultdict
import heapq

"""
You are given an undirected graph representing a network of computers. Each node has a "priority" value. 
A virus starts from one node and spreads every minute to its directly connected, uninfected neighbors. 
If multiple neighbors can be infected at the same time, the virus always chooses the node with the lowest priority first. 
Return the total time it takes to infect all nodes, and the order in which they were infected.
"""

def virus_propagation(n, edges, priorities, start):
    # Build the graph as an adjacency list using a dictionary
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Set to keep track of which nodes have been infected
    infected = set()

    # List to record the order in which nodes are infected
    infection_order = [start]

    # Min-heap (priority queue) to choose the next node based on lowest priority
    min_heap = []
    for neighbor in graph[start]:
        heapq.heappush(min_heap, (priorities[neighbor], neighbor))

    # Counter for how many minutes it takes to infect all nodes
    time = 0

    # Performs BFS with priority-based selection
    while min_heap:
        current_batch = []

        # Extract all nodes at the current level from the heap
        while min_heap:
            prio, node = heapq.heappop(min_heap)
            if node not in infected:
                current_batch.append(node)

        # If we infected any new nodes in this round, increment time
        if current_batch:
            time += 1
            for node in current_batch:
                infected.add(node)
                infection_order.append(node)
                # Push all uninfected neighbors into the heap
                for neighbor in graph[node]:
                    if neighbor not in infected:
                        heapq.heappush(min_heap, (priorities[neighbor], neighbor))

    return time, infection_order

# Example usage:
n = 7
edges = [
    (0, 1), (0, 2), (1, 3), (2, 4),
    (4, 5), (3, 6)
]
priorities = [3, 1, 2, 4, 5, 1, 2]
start = 0

time_needed, order = virus_propagation(n, edges, priorities, start)
print("Time to infect all:", time_needed)
print("Infection order:", order)


"""
You are given an undirected unweighted graph as a list of edges and a number of nodes n. 
Write a function that finds the shortest distance (in number of edges) from a start node to a target node using BFS.
If there is no path between them, return -1.
"""
n = 6
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (4, 5)]

def shortest_path_bfs(n, edges, start, target):
    # Build the graph
    graph = {}
    for i in range(n):
        graph[i] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Standard BFS setup
    visited = set()
    queue = [[start]]  # queue of paths (each path is a list)

    while queue:
        path = queue.pop(0)      # take the first path
        node = path[-1]          # current node is the last in the path

        if node == target:
            return len(path) - 1  # number of edges is one less than number of nodes

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append(new_path)

    return -1  # no path found

print("Shortest path length:", shortest_path_bfs(n, edges, 0, 5))

"""
You are given a binary tree represented as an adjacency list (dictionary). Starting from the root node (value 0), use BFS to find the level (depth) at which a target node appears.
The root is at level 0, its children are at level 1, their children at level 2, and so on.
If the target node is not present in the tree, return -1.
"""
tree = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}
target = 5

def find_node_level(tree, target):
    visited = set()
    queue = [(0, 0)]    # (node, level)

    while queue:
        node, level = queue.pop(0)
        if node == target:
            return level
        
        if node not in visited:
            visited.add(node)
            for child in tree.get(node, []):
                if child not in visited:
                    queue.append((child, level + 1))

    return -1 # Not found
        

result = find_node_level(tree, target)
print(f"Target node {target} is at level {result}" if result != -1 else "Target not found.")


"""
You are given an unweighted directed graph with n nodes (labeled from 0 to n - 1) and a list of directed edges.
Write a function to return the minimum number of edges needed to reach the target node from the start node using BFS.
If the target is not reachable, return -1.
"""
n = 6
edges = [
    (0, 1), (0, 2),
    (1, 3),
    (2, 4),
    (4, 5)
]
start = 0
target = 5

def min_edges_bfs(n, edges, start, target):
    graph = {}
    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)

    visited = set()
    queue = [(start, 0)] # node, distance from start

    while queue:
        node, dist = queue.pop(0)
        if node == target:
            return dist
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))

    return -1

print(min_edges_bfs(n, edges, 0, 5))


"""
You are given a 2D grid consisting of 0s (empty cells) and 1s (walls).
You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1) in the minimum number of steps.
You can move up, down, left, or right, and you cannot walk through walls (1s).
Return the minimum number of steps required, or -1 if the target is unreachable.
"""
grid = [
    [0, 0, 1],
    [1, 0, 1],
    [1, 0, 0]
]

def min_steps_grid(grid):
    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return -1
    
    visited = set()
    queue = [(0,0,0)] # row, col, steps

    while queue:
        r, c, steps = queue.pop(0)
        if (r,c) == (rows - 1, cols - 1):
            return steps
        
        if (r,c) in visited:
            continue
        visited.add((r,c))

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                queue.append((nr, nc, steps + 1))

    return -1

print(min_steps_grid(grid))