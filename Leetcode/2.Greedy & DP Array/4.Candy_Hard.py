# my Approach Not working fine for diff test cases 

def candy(ratings):
    ratings.append(0)
    candy_sum = 0
    for student in range(len(ratings)-2):
        candy =1
        if (ratings[student] > ratings[student-1] or ratings[student] > ratings[student+1]):
            candy +=1
            candy_sum+=candy
        else:
            candy_sum +=1
    return candy_sum
ratings = [1,2,2]
print(candy(ratings))

# optimized approach

def Candy(ratings):
    n = len(ratings)
    candies = [1]*n

    # Left to right comparison
    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] +1

    # Right to left comparison
    for i in range(n-2,-1,-1): # to start loop with middle element
        if ratings[i] >ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1]+1)
    
    return sum(candies)

ratings = [1,0,2]
print(Candy(ratings))