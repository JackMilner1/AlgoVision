
def BubbleSort(items):
    steps = []
    for i in range(len(items)):
        currentIndex = 0
        numSwaps = 0

        for j in range(len(items) - 1):
            nextIndex = currentIndex + 1
            steps = steps + [items[currentIndex :nextIndex + 1]]
            if items[currentIndex] >= items[nextIndex]:
                placeholder = items[currentIndex]
                items[currentIndex] = items[nextIndex]
                items[nextIndex] = placeholder
                numSwaps += 1

            currentIndex += 1
            steps = steps + [items[currentIndex - 1 :nextIndex + 1]]

        if numSwaps == 0:
            break

    return steps

print(BubbleSort([1,3,4,2,6,9,10,21,14,28]))
