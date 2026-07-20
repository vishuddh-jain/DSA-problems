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
 
 

def longestPalindrome(s):

        start = 0
        end = 0

        for i in range(len(s)):

            len1 = expand(s, i, i)

            len2 = expand(s, i, i + 1)

            length = max(len1, len2)

            if length > end - start:

                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

def expand(s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1