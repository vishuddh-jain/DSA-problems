'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''

def longestPalindromicSubstring(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            temp = s[i:j+1]
            if ispalindrome(temp):
                if len(temp) > len(longest):
                    longest = temp
    return longest
                
def ispalindrome(S):
    if S == S[::-1]:
        return True
    return False

s = "babad"
print(longestPalindromicSubstring(s))
 