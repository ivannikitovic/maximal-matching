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

algo1 = [0 for i in range(max_degree)]
algo2 = [0 for i in range(max_degree)]
algo3 = [0 for i in range(max_degree)]
algo4 = [0 for i in range(max_degree)]

for degree in range(1, max_degree+1):
    graph = Graph(num_nodes)
    graph.generate_random_graph(degree)
    
    for i in range(num_trials):
        graph.assign_random_values_to_edges()

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

        algo1[degree-1] += algorithm1.count // num_trials   
        algo2[degree-1] += algorithm2.count // num_trials  
        algo3[degree-1] += algorithm3.count // num_trials    
        algo4[degree-1] += algorithm4.count // num_trials    

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