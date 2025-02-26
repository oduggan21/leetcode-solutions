class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final_list = []
        stack = []

    
        def backTracking(stack,left,right):
            if right == n:
                string_val = ''.join(val for val in stack)
                final_list.append(string_val)
                return 
            if left < n:
                stack.append('(')
                backTracking(stack, left + 1, right)
                stack.pop()
            if right < n and right < left:
                stack.append(')')
                backTracking(stack, left, right + 1)
                stack.pop()

        backTracking(stack, 0,0)
        return final_list
