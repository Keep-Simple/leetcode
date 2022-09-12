"""Python3 program to print DFS traversal for complete graph"""
from collections import defaultdict

# this class represents a directed graph using adjacency list representation


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        return self

    def dfs_util(self, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self):
        # create a set to store all visited vertices
        visited = set()
        # call the recursive helper function to print DFS traversal starting from all
        # vertices one by one
        for vertex in self.graph:
            if vertex not in visited:
                self.dfs_util(vertex, visited)

    def topological_sort_util(self, v, visited, stack):
        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    def topological_sort(self, vertex_count):
        # Mark all the vertices as not visited
        visited = [False] * vertex_count
        stack = []

        # Sort starting from all vertices one by one
        for i in range(vertex_count):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        print(stack[::-1])  # return list in reverse order


g = Graph()
g.add_edge(0, 1).add_edge(0, 2).add_edge(1, 2).add_edge(2, 0).add_edge(2, 3).add_edge(
    3, 3
)
g.topological_sort(4)
g.dfs()


g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.topological_sort(6)
g.dfs()
