'''
Given two numbers as strings s1 and s2, calculate their product.
Note: The numbers can be negative. There can be zeros in the beginning of the numbers.

Examples:

Input: s1 = "0033", s2 = "2"
Output: "66"
Explanation: 33 * 2 = 66

Input: s1 = "11", s2 = "23"
Output: "253"
Explanation: 11 * 23  = 253

Input: s1 = "123", s2 = "0"
Output: "0"
Explanation: Anything multiplied by 0 is equal to 0.
'''


# Solved using inbuilt methods
def MultiplyStrings(s1, s2):
    s1 = int(s1)
    s2 = int(s2)
    result = s1*s2
    return result

print(MultiplyStrings(s1="0033", s2="3"))

# Using proper iterative approach
def multiply_strings(s1, s2):
    s1_int = str_to_int(s1)
    s2_int = str_to_int(s2)
    ans = s1_int *s2_int
    return ans
def str_to_int(str_n):
    result = 0
    for ch in str_n:
        digit = ord(ch) - ord('0')
        result = result * 10 + digit
    return result 
        
print(multiply_strings(s1="0033", s2="3"))