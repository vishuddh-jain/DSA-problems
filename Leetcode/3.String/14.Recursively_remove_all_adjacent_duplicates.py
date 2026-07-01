'''
Given a string s, remove all its adjacent duplicate characters recursively.

Examples: 

Input: s = "geeksforgeek"
Output: "gksforgk"
Explanation: g(ee)ksforg(ee)k -> gksforgk

Input: s = "abccbccba"
Output: ""
Explanation: ab(cc)b(cc)ba->abbba->a(bbb)a->aa->(aa)->"" (empty string)
'''

def removeUtil(s):
    result = ""
    n = len(s)
    i = 0
    while i < n:
                
        repeated = False
                
        while i + 1 < n and s[i] == s[i+1]:
                    
            repeated = True
            i+=1
                
            if not repeated:
                result += s[i]
            i+=1
        
        if n == len(result):
                return result
            
        return removeUtil(result)       
print(removeUtil(s="abccbccba"))
 