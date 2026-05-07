# my Approach Not working fine for diff test cases 

def Candy(ratings):
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
print(Candy(ratings))