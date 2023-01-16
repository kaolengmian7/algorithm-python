def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest_num_index(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def find_smallest_num_index(arr):
    smallest_num = arr[0]
    smallest_num_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_num_index = i
    return smallest_num_index


print(selection_sort([5, 3, 6, 2, 10]))
