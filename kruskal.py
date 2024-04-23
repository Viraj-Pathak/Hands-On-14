class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(graph):
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((u, v, w))

    edges.sort(key=lambda x: x[2])
    vertices = set()
    for u, v, w in edges:
        vertices.add(u)
        vertices.add(v)

    disjoint_set = DisjointSet(vertices)
    minimum_spanning_tree = []
    for u, v, w in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            minimum_spanning_tree.append((u, v, w))

    return minimum_spanning_tree

# Example usage:
graph = {
    'A': [('B', 4), ('H', 8)],
    'B': [('A', 4), ('H', 11), ('C', 8)],
    'C': [('B', 8), ('I', 2), ('D', 7), ('F', 4)],
    'D': [('C', 7), ('F', 14), ('E', 9)],
    'E': [('D', 9), ('F', 10)],
    'F': [('C', 4), ('D', 14), ('E', 10), ('G', 2)],
    'G': [('F', 2), ('I', 6), ('H', 1)],
    'H': [('A', 8), ('B', 11), ('I', 7), ('G', 1)],
    'I': [('C', 2), ('H', 7), ('G', 6)]
}
print(kruskal(graph))
