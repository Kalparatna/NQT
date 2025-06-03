'''
Problem Statement
You are given a Directed Acyclic Graph (DAG) with N vertices and M edges. Each edge has a
weight associated with it. Your task is to find the shortest path from a given source node (SRC)
to a destination node (DES) using the provided graph data.
Input Format
1.N M — Two integers representing the number of vertices (N) and the number of edges (M).
X Y W — Three integers for each edge representing an edge from vertex X to vertex Y with
weight W.
2.
SRC DES — Two integers representing the source node (SRC) and the destination node
(DES).
3.
Output Format
Print the shortest path from SRC to DES.
Display the total weight of this path.
Example Input
3 3
0 1 5
1 2 3
0 2 10
0 2
Example Output
Path: 0 -> 1 -> 2, Total Weight: 8


'''
# Helper function to perform topological sort
def topological_sort(v, visited, stack, graph):
    visited[v] = True
    for neighbor, weight in graph[v]:
        if not visited[neighbor]:
            topological_sort(neighbor, visited, stack, graph)
    stack.append(v)

# Main function
def shortest_path_in_dag(N, M, edges, SRC, DES):
    # Step 1: Build graph
    graph = [[] for _ in range(N)]
    for u, v, w in edges:
        graph[u].append((v, w))

    # Step 2: Topological Sort
    visited = [False] * N
    stack = []
    for i in range(N):
        if not visited[i]:
            topological_sort(i, visited, stack, graph)

    # Step 3: Initialize distances
    dist = [float('inf')] * N
    dist[SRC] = 0
    parent = [-1] * N

    # Step 4: Relax edges in topological order
    while stack:
        u = stack.pop()
        if dist[u] != float('inf'):
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    parent[v] = u

    # Step 5: Reconstruct path
    path = []
    curr = DES
    if dist[DES] == float('inf'):
        print("No path exists")
        return
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    # Output
    print(" -> ".join(map(str, path)))
    print(dist[DES])

# Example usage:
N = 3
M = 3
edges = [
    (0, 1, 5),
    (1, 2, 3),
    (0, 2, 10)
]
SRC = 0
DES = 2

shortest_path_in_dag(N, M, edges, SRC, DES)
