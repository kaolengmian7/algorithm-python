def four_sum(nums, target):
    result = []

    if (len(nums) < 4):
        return result

    nums.sort()

    for i in range(0, len(nums)-3):
        for j in range(i+1, len(nums)-2):
            l = j + 1
            r = len(nums)-1
            while l < r:
                sum = nums[i]+nums[j]+nums[l]+nums[r]
                if (sum > target):
                    r -= 1
                elif (sum < target):
                    l += 1
                else:
                    subRes = [nums[i], nums[j], nums[l], nums[r]]
                    if subRes not in result:
                        result.append(subRes)
                    l += 1
    return result

print(four_sum([1,0,-1,0,-2,2], 0))

