# Using inbuilt function sorted()

def h_index(citations):
    arr = sorted(citations)
    sort_arr = arr[::-1]
    count = 0
    for i in range(len(sort_arr)):
        if sort_arr[i] >= i+1:
            count+=1
    return count
        
print(h_index([3,0,6,1,2,4,5]))


# Brute force approach

def h_index(citations):
    n = len(citations)
    for h in range(n,-1,-1): # we are looping backwards so that we get the h that occured atleast h times
        count = 0
        
        for c in citations:
            if c >= h:
                count+=1

            if count >= h:
                return count
            
print(h_index([3,0,6,1,2,4,5,7,8,9]))