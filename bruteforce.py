from graph import Graph

import random

def bruteforce(G: Graph) -> list[list[int]]:
    """
    Inputs
    --------------------

    G: Graph
        Graph represented by our graph class defined in
        graph.py.

    Outputs
    --------------------

    maximal_matching: list[list[int]]
        Returns a random set of maximal matching pairs 
        found using brute force.

    """
    edges = G.get_all_edges()
    random.shuffle(edges)

    M = set()

    for i in range(len(edges)):
        idx1, idx2 = edges[i]

        shares_endpoint = False
        for edge in M:
            if idx1 in edge or idx2 in edge:
                shares_endpoint = True
                break

        if not shares_endpoint:
            M.add(frozenset(edges[i]))

    return [list(edge) for edge in M]

if __name__ == "__main__":
    test = Graph(5)

    test.adj[0] = [0, 1, 0, 0, 1]
    test.adj[1] = [1, 0, 1, 1, 1]
    test.adj[2] = [0, 1, 0, 1, 0]
    test.adj[3] = [0, 1, 1, 0, 1]
    test.adj[4] = [1, 1, 0, 1, 0]

    print(test)

    print(bruteforce(test))