
### 2. `main.py`

```python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def topological_sort_util(v, visited, stack, adj):
    visited[v] = True
    for i in adj[v]:
        if not visited[i[0]]:
            topological_sort_util(i[0], visited, stack, adj)
    stack.append(v)

def longest_path(graph: list, source: int) -> int:
    V = len(graph)
    adj = [[] for _ in range(V)]
    
    for u in range(V):
        for v, weight in graph[u]:
            adj[u].append([v, weight])
    
    stack = []
    visited = [False] * V
    dist = [-10**9] * V

    for i in range(V):
        if not visited[i]:
            topological_sort_util(i, visited, stack, adj)
    
    dist[source] = 0

    while stack:
        u = stack.pop()
        if dist[u] != -10**9:
            for i in adj[u]:
                if dist[i[0]] < dist[u] + i[1]:
                    dist[i[0]] = dist[u] + i[1]

    max_dist = max(dist)
    return max_dist

