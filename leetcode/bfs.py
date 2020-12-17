"""BFS using a Queue, aka Level Order traversal
Time Complexity: O(V+E)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

class BreathFirstSearch:
    def bfs(self, graph, node):
        visited = []
        queue = []

        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            print (queue, visited)

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    def levelOrder(self, root):
        visited = []
        queue = []

        visited.append([root.val])
        queue.append(root.val)

        while queue:
            vertex = queue.pop(0)

            if vertex.left:
                queue.append(vertex.left)
                visited.append([vertex.left])
            elif vertex.right:
                queue.append(vertex.right)
                visited.append([vertex.right])

        return visited





bfs = BreathFirstSearch()
bfs.bfs(graph, 'A')