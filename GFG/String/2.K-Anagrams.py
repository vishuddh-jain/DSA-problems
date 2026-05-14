def isKAnagram(s1,s2,k):
    
    if len(s1) != len(s2):
        return "No"
    
    count = 0
    s2_list = list(s2)
    
    for i in s1:
        if i in s2_list:
            s2_list.remove(i)
        else:
            count+=1
    
    if count <= k:
        return "Yes"
    else:
        return "No"
    
print(isKAnagram(s1="anagram", s2='grammar', k=3))