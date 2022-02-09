def selection_sort(array):
    size = len(array)
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if array[j] < array[min]:
                min = j

        temp = array[i]
        array[i] = array[min]
        array[min] = temp
    return array


array = [5, 3, 8, 6, 7, 2]
size = len(array)
print("Size of the array = '{}'".format(size))
print("array before sorting '{}' ".format(array))
print("array after sorting '{}' ".format(selection_sort(array)))

print()
