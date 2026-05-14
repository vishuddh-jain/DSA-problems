'''
Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams — i.e., 
if they contain the same characters with the same frequencies.

Examples:

Input: s1 = “geeks”  s2 = “kseeg”
Output: true
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Input: s1 = "allergy", s2 = "allergyy"
Output: false
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams.

Input: s1 = "listen", s2 = "lists"
Output: false
Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams.
'''

def ifAnagrams(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    return False
print(ifAnagrams(s1="geeks", s2= "eekgs"))


# brute force approach

def isAnagram(s, t):

    # Length mismatch
    if len(s) != len(t):
        return False

        # Convert t into list so characters can be removed
    t_list = list(t)

        # Check every character of s
    for ch in s:

        if ch in t_list:
            t_list.remove(ch)

        else:
            return False

    return True

print(isAnagram(s="geeks", t= "eekgs"))