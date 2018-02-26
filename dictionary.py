
#Simple dictionary with hashes by modulo, table doubling for size
#and chaining for collisions
class Dictionary():
    def __init__(self, size = 10):
        self.dict = [[None,None] for i in range(size)]
        self.size = size
        self.inserted = 0
    def __str__(self):
        return str(self.dict)
    def hashing(self, key):
        return key % self.size
    def insert(self, key, value):
        if self.inserted >= self.size // 2 :
            self.tableDoubling()
        hashed = self.hashing(key)
        if self.dict[hashed][0] == None:
            self.dict[hashed]=[[key,value]]
            self.inserted += 1
        else:
            self.dict[hashed].append([key,value])
            self.inserted += 1
    def find(self, key):
        hashed=self.hashing(key)
        for lst in (self.dict[hashed]):
            if lst[0] == key:
                return lst[1]
                
        return None
    
    def tableDoubling(self):
        table = [[None,None] for i in range(self.size)]
        self.dict.extend(table)
        self.size *= 2
