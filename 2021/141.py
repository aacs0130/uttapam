# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #is the value unique? No
        if head == None or head.next == None:
            return False
        queue = [head]
        while head.next:
            head = head.next
            if head in queue:
                return True
            else:
                queue.append(head)
        return False
