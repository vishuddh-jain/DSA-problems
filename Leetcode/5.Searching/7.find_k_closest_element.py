'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]
'''

def findClosestElements(arr, k, x):
        low = 0
        high = len(arr) - 1
    
        while (high - low +1) > k:

            if abs(arr[low] - x) > abs(arr[high] - x):  # "abs" is like a modulo function 
                low += 1
            else:
                high -= 1

        return arr[low:high + 1]
arr = [1,1,2,3,4,5]
k = 4
x = -1
print(findClosestElements(arr,k,x))