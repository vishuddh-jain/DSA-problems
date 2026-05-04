# basic approach time complexity O(n^2)

import math
def productExceptSelf(nums):
    answer = []

    for i in range(len(nums)):
        temp = nums[:i] + nums[i+1:]
        result = math.prod(temp)
        answer.append(result)
    return answer

nums = [1,2,3,4]
print(productExceptSelf(nums))