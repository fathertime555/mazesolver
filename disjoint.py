class DisjointSet:
    def __init__(self, elements):
        self.parent = {element: element for element in elements}
        self.rank = {element: 0 for element in elements}

    def find(self, element):
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element1, element2):
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1