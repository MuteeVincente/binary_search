### BINARY SEARCH  is   a searching algorithm for finding an element's position in a sorted algorithm.


# The elements can be sorted in descending or ascending order( Doesn't matter the order.

### THIS IS THE CODE IN PYTHON.


def binary_search(arr,target):

    #this is the same as low = 0 and high = len(arr) -1

    low , high = 0 , len(arr) - 1


    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return - 1


sorted_list = input("Enter sorted list elements: \n").split()


print("Sorted list : ", sorted_list)

target_element = input ("\nEnter the target element of the above array  : \n")

position = binary_search (sorted_list , target_element)


if position != -1:
    print(f"{target_element} found at index { position} ")
else:
    print(f"{target_element}  Not Found")
