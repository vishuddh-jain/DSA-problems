def thirdMax(nums):
        great_ele = max(nums)
        s_g , t_g = float('-inf'), float('-inf')

        for i in range(len(nums)):
            if nums[i] > s_g and nums[i] < great_ele:
                s_g = nums[i]
    
        for i in range(len(nums)):
            if nums[i] > t_g and nums[i] < s_g:
                t_g = nums[i]
        
        
        if t_g == float('-inf'):
            return s_g
        else:
            return t_g
            
print(thirdMax(nums =[1,2]))