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
        n = len(heights)

        for i in range(n + 1):

            current_height = 0 if i == n else heights[i]

            while stack and current_height < heights[stack[-1]]:

                h = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area

print(largestRectangleArea(heights=[2,1,5,6,2,3]))