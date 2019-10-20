# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        #1. scan to get A array and B array
        head = headA
        arrA = []
        while head.next !=None:
            arrA.append(head.val)
            head=head.next
        arrA.append(head.val)
        print('arrayA {}').format(arrA)

        head = headB
        arrB = []
        while head.next !=None:
            arrB.append(head.val)
            head=head.next
            
        arrB.append(head.val)
        print('arrayB: {}').format(arrB)

        #2. compare A and B from tail and get the first intersect value and, HeadShort,  skip_no, if no value return None

        i = len(arrA) -1
        j = len(arrB) - 1
        while( i>=0 and j>=0):
            if arrA[i]==arrB[j]:
                i=i-1
                j=j-1
            else:
                break
        i=i+1
        j=j+1
        '''
        if i < j:
            headShort = headA
            skip = i
            print('short is A and skip is {}'.format(skip))
        else:
            headShort = headB
            skip = j          
            print('short is B and skip is {}'.format(skip))
            
        #3. find nodeInter from headShort by skip_no
        node = headShort
        while node.next != None and skip >0:
            node = node.next
            skip -=1
        '''
        #check node with same value are the same node
        nodeA = headA
        while nodeA.next != None and i >0:
            nodeA = nodeA.next
            i -=1

        nodeB = headB
        while nodeB.next != None and j >0:
            nodeB = nodeB.next
            j -=1

        while (nodeA != nodeB):
            nodeA = nodeA.next
            nodeB = nodeB.next
            
        
        print('the intersect node is {}'.format(nodeA))
        return nodeA
        
        ## return nodeInter 
'''
ex1:
1. A=[4,1,8,4,5]
B = [5,0,1,8,4,5]
i = 4 3 2 1不同
ex4:
0
[]
[]
0
0
return None
'''        
