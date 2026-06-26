'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''


def isPalindrome(s):
        alphabets = list("abcdefghijklmnopqrstuvwxyz0123456789")
        s = s.lower()
        string = ""
        for i in s:
            if i in alphabets:
                string += i
        if string == string[::-1]:
            return True
        return False
    
print(isPalindrome(s="racecar"))

# 19ms Time complexity

            
