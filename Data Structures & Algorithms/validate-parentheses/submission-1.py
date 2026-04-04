class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                prev = stack.pop()
                if ((prev == '(' and char == ')') or (prev == '{' and char == '}') or
                    prev == '[' and char == ']'):
                    continue
                else:
                    return False
        
        return len(stack) == 0
