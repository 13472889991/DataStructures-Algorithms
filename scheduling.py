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
    return (output[-1])

def compatible(task, tasks):
    ''' Given a task, and a separate list of tasks, returns a list of tasks that
        are compatible with the given task '''
    output = []
    for i in tasks:
        if i.end <= task.start
            output.append(i)
    return output

def weightedSchedule(tasks):
    opt=[0 for i in range(1,len(tasks))
    for i in range(1,len(tasks)):
        opt[i] = (max(i.weight + opt[compatible(i), opt[i-1]))
    return opt
                  
