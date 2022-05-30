# This code is contributed by Neelam Yadav and complete instruction is available on 
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


# pyhton code to print BFS traversal from a given source.
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)


    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
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


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
g.BFS(2)
