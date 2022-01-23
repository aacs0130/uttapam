class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, node):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        if not node:
            return None
        if node.left:
            output.extend(self.inorderTraversal(node.left))
        #Make the val to []
        output.extend([node.val])
        if node.right:
            output.extend(self.inorderTraversal(node.right))
        return output

if __name__ == '__main__':
    s = Solution()
    #test case 1
    node3 = TreeNode(val=3)
    node2 = TreeNode(val=2, left=node3)
    root = TreeNode(val=1, right=node2)

    print('test case 1')
    result = s.inorderTraversal(root)
    print('result %s' % result)
    print('ans is [1,3,2]')

    #test case 6
    node_list =[]
    for i in range(6):
        node_list.append(TreeNode(val=i))
    node_list[1].left = node_list[2]
    node_list[1].right = node_list[4]
    node_list[2].right = node_list[3]
    node_list[4].left = node_list[5]
    root = node_list[1]
    
    print('test case 6')
    result = s.inorderTraversal(root)
    print('result %s' % result)
    print('ans is [2, 3, 1, 5, 4]')
