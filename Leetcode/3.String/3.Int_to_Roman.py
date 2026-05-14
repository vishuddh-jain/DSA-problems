# Optimized approach with time complexity 0 using list approach 
def IntToRoman(num):
    my_dict = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

    for value, symbol in my_dict:

        while num >= value:
            result+=(symbol)
            num -= value

    return (result)

num = 490
print(IntToRoman(num))


# basic string addition approach
def intToRoman(num):
    my_dict = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

    for value, symbol in my_dict:

        while num >= value:
            result+=(symbol)
            num -= value

    return (result)

num = 490
print(intToRoman(num))