"""
what is Binary search:
     Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array.
     If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
     Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
"""


def binary_search(array:list, number:int) -> int:
    """
    This function is used to index of the searched element by using binary search
    :param array: array is the list to search
    :param number: number is the number to search in the list
    :return: it returns the index of the searching number in the list
    """
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while start <= end:
        print("subarray in step {} : {}".format(step, str(array[start:end + 1])))
        # increment the step value
        step = step + 1
        # enter the formula for the binary search
        mid = (start + end) // 2
        # if number is equal to mid element of the array it will print the mid element of the array

        if number == array[mid]:
            return mid
        # other wise if the number is lesser then the mid element of the array mid element is subtracted by 1

        elif number < array[mid]:
            end = mid - 1
            print(end)
        # other wise if the number is greater then the mid element of the array mid elemen start element is equal to mid + 1

        else:
            start = mid + 1
            print(start)
    # if all the above conditions are false it will return -1

    return -1



array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
print("array = {}".format(array))
print("The length of the array is {}".format(len(array)))
number = int(input("please enter the number to search:\n"))
print("searching number is {}".format(number))

print("searching for {} in {}".format(number,array))
print("index of {} in the array is '{}' ".format(number, binary_search(array, number)))
