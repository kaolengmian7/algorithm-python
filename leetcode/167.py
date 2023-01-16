def two_sum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while 1:
        sum = numbers[i] + numbers[j]
        if sum < target:
            i = i + 1
        elif sum > target:
            j = j - 1
        else:
            break
    return i + 1, j + 1

arr = [2,6,11,15]
target = 8
print(two_sum(arr, target))
