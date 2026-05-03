# basic recursion approach

def minJumps(nums, i=0):
    # reached end
    if i >= len(nums) - 1:
        return 0
    
    # if stuck (not needed here as problem guarantees reachability
    min_steps = float('inf')
    
    for jump in range(1, nums[i] + 1):
        steps = 1 + minJumps(nums, i + jump)
        min_steps = min(min_steps, steps)
    
    return min_steps
nums = [2,3,1,1,4]
print(minJumps(nums, i =0))