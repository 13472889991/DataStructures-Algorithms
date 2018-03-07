import heapq
class Node:
    def __init__(self, value, adjList = None):
        #adjList should contain tuples in the form ("Weight","Name")
        self.value = value
        self.neighbours = adjList
        if self.neighbours == None:
            self.neighbours = [ ]
    def addNeighbours(self, edge):
        #edge should be in the form ("Weight","Name")
        self.neighbours.append(edge)
    def __str__(self):
        return (str(self.value))
def dijkstra(start):
    determined=[]
    queue=[]
    # distance of every node from start node
    distance={}
    distance[start] = 0
    for neighbours in start.neighbours:
        heapq.heappush(queue, neighbours)
        print (neighbours[1])
        distance[neighbours[1]] = neighbours[0]

    while queue:
        poppedNode = heapq.heappop(queue)
        determined.append(poppedNode)
        for tup in poppedNode.neighbours :
            vertex=tup[1]
            distance2=tup[0]
            #distance between the popped node and current vertex
            if distance[poppedNode.value] > distance[vertex] + distance2 :
                distance[poppedNode.value] = distance[vertex] + distance2
    return distance
