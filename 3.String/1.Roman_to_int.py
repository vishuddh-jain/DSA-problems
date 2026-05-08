def Roman_to_int(s):
    dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "c" : 100,
        "D" : 500,
        "M" : 1000
    }

    val = 0
    i = 0

    while i < len(s):
        if i+1 < len(s) and dict[s[i]] < dict[s[i+1]]:
            val += dict[s[i+1]] - dict[s[i]]
            i+=2
        else:
            val += dict[s[i]]
            i+=1
    return val

s = 'VI'
print(Roman_to_int(s))
