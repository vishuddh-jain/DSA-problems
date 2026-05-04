def h_index(nums):
    arr = sorted(nums)
    sort_arr = arr[::-1]
    count = 0
    for i in range(len(sort_arr)):
        if sort_arr[i] >= i+1:
            print(sort_arr[i])
            count+=1
    return count
        
print(h_index([3,0,6,1,2,4,5]))

