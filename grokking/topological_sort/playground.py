from collections import defaultdict, deque

directed_edges = [[3, 2], [3, 0], [2, 1]]

graph = defaultdict(list)
for start, end in directed_edges:
    graph[start].append(end)
    # for non-directional graph
    # graph[end].append(start)
