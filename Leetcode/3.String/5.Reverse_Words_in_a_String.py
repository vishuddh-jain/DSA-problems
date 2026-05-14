# Using inbuilt function splitting and slicing

def Rev_words_in_string(s : str):
    s_list = s.split()
    rev_s_list = s_list[::-1]
    
    return " ".join(rev_s_list)

print(Rev_words_in_string(s = "  The   sky is blue")) 

