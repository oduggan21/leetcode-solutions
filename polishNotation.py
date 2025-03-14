class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok.lstrip('-').isdigit(): 
                stack.append(int(tok)) 
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if tok == '+':
                    stack.append(num1 + num2)
                elif tok == '-':
                    stack.append(num1 - num2)
                elif tok == '*':
                    stack.append(num1 * num2)
                elif tok == '/':
                    stack.append(int(num1 / num2)) 
        return stack.pop()

