"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
"""

# Solved using recursion
def isMatch(s, p):
    def solve(i, j):

            # Case 1: Both string and pattern are finished
            if i == len(s) and j == len(p):
                return True

            # Case 2: Pattern finished but string remains
            if j == len(p):
                return False

            # Case 3: String finished but pattern remains
            if i == len(s):
                while j < len(p):
                    if p[j] != "*":
                        return False
                    j += 1
                return True

            # Case 4: Characters match or '?'
            if s[i] == p[j] or p[j] == "?":
                return solve(i + 1, j + 1)

            # Case 5: '*'
            if p[j] == "*":

                # Option 1: '*' matches nothing
                # Option 2: '*' matches one character
                return solve(i, j + 1) or solve(i + 1, j)

            # Case 6: Characters don't match
            return False

    return solve(0, 0)

print(isMatch(s="abcd", p="*c*"))

