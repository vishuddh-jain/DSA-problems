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


# using optimized approach to get O(n) time complexity

def productExceptSelf(nums):
    n = len(nums)
    answer = [1]*n

    prefix =1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    suffix =1
    for i in range(n-1, -1,-1):
        answer[i] *= suffix
        suffix *=nums[i]

    return answer

nums = [1,2,3,4]
print(productExceptSelf(nums))


