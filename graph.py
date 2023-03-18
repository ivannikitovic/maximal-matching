import random
from math import floor

class Graph:

    def __init__(self, num_nodes: int) -> None:
        """

        """
        self.n = num_nodes

        self.adj = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.r = [[0 for _ in range(self.n)] for _ in range(self.n)]

        self.assign_random_values_to_edges()

    def __repr__(self) -> str:
        result = ""

        for i in range(self.n):
            for j in range(self.n):
                result += str(self.adj[i][j]) + " "
            result += "\n"

        return result
    
    def generate_random_graph(self, degree: int, method : str = "union") -> None:
        if method == "union":
            random_matchings = []

            for _ in range(degree):
                matching = [[0 for _ in range(self.n)] for _ in range(self.n)]
                size = floor(self.n / 2.0)
                k = 0

                while k != size:
                    i = random.randint(0, self.n-1)
                    j = random.randint(0, self.n-1)

                    if i != j and 1 not in matching[j] and 1 not in matching[i]:
                        matching[i][j] = 1
                        matching[j][i] = 1
                        k += 1

                random_matchings.append(matching)

            for matching in random_matchings:
                for i in range(self.n):
                    for j in range(self.n):
                        if matching[i][j] == 1:
                            self.adj[i][j] = 1
                            self.adj[j][i] = 1

        if method == "euclidean":
            coords = [(random.random(), random.random()) for _ in range(self.n)]

            for i in range(self.n):
                distances = [((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)**0.5 for j in range(self.n)]
                sorted_distances = sorted(list(zip(distances, range(self.n))))[1:]

                for k in range(degree):
                    j = sorted_distances[k][1]
                    self.adj[i][j] = 1
                    self.adj[j][i] = 1
                    
    def assign_random_values_to_edges(self, seed=None) -> None:
        """
        
        """
        if seed:
            random.seed(seed)

        for i in range(self.n):
            for j in range(self.n):
                if j > i:
                    self.r[i][j] = random.random()
                if j < i:
                    self.r[i][j] = self.r[j][i]

    def get_adjacent_edges(self, e: tuple[int]) -> list[tuple[int]]:
        """
        
        """
        idx1, idx2 = e

        result = []

        for i in range(self.n):
            if self.adj[idx1][i] == 1 and i != idx2:
                result.append((idx1, i))
            
            if self.adj[idx2][i] == 1 and i != idx1:
                result.append((idx2, i))
                
        return result
    
    def get_all_edges(self) -> list[tuple[int]]:
        """
        
        """
        result = set()

        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] == 1 and i != j:
                    result.add(frozenset(sorted((i, j))))
        
        return [list(edge) for edge in result]

    def get_edge_random_value(self, e: tuple[int]) -> float:
        idx1, idx2 = e

        return self.r[idx1][idx2]

if __name__ == "__main__":
    test = Graph(5)

    # test.adj[0] = [0, 1, 0, 0, 1]
    # test.adj[1] = [1, 0, 1, 1, 1]
    # test.adj[2] = [0, 1, 0, 1, 0]
    # test.adj[3] = [0, 1, 1, 0, 1]
    # test.adj[4] = [1, 1, 0, 1, 0]

    test.generate_random_graph(2, method="union")

    print(test)

    # print(test.get_adjacent_edges((1, 4)))

    print(test.get_all_edges())