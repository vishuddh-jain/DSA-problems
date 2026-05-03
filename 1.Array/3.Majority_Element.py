def majorityElement(nums):
        dict = {}
        key, max = 0, 0
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for k in dict:
            val = dict[k]
            if val >= max:
                max = val
                key = k
        return key
print(majorityElement([3,2,3]))