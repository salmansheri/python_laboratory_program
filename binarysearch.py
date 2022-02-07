def binary_search(array, number):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while start <= end:
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        step = step+1
        mid = (start + end) // 2
        print(mid)

        if number == array[mid]:
            return mid

        if number < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
number = int(input("Please Enter the number to search:-\n"))

print("Searching for {} in {}".format(number, array))
print("Index of {}: {}".format(number, binary_search(array, number)))
