def selectsort(arr):
    min = arr[0]
    arr2 = []
    for i in range(0, len(arr)):
        if min > arr[i]:
            min = arr[i] 
    arr2.append(min)
    index = arr.index(min)
    arr.pop(index)

    min = arr[0]
    for x in range(0, len(arr)):
        if min > arr[x]:
            min = arr[x] 
    arr2.append(min)
    index = arr.index(min)
    arr.pop(index)

    min = arr[0]
    for x in range(0, len(arr)):
        if min > arr[x]:
            min = arr[x] 
    arr2.append(min)
    index = arr.index(min)
    arr.pop(index)

    min = arr[0]
    for x in range(0, len(arr)):
        if min > arr[x]:
            min = arr[x] 
    arr2.append(min)
    index = arr.index(min)
    arr.pop(index)

    min = arr[0]
    for x in range(0, len(arr)):
        if min > arr[x]:
            min = arr[x] 
    arr2.append(min)
    index = arr.index(min)
    arr.pop(index)

    print('arr2 is: ', arr2)
    return arr2
selectsort([2,4,3,1,0])


