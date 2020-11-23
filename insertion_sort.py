def insertion_sort(arr):
    for i in range(0, len(arr)):
        min = arr[i]
        hold = i-1
        while hold >= 0 and min < arr[hold]:
            arr[hold + 1] = arr[hold]
            hold -= 1
        arr[hold + 1] = min
    print('arr is:', arr)

insertion_sort([3,2,6,0,1])