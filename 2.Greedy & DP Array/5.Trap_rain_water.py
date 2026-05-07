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