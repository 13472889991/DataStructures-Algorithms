class Heap():
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return str(self.lst)
    # Returns left child index of node, runs in 0(1) time.Returns none if D.N.E
    
    def left(self, index):
        index += 1
        if 2 * index >= len(self.lst) + 1:
            return None
        return (2 * index - 1)
    # Returns right child index of node, runs in 0(1) time.Returns none if
    # D.N.E

    def right(self, index):
        index += 1
        if 2 * (index)  >= len(self.lst):
            return None
        return (2 * index)
    # Returns parent index of the node, runs in 0(1) time.Returns none if D.N.E

    def parent(self, index):
        if index == 0:
            return None
        index += 1
        return (index // 2 - 1)
    # Given a key, finds index of key. Runs in 0(n) time, where N is the size of Heap
    # Returns none if D.N.E

    def find(self, key):
        for counter, value in enumerate(self.lst):
            if key == value:
                return counter
        return None
    # appends a key to the end of the heap
    
    def append(self, key):
        self.lst.append(key)
    # Changes value of a key at a index to new key.

    def change(self, index, key):
        if index >= len(self.lst):
            self.lst[index] = key
    # Max_Heapify "fixes" the max heap at the index by swapping it with the
    # largest of its children.

    def max_heapify(self, index):
        largest = index
        l = self.left(index)
        r = self.right(index)
    
        if(l != None and self.lst[index] < self.lst[l]):
            largest = l
        if(r != None and self.lst[largest] < self.lst[r]):
            largest = r
        if largest != index:
            temp = self.lst[largest]
            self.lst[largest] = self.lst[index]
            self.lst[index] = temp
    def extract_max(self):
        self.lst[0], self.lst[len(self.lst)-1] = self.lst[len(self.lst)-1],self.lst[0]                                               
        output = self.lst.pop()
        self.build_max_heap()
        return output
    #Heap_sort sorts the heap.
    def build_max_heap(self):
        size = len(self.lst)
        for i in range(0, size//2):
            self.max_heapify(i)
    
    def heap_sort(self):
        for i in range (len(self.lst)):
            print(self.extract_max())
            self.build_max_heap()
        
        
