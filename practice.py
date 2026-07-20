# def solve(nums, k):
#     n = len(nums)
#     k = k % n
    
#     rotated_arr = nums[-k:] + nums[:-k]
    
#     print(rotated_arr)    
    
# if __name__ == "__main__":
#     user_input = input().strip().split()
    
#     n = int(user_input[0])
#     k = int(user_input[1]) 
    
#     arr = list(map(int, input().strip().split()))
#     print(solve(arr, k))

def evaluate_expression(expression):
    stack = []
    
    tokens = expression.split()
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(token)
        
        else:
            if len(stack) < 2:
                return "Invalid expression" 
            val2 = int(stack.pop())
            val1 = int(stack.pop())
            
            if token == "+":
                stack.append(val1+val2)
            elif token == "-":
                stack.append(val1-val2)
            elif token == "*":
                stack.append(val1*val2)
            elif token == "/":
                stack.append(int(val1/val2))
            else:
                return "Invalid Operator"
            
    return stack[0] if len(stack) == 1 else "Invalid Expression"

if __name__ == "__main__":
    user_input = input().strip()
    if user_input:
        result = evaluate_expression(user_input)
        print(result)
    