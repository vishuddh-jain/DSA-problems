'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4'''

def largestRectangleArea(heights):
        
        stack = []
        max_area = 0

        for i in range(len(heights)+1):

            current_height = 0 if i == len(heights) else heights[i]

            while stack and current_height < heights[stack[-1]]:

                left = stack.pop()

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, heights[left] * width)

            stack.append(i)

        return max_area

print(largestRectangleArea(heights=[2,1,5,6,2,3]))