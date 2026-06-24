'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
'''
def longestValidParenthesis(s):
    stack = [-1]
    ans = 0
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
            
        else:
            stack.pop()
            
            if not stack:
                stack.append(i)
                
            else:
                ans = max(ans, i - stack[-1])
    return ans

print(longestValidParenthesis("((())))()()))"))