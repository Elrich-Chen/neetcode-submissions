class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        latest = 0

        for c in tokens:
            try:
                c = int(c)
                stack.append(int(c))
            except:
                second = stack.pop()
                first = stack.pop()
                if c == "+":
                    stack.append(first+second)
                elif c == "*":
                    stack.append(first*second)
                elif c == "-":
                    stack.append(first-second)
                else:
                    stack.append(int(first/second))
        
        return int(stack.pop())