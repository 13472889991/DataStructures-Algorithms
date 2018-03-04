class Graph():
    def __init__(self, lst):
        self.vertices={}
        for i in lst:
            self.vertices[i[0]]=[]
            self.vertices[i[1]]=[]
        for i in lst:
            self.vertices[i[0]].append(i[1])
            self.vertices[i[1]].append(i[0])
        
    def __str__(self):
        return str(self.vertices)

    # Start is the first node you want to start at
    def BFS(self, start):
        level = {start : 0}
        parent = {start : None}
        i = 1
        frontier = [start]
        while frontier:
            nextFrontier = [ ]
            for u in frontier:
                for v in self.vertices[u]:
                    if v not in level:
                        level[v] = i
                        parent[v] = u
                        nextFrontier.append(v)
            frontier = nextFrontier
            i += 1
        print str(level)
