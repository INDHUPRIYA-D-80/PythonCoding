from collections import deque

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adj_matrix = [[0 for _ in range(self.v)] for _ in range(self.v)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def bfs(self, start):
        visited = [False]*self.v
        levels  = [-1]*self.v
        parent = [-1]*self.v

        traversal = []

        q = deque()
        
        # Starting node
        q.append(start)
        visited[start] = True
        levels[start] = 0
        # Parent is still gonna be -1 for start node

        while q:
            curr_node = q.popleft()
            # This is the place where you edit your node
            traversal.append(curr_node)
            for neighbor in range(self.v):
                if self.adj_matrix[curr_node][neighbor] == 1  and not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True
                    levels[neighbor] = levels[curr_node] + 1
                    parent[neighbor] = curr_node

        return traversal, levels, parent
                    
    def shortest_path(self, start, end):
        _, levels, parent = self.bfs(start)
        path = []

        while end != -1:
            path.append(end)
            end = parent[end]

        return path[::-1]

g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

start_node = 1
end_node = 4

traversal, levels, parent = g.bfs(start_node)

print(traversal)
print(levels)
print(parent)

print(g.shortest_path(start_node, end_node))