def earliestRepeatingChar(s):
    dict = {}
    
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
        if dict[i] == 2:
            return i
    return "-1" 
        
s = "geeksforgeeks"
print(earliestRepeatingChar(s))