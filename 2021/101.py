from collections import defaultdict
from math import log, ceil
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def tree_to_dict(self, root):
        # Transfer the tree to a dictionary of index : value.
        """
        :type root: TreeNode
        :rtype: defaultdict
        key: index, value: value
        """
        value_dict = defaultdict(lambda : None)
        queue = [(0, root)]
        while(len(queue) > 0):
            index, node = queue.pop(0)
            value_dict[index] = node.val
            if node.left:
                queue.append( (index*2+1, node.left) )
            if node.right:
                queue.append( (index*2+2, node.right) )
        return value_dict

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Transfer the tree to a dictionary of index : value.
        value_dict = self.tree_to_dict(root)
        if len(value_dict) <= 1:
            return True          
        max_index = max(value_dict.keys()) 
        layer = ceil(log(max_index+2 , 2))
        for level in range(2, layer+1):
            start = 2**(level-1) - 1
            end = 2**level - 2
            #print('level %d, start %d, end %d' % (level, start, end))
            while start < end :
                if value_dict[start] != value_dict[end] :
                    return False
                start += 1
                end -= 1
        return True

if __name__ == '__main__':
    #test case 3
    root = TreeNode(val=1)
    
    s = Solution()
    print('root %s' % root.val)
    result = s.isSymmetric(root)
    print('result %s' % result)
    print('ans is True')

    #test case 6
    left = TreeNode(val=2)
    root = TreeNode(val=1, left=left)
    
    s = Solution()
    print('root %s' % root.val)
    result = s.isSymmetric(root)
    print('result %s' % result)
    print('ans is False')

