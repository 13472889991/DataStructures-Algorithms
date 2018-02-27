
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
        hashed = self.hashing(key)
        for lst in (self.dict[hashed]):
            if lst[0] == key:
                return lst[1]
                
        return None
    def delete(self, key):
        hashed = self.hashing(key)
        for lst in (self.dict[hashed]):
            if lst[0] == key:
                self.dict[hashed].remove(lst)
        if len(self.dict[hashed]) == 0:
            self.dict[hashed].append(None)
            self.dict[hashed].append(None)

    def tableDoubling(self):
        table = [[None,None] for i in range(self.size)]
        self.dict.extend(table)
        self.size *= 2
# Dictionary with open addressing instead
class Dictionary2():
    def __init__(self, size = 10):
        self.dict = [[None,None] for i in range(size)]
        self.size = size
        self.inserted = 0
        
    def __str__(self):
        return str(self.dict)
    
    def hashing(self, key):
        return key % self.size
    
    def hashing2(self, key , counter):
        return counter * key % self.size
    
    def insert(self, key, value, counter = 1):
        if self.inserted >= self.size // 2 :
            self.tableDoubling()
        hashed = self.hashing(key)
        if self.dict[hashed][0] == None or self.dict[hashed][0] == "Deleted":
            self.dict[hashed]=[[key,value]]
            self.inserted += 1
            return True
        else:
            hashed2=self.hashing2(key, counter)
            probe=(hashed * counter * hashed2) % self.size
            if self.dict[probed][0] == None:
                self.dict[probed][0] == [[key, value]]
                self.inserted += 1
            else:
                counter += 1
                self.insert(key, value, counter)
            
    def find(self, key, counter = 1)
        hashed = self.hashing(key)
        probe=(hashed * counter * hashed2) % self.size
            if self.dict[hashed][0] == key:
                return self.dict[hashed]
            else:
                if self.dict[probed][0] != None:
                    if key == self.dict[probed][0]:
                        return self.dict[probed]
                if self.dict[probed][0] == None:
                    return None
                counter += 1
                self.find(self, key, counter)

    
    def delete(self, key):
        hashed = self.hashing(key)
        for lst in (self.dict[hashed]):
            if lst[0] == key:
                self.dict[hashed].remove(lst)
        if len(self.dict[hashed]) == 0:
            self.dict[hashed].append("Deleted")
            self.dict[hashed].append("Deleted")

    def tableDoubling(self):
        table = [[None,None] for i in range(self.size)]
        self.dict.extend(table)
        self.size *= 2
