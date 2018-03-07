from collections import defaultdict
INF=float("inf")

class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def addWeights(self,u,v,w):
        self.graph.append([u,v,w])
distances = {}
parents = {}

def bellmanford(graph, Start):
    for iterations in range(len(vertices) - 1):
        for u,v,w in graph.graph:
            relax(u,v,w)
    for u, v ,w in graph.graph:
        if distance[u] != INF and distance[u] + w < distance[v]:
            print ("This graph has a negative cycle!")
            return None

def relax(u,v,w):
    if distances[u] != INF and distance[u] + w < distance[v]:
        distance[v] = distance[u] + w

def initialize(graph, start):
    distances = {}
    parents = {}
    for vertices in graphraph.vertices:
            distances[i] = INF
            parents[i] = None

    distances[start] = 0
