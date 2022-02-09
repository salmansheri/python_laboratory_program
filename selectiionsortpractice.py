def selection_sort(array):
    size = len(array)
    for i in range(size):
        min = i
        for j in range(i + 1, size):
            if array[j] < array[min]:
                min = j

        temp = array[i]
        array[i] = array[min]
        array[min] = temp

    return array


array = [5,4,3,2,1]
print("array element before sorting {}".format(array))
print("array element after sorting {}".format(selection_sort(array)))
