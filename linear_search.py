def linear_search(array:list, number:int)-> int and str:
    """
    This function is used to determine searched using linear search
    :param array: the given number is searched in array
    :param number: this number to search in array
    :return: returns the index of the searching in the array
    """
    start = flag = 0
    end = len(array)
    while start < end:
        if array[start] == number:
            flag = 1
            break
        start += 1
    if flag == 1:
        return start

    else:
        return "number is not found in the array"


array = [1, 2, 3, 4, 5]
print("array = {}".format(array))
print("length of the array is {}".format(len(array)))
number = int(input("Enter the number you want to search using the linear search:\n"))
print("searching number is {}".format(number))

print("array = {}".format(array))
print("Index of the searching number is '{}' "
      .format(linear_search(array, number)))
