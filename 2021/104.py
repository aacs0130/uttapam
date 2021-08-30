class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        test case 5
        input = [1, None, 2, None, 3, None, 4]
        output = 4
        
        test case 6
        input =[1,2,3,4,5,6,7]
        output = 3
        '''
        if root == None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            next_q = []
            for el in queue:
                if el.left:
                    next_q.append(el.left)
                if el.right:
                    next_q.append(el.right)
            queue = next_q
        return depth
