# This code is contributed by Neelam Yadav and complete instruction is available on
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


# pyhton code to print BFS traversal from a given source.
from collections import defaultdict
import numpy as np


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # find the maximum number of nodes

    def maxNode(self):

        nodes = list(self.graph.values())
        nodes.append(list(self.graph.keys()))
        nodes = list(np.concatenate(nodes).flat)
        uniqueNodes = np.unique(nodes)
        return np.max(uniqueNodes)

    # Function to print a BFS of graph

    def BFS(self, s):
        visited = [False] * (self.maxNode() + 1)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    # Function to print a DFS of graph

    def dfsFunc(self, s, visited):
        visited[s] = True
        print(s)
        for i in self.graph[s]:
            if visited[i] == False:
                self.dfsFunc(i, visited)

    # Function for preparation of DFS traversal

    def DFS(self, s):
        visited = [False] * (self.maxNode() + 1)
        self.dfsFunc(s, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

g.DFS(0)
