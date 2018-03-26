class Stack():
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return str(self.lst)

    def pop(self):
        return self.lst.pop()

    def insert(self, value):
        self.lst.append(value)

    def size(self):
        return len(self.lst)

class Queue():
    def __init__(self, lst):
        self.lst = lst[:-1]

    def __str__(self):
        return str(self.lst)
    
    def insert(self, value):
        self.lst.insert(0,item)

    def remove(self):
        return self.lst.pop()

    
