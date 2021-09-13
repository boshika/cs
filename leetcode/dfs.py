

"""Depth First Search-Iterative, O(V+E), O(V)"""

def dfs(start_node, graph):
    visited = set()
    stack = []

    stack.append(start_node)
    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)

            for i in graph[current_node]:
                stack.append(i)

        return visited



