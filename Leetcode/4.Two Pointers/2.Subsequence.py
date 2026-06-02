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