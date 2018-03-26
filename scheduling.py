class Task():
    def __init__(self, start, end, weight = 1):
        self.start = start
        self.end = end
        self.weight = weight

    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return (str(self.start)+ " : " +str(self.end))
def schedule(tasks):
    ''' Takes Tasks, a list of Task objects sorted by finishing time, and returns
        the optimal amount of scheduled tasks in order '''
    currentEnd = 0
    output = []
    for task in tasks:
        if task.start >= currentEnd:
            output.append(task)
            currentEnd = task.end
    return (output)
