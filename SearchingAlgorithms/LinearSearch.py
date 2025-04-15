def LinearSearch(items,itemToFind):
    steps = []
    if len(items) > 0:
        for i in range(len(items)):
            item = items[i]
            steps = steps + [items[:i]]
            
            if item == itemToFind:
                return i,steps + [items[:i+1]] + [[itemToFind]]

    return -1,steps

'''listToSearch = [1,4,6,7,9,12,13,16,70,104,108]
print(f"{LinearSearch(listToSearch,16)}")'''