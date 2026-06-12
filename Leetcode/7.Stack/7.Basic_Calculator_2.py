'''
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
'''
def calculate(s):

        stack = []
        num = 0
        sign = '+'

        for i in range(len(s)):

            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch) # if only digit input is given

            if ch in "+-*/" or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    stack.append(stack.pop() * num)

                elif sign == '/':
                    stack.append(int(stack.pop() / num))

                sign = ch
                num = 0

        return sum(stack)
print(calculate(s="3+2*2"))