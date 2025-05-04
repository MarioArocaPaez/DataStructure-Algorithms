"""
You are given an undirected graph with n nodes labeled from 0 to n - 1 and a list of edges.
Write a function to determine if there exists any path from a start node to an end node using DFS.

Return True if such a path exists, otherwise return False
"""
n = 6
edges = [
    (0, 1), (0, 2),
    (1, 3),
    (2, 4),
    (4, 5)
]
start = 0
end = 5

def path_exists_dfs(n, edges, start, end):
    # Build the graph as adjacency list
    graph = {}
    for i in range(n):
        graph[i] = []
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        if node == end:
            return True
        
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
                
        return False
    
    return dfs(start)

print(path_exists_dfs(6, [(0,1), (0,2), (1,3), (2,4), (4,5)], 0, 5))  # Output: True

"""
You are given a 2D grid of 0s and 1s.
A region is formed by adjacent 1s connected horizontally or vertically (not diagonally).
Write a function to return the number of connected regions (groups of 1s) in the grid using DFS.
"""
grid = [
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1]
]

def count_regions(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def dfs(r, c):
        # Stop if out of bounds or not a 1 or already visited
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if (r, c) in visited or grid[r][c] == 0:
            return
        
        visited.add((r,c))

        # Explore neighbors
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                dfs(r,c)
                count += 1


print(count_regions(grid))  # Output: 3


"""
You are given an undirected graph with n nodes labeled from 0 to n - 1 and a list of edges.
Write a function to determine if the graph contains a cycle, using DFS.

A cycle occurs when a path leads back to a previously visited node that is not the parent of the current node.

Return True if there is a cycle, otherwise return False.
"""
n = 5
edges = [
    (0, 1),
    (1, 2),
    (2, 0),
    (3, 4)
]

def has_cycle(n, edges):
    graph = {}
    visited = set()
    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
                elif neighbor != parent:
                    # Found a back edge - cycle exists
                    return True
                
        return False
    
    # Check each component (in case the graph is disconnected)
    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
            
    return False

print(has_cycle(n, edges))  # Output: True

"""
You are given a directed graph with n nodes labeled from 0 to n - 1, and a list of directed edges.
Write a function to determine if it is possible to reach a target node from a given start node using DFS.
Return True if there is a path from start to target, otherwise return False.
"""
n = 5
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4)
]
start = 0
target = 4

def can_reach_target(n, edges, start, target):
    graph = {}
    visited = set()
    for i in range(n):
        graph[i] = []

    for u, v in edges:
        graph[u].append(v)

    def dfs(node):
        if node == target:
            return True
        visited.add(node)
        for e in graph[node]:
            if e not in visited:
                if dfs(e):
                    return True
                
        return False

    return dfs(start)

print(can_reach_target(n, edges, start, target))  





    

    
