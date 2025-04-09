def LinearSearch(items,itemToFind):
    steps = []
    for i in range(len(items)):
        item = items[i]
        steps = steps + [item]
        
        if item == itemToFind:
            return steps,i

    return steps,-1

listToSearch = [1,4,6,7,9,12,13,16,70,104,108]
print(f"{LinearSearch(listToSearch,16)}")