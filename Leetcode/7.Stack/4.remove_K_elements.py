'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''

def RemoveKelements(num,k):
    stack = []
    for digit in num:
        
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k-=1
        
        stack.append(digit)
        
    while k > 0:
        stack.pop()
        k-=1
        
    result = ''.join(stack).lstrip('0') # this is to remove if any leading zeros in the result is present
    
    if result:
        return result
    else:
        return "0"
    
print(RemoveKelements(num='1432219', k=3)) 