# class Solution:
def removeElement(nums, val):
        result = []

        for i in nums :
            if i == val :
                pass
            else :
                result.append(i)

        for i in range(len(result)):
            nums[i] = result[i]

        return len(result)
print(removeElement([3,2,2,3], 3))