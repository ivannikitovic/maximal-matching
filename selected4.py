from graph import Graph

class Algorithm4:

    def __init__(self) -> None:
        self.count = 0
        self.memo = {}

    def selected4(self, e: tuple[int], G: Graph):
        """
        Inputs
        --------------------

        e: tuple
            Denotes the edge to check whether it was selected
            to the maximal matching. It contains two integers
            denoting the vertices it connects.

        G: Graph
            Graph represented by our graph class defined in
            graph.py.

        Outputs
        --------------------

        selected: bool
            True if given edge e was selected to the maximal
            matching, False otherwise.

        """
        self.count += 1

        r_e = G.get_edge_random_value(e)

        adj_edges = G.get_adjacent_edges(e)
        adj_edges_sorted = sorted(adj_edges, key=G.get_edge_random_value)

        for i in range(len(adj_edges_sorted)):
            r_e_i = G.get_edge_random_value(adj_edges_sorted[i])

            if r_e_i < r_e:
                if adj_edges_sorted[i] in self.memo:
                    selected = self.memo[adj_edges_sorted[i]]
                else:
                    selected = self.selected4(adj_edges_sorted[i], G)
                    self.memo[adj_edges_sorted[i]] = selected
                
                if selected:
                    return False

        return True

if __name__ == "__main__":
    test = Graph(5)

    test.adj[0] = [0, 1, 0, 0, 1]
    test.adj[1] = [1, 0, 1, 1, 1]
    test.adj[2] = [0, 1, 0, 1, 0]
    test.adj[3] = [0, 1, 1, 0, 1]
    test.adj[4] = [1, 1, 0, 1, 0]

    print(test)

    edges = test.get_all_edges()

    maximal_matching_set = set()

    algorithm1 = Algorithm4()

    for edge in edges:
        if algorithm1.selected4(edge, test):
            maximal_matching_set.add(frozenset(edge))

    print([list(edge) for edge in maximal_matching_set])

    print(algorithm1.count)