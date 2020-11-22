def selectsort(arr):
    min = arr[0]
    arr2 = []
    for i in range(0, len(arr)):
        # min = arr[i]
        if min > arr[i]:
            min = arr[i] 
    print('min is:', min)
    arr2.append(min)
    index = arr.index(min)
    arr.pop(index)
    print('index of min is:', index)
    print('arr now is:', arr)

    min = arr[0]
    for x in range(0, len(arr)):
        if min > arr[x]:
            min = arr[x] 
    print('minum is:', min)
    arr2.append(min)
    index = arr.index(min)
    arr.pop(index)
    print('index of min is:', index)
    print('arr now is:', arr)

    min = arr[0]
    for x in range(0, len(arr)):
        if min > arr[x]:
            min = arr[x] 
    print('minum is:', min)
    arr2.append(min)
    index = arr.index(min)
    arr.pop(index)
    print('index of min is:', index)
    print('arr now is:', arr)

    min = arr[0]
    for x in range(0, len(arr)):
        if min > arr[x]:
            min = arr[x] 
    print('minum is:', min)
    arr2.append(min)
    index = arr.index(min)
    arr.pop(index)
    print('index of min is:', index)
    print('arr now is:', arr)

    min = arr[0]
    for x in range(0, len(arr)):
        if min > arr[x]:
            min = arr[x] 
    print('minum is:', min)
    arr2.append(min)
    index = arr.index(min)
    arr.pop(index)
    print('index of min is:', index)
    print('arr now is:', arr)
    
    print('arr2 is: ', arr2)
selectsort([2,4,3,1,0])


