'''
Given an array arr[] of positive integers and an integer k. You have to find the maximum value for each contiguous subarray of size k. 
Return an array of maximum values corresponding to each contiguous subarray.

Examples:

Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output: [3, 3, 4, 5, 5, 5, 6]
Explanation: 
1st contiguous subarray [1, 2, 3], max = 3
2nd contiguous subarray [2, 3, 1], max = 3
3rd contiguous subarray [3, 1, 4], max = 4
4th contiguous subarray [1, 4, 5], max = 5
5th contiguous subarray [4, 5, 2], max = 5
6th contiguous subarray [5, 2, 3], max = 5
7th contiguous subarray [2, 3, 6], max = 6

Input: arr[] = [5, 1, 3, 4, 2], k = 1
Output: [5, 1, 3, 4, 2]
Explanation: When k = 1, each element in the array is its own subarray, so the output is simply the same array
'''
# Time Limit Exceeding Approach

def maxOfSubarray(arr, k):
    l = 0
    result = []
    for r in range(k, len(arr)+1): 
        win_max = max(arr[l:r])
        result.append(win_max)
        l += 1
    return result
    
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
print(maxOfSubarray(arr, 3))

# Deque approach

from collections import deque
def maxOfSubarrays(arr, k):
        result =[]
        dq = deque()
        for i in range(len(arr)):
            
            # confirming if element not inside the window, if outside -> remove it
            while dq and dq[0] <= i-k:
                dq.popleft()
                
            # confirming if element is smaller than current and removing it
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
                
            dq.append(i)
            
            # confirming window is formed of size K 
            if i >= k-1:
                result.append(arr[dq[0]])
                
        return result
        
print(maxOfSubarray(arr = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3))