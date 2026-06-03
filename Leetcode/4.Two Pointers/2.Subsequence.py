'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''

def isSubsequence(s: str, t: str) -> bool:
    result = ''
    i=0
    if len(s) == 0:
        return True
    if len(s) < len(t):
        for j in range(len(t)):
            if t[j] == s[i]:
                result += s[i]
                if result == s:
                    return True
                i+=1
        return False
    else:
        return False

    
print(isSubsequence(s="abc", t="ahbgdc"))
print(isSubsequence(s="axc", t="ahbgdc"))