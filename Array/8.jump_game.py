def canJump(nums):
    max_rea = 0
    for i in range(len(nums)):
        if i > max_rea: # checking this max_rea with "i" because if i > max_rea then how can that no./max_reach surpass the index 
            return False
        max_rea = max(max_rea, i+nums[i])

        if max_rea >= len(nums)-1:
            return True
        return True

nums= [3,2,1,0,4]
print(canJump(nums))
    