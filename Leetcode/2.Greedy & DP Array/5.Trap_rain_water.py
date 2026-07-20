# Brute force approach

def trap(height):
    n =len(height)

    water = 0
    for i in range(n):

        leftmax = 0
        rightmax =0 

        for left in range(i+1):
            leftmax = max(leftmax, height[left])

        for right in range(i, n):
            rightmax = max(rightmax, height[right])

        water = water + min(leftmax,rightmax) - height[i]
    return water

height = [4,2,0,3,2,5]
print(trap(height))

# Two Pointer Approach

def trapRainWater(heights):
    left = 0
    right = len(heights) -1
    
    left_max = heights[left]
    right_max = heights[right]
    
    water = 0
    
    while left < right:
        if left_max < right_max:
            left +=1
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
            
        elif right_max < left_max:
            right -=1
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
    return water
 
if __name__ == "__main__":
    user_input = input().strip().split()
    arr = list(map(int, user_input))
    print(trapRainWater(arr))