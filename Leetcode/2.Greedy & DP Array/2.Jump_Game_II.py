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

# greedy approach 

def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        # when we reach end of current range
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps

nums = [2,3,1,1,4]
print(jump(nums))