'''
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.
Note: A subarray is a contiguous part of any given array.
Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.

Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.

Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400
Explanation: arr3 = 400, which is maximum.
'''

def maxSubarraySum(arr, k):
    win_sum = sum(arr[:k])
    max_sum = win_sum
    
    for i in range(len(arr)-k):
        win_sum = win_sum - arr[i] - arr[i+k]
        max_sum = max(win_sum, max_sum)
        
    return max_sum

print(maxSubarraySum(arr=[100,200,300,400], k = 4))