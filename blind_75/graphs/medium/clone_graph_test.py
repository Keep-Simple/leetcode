class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    """
    https://leetcode.com/problems/clone-graph/

    Given a reference of a node in a connected undirected graph.
    Return a deep copy (clone) of the graph.

    Each node in the graph contains a value (int)
    and a list (List[Node]) of its neighbors.

    Constraints:
        The number of nodes in the graph is in the range [0, 100].
        1 <= Node.val <= 100
        Node.val is unique for each node.
        There are no repeated edges and no self-loops in the graph.
        The Graph is connected and all nodes can be visited starting from the given node.
    """
    if not node:
        return None

    new_nodes_map = {}

    def dfs(node):
        if node in new_nodes_map:
            return new_nodes_map[node]

        new_node = Node(node.val)
        new_nodes_map[node] = new_node

        for neighbor in node.neighbors:
            new_node.neighbors.append(dfs(neighbor))

        return new_node

    return dfs(node)
