def NextGreaterElement(a):
    n= len(a)
    ans = [-1] *n
    
    stack = []
    
    for i in range(n-1, -1,-1):
        while stack and stack[-1] <= a[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(a[i])
        
    return ans
a = [1,3,2,4]
print(NextGreaterElement(a)) 