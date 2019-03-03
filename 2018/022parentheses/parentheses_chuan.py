class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        def dfs(stack, n, left):
            if len(stack) == 2*n:
                self.ans.append(''.join(stack))
                return
            if left < n:
                stack.append('(')
                dfs(stack, n, left+1)
                stack.pop()
                
            if len(stack) < 2 * left:
                stack.append(')')
                dfs(stack, n, left)
                stack.pop()
        
        dfs([], n, 0)
        return self.ans
            