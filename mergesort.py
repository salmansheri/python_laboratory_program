def merge_sort(array: list) -> list:
    low = 1
    high = len(array)
    if low < high:
        mid = high // 2
        sort_left = array[:mid]
        sort_right = array[mid:]
        merge_sort(sort_left)
        merge_sort(sort_right)

        array.clear()
        while len(sort_left) > 0 and len(sort_right) > 0:
            if sort_left[0] <= sort_right[0]:
                array.append(sort_left[0])
                sort_left.pop(0)
            else:
                array.append(sort_right[0])
                sort_right.pop(0)
        for i in sort_left:
            array.append(i)
        for i in sort_right:
            array.append(i)
        return array


arr = []
num = int(input("Enter the number of element you want to enter in the array"))
for i in range(num):
    elements = int(input("Enter the element for the array to consist: "))
    arr.append(elements)
print("array = {}".format(arr))



print("array before sorting :\n {}".format(arr))
print("array after sorting:\n {}".format(merge_sort(arr)))
