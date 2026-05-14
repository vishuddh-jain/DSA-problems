# (Replace spaces with %20)

def Urlify(s):
    s_list = list(s)
    for i in range(len(s)):
        if s_list[i] == " ":
            s_list[i] = "%20"
    return ''.join(s_list)

s = "ab cd"            
print(Urlify(s))