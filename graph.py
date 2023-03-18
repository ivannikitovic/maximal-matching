import random

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

    test.adj[0] = [0, 1, 0, 0, 1]
    test.adj[1] = [1, 0, 1, 1, 1]
    test.adj[2] = [0, 1, 0, 1, 0]
    test.adj[3] = [0, 1, 1, 0, 1]
    test.adj[4] = [1, 1, 0, 1, 0]

    print(test)

    print(test.get_adjacent_edges((1, 4)))

    print(test.get_all_edges())