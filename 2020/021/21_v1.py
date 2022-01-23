#python 3 code

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
FIXME
#Not check implement 
def printd(object, format = None):
    printFlag = True

    if printFlag = True:
        if format == None:
            print(object)
        else:
            print(format, object)
'''

def printList(list1):
    outStr = None
    printFlag = True
    #Init outStr
    if list1 != None:
        outStr = str(list1.value)+" => "
        list1 = list1.next

    while (list1 != None):
        outStr = outStr+str(list1.value)+" => "
        list1 = list1.next

    if printFlag == True:
        print("List:"+outStr)

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode   
        :rtype: ListNode
        """
        '''
        Pointer pa, pb
        pointer can change the thing it point to
        List change it's next
        '''
        pa = l1
        pb = l2
        #make one more for pointer
        Now = None
        Out = None
        LastInsertFrom = None
        print("Init:l1 and l2")
        printList(l1)
        printList(l2)

        while (pa.next !=None and pb.next != None):
            if pa.value < pb.value:
                if Out == None: #see the first time
                    Out.next = pa
                Now = pa
                pa = pa.next
                LastInsertFrom = 'A'
            elif pa.value > pb.value:
                if Out == None: #see the first time
                    Out.next = pb
                Now = pb
                pb = pb.next
                LastInsertFrom = 'B'
            else:# pa.value == pb.value
                if LastInsertFrom == 'A':
                    if Out == None: #see the first time
                        Out.next = pa
                    Now = pa
                    pa = pa.next
                    #LastInsertFrom = 'A'
                elif LastInsertFrom == 'B':
                    if Out == None: #see the first time
                        Out.next = pb
                    Now = pb
                    pb = pb.next
                    #LastInsertFrom = 'B'
                #LastInsertFrom == None
                else:
                    #Will init it next round
                    EqualPA = pa
                    EqualPB = pb
                    while(EqualPA !=None and EqualPB !=None and (EqualPA.value == EqualPB.value)):
                        EqualPA = EqualPA.next
                        EqualPB = EqualPB.next
                    #include both None
                    if EqualPA == None:
                        LastInsertFrom = 'A'
                    elif EqualPB == None:
                        LastInsertFrom = 'B'
                    elif EqualPA.value > EqualPB.value:
                        LastInsertFrom = 'A'
                    else:
                        LastInsertFrom = 'B'
            print("=====\nNow value A:[%s]\nB:[%s]\nOut list:", % (pa.value, pb.value))
            printList(Out.next)        
            #End of while          


        #Insert the remaining lists
        if pa.next !=None:
            Now.next = pa
        else:
            Now.next = pb



        print("=====Final=====")        
        printList(Out.next)        

        #make one more for pointer
        return Out.next

