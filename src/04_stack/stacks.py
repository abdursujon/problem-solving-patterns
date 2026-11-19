class Stack:
    #======== Easy Leetcode ==========#
    # 20. Valid parenthesis
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b=='(' or b=='{' or b=='[':
                stack.append(b)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if b==')' and top!='(':
                    return False
                elif b==']' and top !='[':
                    return False 
                elif b=='}' and top !='{':
                    return False 
            
        return len(stack) == 0
