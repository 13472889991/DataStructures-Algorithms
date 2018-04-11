import math


class VanEmdeBoasLeaf():
    def __init__(self,size):
        if size != 2:
            raise ValueError('Leaf should only be of size 2!')
        else:
            self.leaf = True
            self.size = 2
            self.min = None
            self.max = None
            self.clusters = None
            self.summary = None
    def high(self, index):
        '''Returns the cluster index belongs to
           Arguments ---
           index -- index
        '''
        return int(math.floor(index / math.sqrt(self.size)))

    def low(self, index):
        '''Returns the index in the cluster it belongs to
           Arguments ---
           index -- index
        '''
        return (index % math.ceil(math.sqrt(self.size)))
	

class VanEmdeBoas():
    ''' Van Emde Boas tree implementation '''
    
    def high(self, index):
        '''Returns the cluster index belongs to
           Arguments ---
           index -- index
        '''
        return int(math.floor(index / math.sqrt(self.size)))

    def low(self, index):
        '''Returns the index in the cluster it belongs to
           Arguments ---
           index -- index
        '''
        return (index % math.ceil(math.sqrt(self.size)))
	
    def __init__(self, size):
        if size <= 0:
            raise ValueError('Invalid size of universe!')
        self.size = 2
        temp = 2
        while size > self.size:
            temp = self.size
            self.size = self.size * self.size
        self.min = None
        self.max = None
        self.leaf = False
        if temp > 2:
            self.clusters = [VanEmdeBoas(temp) for i in range (temp)]
            self.summary=VanEmdeBoas(temp)
        elif temp == 2:
            self.clusters=[VanEmdeBoasLeaf(temp) for i in range(temp)]
            self.summary = VanEmdeBoasLeaf(temp)


    def insert(self,s ,x):
        high = s.high(x)
        low = s.low(x)
        if s.min is None:
            s.min = x
            s.max = x
        if x < s.min:
            s.min , x = x , s.min
        if x > s.max:
            s.max , x = x , s.max
        if s.clusters != None:
            if(self.clusters[high].min is None):
                self.insert(s.summary,low)
            self.insert(s.clusters[high],low)
            
    def successor(self, s, x):
        high = self.high(x)
        low = self.low(x)
        if s.min == None:
            return None
        if x < s.min:
            return s.min
        if x > s.max:
            return None
        if x < s.clusters[high].max :
            return high* (int(math.sqrt(self.size))) + self.successor(s.clusters[high],low)
        else:
            temp = self.successor(s.summary,high)
            if temp == None:
                return s.max
            else:
                return temp*(int(math.sqrt(self.size))) + s.clusters[temp].min
                




'''    def insert(self,s ,x):
        high = self.high(x)
        low = self.low(x)
        print(high, " ", low)
        if s.min == None:
            s.min = s.max = x
        if x < s.min:
            s.min , x = x , s.min
        if x > s.max:
            s.max , x = x , s.max
        if s.clusters == None:
            pass
        elif s.clusters[high].min == None:
            self.insert(s.summary, high)
            s.summary.elements[high] = 1
            s.clusters[high].elements[low] = 1
            self.insert(s.clusters[high], low)
    '''
        
