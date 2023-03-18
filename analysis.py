import random
from matplotlib import pyplot as plt
from graph import Graph

from selected1 import Algorithm1
from selected2 import Algorithm2
from selected3 import Algorithm3
from selected4 import Algorithm4

num_nodes = 30
max_degree = 5
num_trials = 10

algo1 = []
algo2 = []
algo3 = []
algo4 = []

for degree in range(1, max_degree+1):
    graph = Graph(num_nodes)
    graph.assign_random_values_to_edges()

    for i in range(num_trials):

        graph.generate_random_graph(degree)

        edges = graph.get_all_edges()
        random.shuffle(edges)

        algorithm1 = Algorithm1()
        algorithm2 = Algorithm2()
        algorithm3 = Algorithm3()
        algorithm4 = Algorithm4()

        for edge in edges:
            algorithm1.selected1(edge, graph)
            algorithm2.selected2(edge, graph)
            algorithm3.selected3(edge, graph)
            algorithm4.selected4(edge, graph)

        algo1.append(algorithm1.count // num_trials)    
        algo2.append(algorithm2.count // num_trials)   
        algo3.append(algorithm3.count // num_trials)   
        algo4.append(algorithm4.count // num_trials)   

print(algo1)
print(algo2)
print(algo3)
print(algo4)

X = range(1, max_degree+1)

plt.plot(X, algo1, label="selected1")
plt.plot(X, algo2, label="selected2")
plt.plot(X, algo3, label="selected3")
plt.plot(X, algo4, label="selected4")

plt.xticks(X)
plt.legend()
plt.show()