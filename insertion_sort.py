def insertion_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        pos = i
        while pos > 0 and array[pos - 1] > value:
            array[pos] = array[pos - 1]
            pos = pos - 1
        if pos != i:
            array[pos] = value

    return array


array = []
n = int(input("Enter the upper limit: \n"))
for i in range(n):
    array.append(int(input()))

print("array before sorting:\n{}".format(array))
print("array after sorting:\n {}".format(insertion_sort(array)))
