def select_sort(array):
    for i in range(0, len(array)):
        index = i
        for x in range(i+1,len(array)):
            if array[index] > array[x]:
                index = x
        array[i], array[index]=array[index], array[i]
    print('array is:', array)

select_sort([2,0,1,3,4])