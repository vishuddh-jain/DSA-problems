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