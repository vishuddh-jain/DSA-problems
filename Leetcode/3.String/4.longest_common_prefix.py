def LongestCommonPrefix(strs):
    if strs is None:
        return ""
    
    first = strs[0]

    for i in range(len(first)):
        for word in strs[1:]:

            if i >= len(word) or word[i] != first[i]:
                return first[:i]
            
    return first

strs = ["flower","flow","flight"]
print(LongestCommonPrefix(strs))