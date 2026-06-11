'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
'''
def isValid(s):
        stack = []
        brackets = {
            ')' : '(', 
            '}' : '{', 
            ']' : '['
        }
        for ch in s:
            if ch in "({[":
                stack.append(ch)

            else:
                if not stack:
                    return False
                
                if stack[-1] != brackets[ch]:
                    return False
                
                stack.pop()

        return len(stack) == 0
print(isValid(s='(([]}))'))