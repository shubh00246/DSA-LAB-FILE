def is_balanced(expression):
    stack = []
    opening = set("([{")
    closing = set(")]}")
    pair = {")": "(", "]": "[", "}": "{"}
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != pair[char]:
                    return False
            stack.pop()  
            
            return len(stack) == 0
        
        print(is_balanced("((()))"))  # True
       

    
