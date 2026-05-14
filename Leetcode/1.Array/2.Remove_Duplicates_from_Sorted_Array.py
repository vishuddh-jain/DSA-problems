def removeDuplicates(nums):
        l=0
        r=1
        for i in range(len(nums)-1):
            if nums[r] == nums[l]:
                r+=1
            else:
                nums[l+1] = nums[r]
                l+=1
                r+=1
        return l+1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))