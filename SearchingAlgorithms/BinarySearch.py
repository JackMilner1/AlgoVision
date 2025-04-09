def BinarySearch(items,itemToFind,start,end):
    steps = []

    steps.append(items[start:end])
    if end - start == 1:
        return -1,steps
    
    index = (start + end) // 2
    
    if items[index] == itemToFind:
        return index,steps
    else:
        data = None

        if itemToFind > items[index]:
            data = BinarySearch(items,itemToFind,index,end)
        else:
            data = BinarySearch(items,itemToFind,start,index)

        index = data[0]
        steps = steps + data[1]
    
    return index,steps

    
listToSearch = [1,4,6,7,9,12,13,16,70,104,108]
data = BinarySearch(listToSearch,16,0,len(listToSearch))
print(f"Steps to completion {data[1]}\nIndex of item {data[0]}")