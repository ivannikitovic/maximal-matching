from graph import Graph

class Algorithm1:

    def __init__(self) -> None:
        self.count = 0

    def selected1(self, e: tuple[int], G: Graph) -> bool:
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
        selected = True
        r_e = G.get_edge_random_value(e)

        adj_edges = G.get_adjacent_edges(e)

        for edge in adj_edges:
            r_e_prime = G.get_edge_random_value(edge)

            if r_e_prime < r_e:
                self.count += 1
                if self.selected1(edge, G):
                    selected = False

        return selected

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

    algorithm1 = Algorithm1()

    for edge in edges:
        if algorithm1.selected1(edge, test):
            maximal_matching_set.add(frozenset(edge))

    print([list(edge) for edge in maximal_matching_set])

    print(algorithm1.count)