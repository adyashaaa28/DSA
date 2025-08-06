#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

class Solution:  
    def isValid(self, s: str) -> bool:  
        bracket_map = {')': '(', '}': '{', ']': '['}  
        stack = []  
        for char in s:  
            if char in bracket_map.values():   
                stack.append(char)  
            elif char in bracket_map.keys():    
                if stack == [] or stack.pop() != bracket_map[char]:  
                    return False  
        return stack == []  
 