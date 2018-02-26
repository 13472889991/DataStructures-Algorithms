# Insertion Sort that runs in θ(n^2) time
# TODO:implement with binary search to insert, O(n(lg(n)) time

def insertionSort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        for z in range(0, i):
            if key < lst[i - z]:
                temp = lst[i - z]
                lst[i - z] = key
                lst[i - z + 1] = temp
    return lst
# Merge sort that runs in O(n(lg(n))) time

def mergeSort(lst):
    if (len(lst) == 1):
        return lst
    return merge(mergeSort(lst[0:len(lst) // 2]),
                 mergeSort(lst[len(lst) // 2:]))

def merge(lst, lst2):
    # individual list counters
    j = 0
    k = 0
    output = []
    # Append inf to end of arrays to make it easier
    lst.append(float("inf"))
    lst2.append(float("inf"))
    for i in range(len(lst) + len(lst2)):
        if lst[j] < lst2[k]:
            output.append(lst[j])
            j += 1
        elif lst2[k] < lst[j]:
            output.append(lst2[k])
            k += 1
        elif lst2[k] == lst[j] and lst2[k] != float("inf"):
            output.append(lst2[k])
            k += 1
    return output

def countingSort(lst, maximum = 0):
    sort=[]
    if maximum == 0:
        for i in lst:
            if maximum < i:
                maximum = i
    output=[0 for i in range(maximum + 1)]
    for i in lst:
        output[i]+=1
    for counter, value in enumerate(output):
        for i in range(value):
            sort.append(counter)
    return sort



            
            
    
    
    
