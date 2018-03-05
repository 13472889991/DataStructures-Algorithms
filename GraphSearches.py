class Graph():
    def __init__(self, lst):
        self.vertices={}
        for i in lst:
            self.vertices[i[0]] = []
            self.vertices[i[1]] = []
        for i in lst:
            self.vertices[i[0]].append(i[1])
            self.vertices[i[1]].append(i[0])
        
    def __str__(self):
        return str(self.vertices)

    # Start is the first node you want to start at
    def BFS(self, start):
        level = {start : 0}
        parent = {start : None}
        levelCounter = 1
        frontier = [start]
        while frontier: #While there are descendants
            nextFrontier = [ ]
            for vertice in frontier:
                for connection in self.vertices[vertice]:
                    if connection not in level:
                        level[connection] = levelCounter
                        parent[connection] = vertice
                        nextFrontier.append(connection)
            frontier = nextFrontier
            levelCounter += 1
        print str(level)
    def DFS(self, start):
        parent = { }
        for vertices in self.vertices[start]:
            if vertices not in parent:
                parent[start] = None
                
                return self.DFSVisit(start, parent)
        

    def DFSVisit(self, start, parent):
        for vertices in self.vertices[start]:
            if vertices not in parent:
                parent[vertices] = start
                return self.DFSVisit(start, parent)
        
