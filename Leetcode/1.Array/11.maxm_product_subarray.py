"""
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Note that the product of an array with a single element is the value of that element.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

def maxproduct(arr):
    pre =1
    suff =1
    if len(arr) == 1:
        return arr[0]
    max_prod = 0
    n = len(arr)
    for i in range(n):
        if pre == 0:
            pre =1
        if suff == 0:
            suff =1
        
        pre = pre * arr[i]
        suff = suff * arr[n-i-1]
        max_prod = max(max_prod, pre, suff)
    return max_prod

print(maxproduct(arr= [2,3,-2,4]))