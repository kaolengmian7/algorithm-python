def three_sum(nums):
    result = []
    target = 0

    if (len(nums) < 3):
        return result

    nums.sort()

    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if (sum < target):
                j += 1
            elif (sum > target):
                k -= 1
            else:
                sumResult = [nums[i], nums[j], nums[k]]
                if sumResult not in result:
                    result.append(sumResult)
                j += 1

    return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
