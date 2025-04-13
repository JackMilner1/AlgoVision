def BinarySearch(items,itemToFind,start,end):
    steps = []

    steps.append(items[start:end])
    if end - start == 1:
        return -1,steps
    
    index = (start + end) // 2
    
    if items[index] == itemToFind:
        return index,steps + [[itemToFind]]
    else:
        data = None

        if itemToFind > items[index]:
            data = BinarySearch(items,itemToFind,index,end)
        else:
            data = BinarySearch(items,itemToFind,start,index)

        index = data[0]
        steps = steps + data[1]
    
    return index,steps

def isInOrder(items):
    if len(items) < 2:
        return True
    
    currentValue = items[0]
    for i in range(1,len(items)):
        if items[i] < currentValue:
            return False
        
        currentValue = items[i]
    
    return True
    
    
'''listToSearch = [1,4,6,7,9,12,13,16,70,104,108]
data = BinarySearch(listToSearch,16,0,len(listToSearch))
print(f"Steps to completion {data[1]}\nIndex of item {data[0]}")'''