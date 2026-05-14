'''
Given two strings s1 and s2 of equal length, determine whether s2 is a rotation of s1.
A string is said to be a rotation of another if it can be obtained by shifting some leading characters of the original string to its end without changing the order of characters.

Examples: 

Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: After 2 right rotations, s1 will become equal to s2.

Input: s1 = "aab", s2 = "aba"
Output: true
Explanation: After 1 left rotation, s1 will become equal to s2.

Input: s1 = "abcd", s2 = "acbd"
Output: false
Explanation: Strings are not rotations of each other.
'''

def strings_are_rotation(s1,s2):
    for i in range(len(s2)):
        if s2 == s1:
            return True
        t = 0
        s2 = s2[t+1:] + s2[:t+1]
    return False

print(strings_are_rotation(s1="abcd", s2="cdab"))
    
