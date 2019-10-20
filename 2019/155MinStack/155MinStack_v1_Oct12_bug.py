#This is test on the leetcode platform.
#https://leetcode.com/problems/min-stack/

class MinStack(object):

    #check the stack is empty or not 
    #check the min value
    def __init__(self):
        """
        initialize your data structure here.
        """
        #top_index have element
        self.array = []
        self.top_index = -1
        self.min_index = -1
        self.min_value = None
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        ##push value in stack
        self.top_index += 1
        self.array.append(x)
        
        ##check min_value
        #FIXED: for first element
        if self.min_index == -1:
            self.min_index = 0
            self.min_value = x
        elif x < self.min_value:
            self.min_value = x
            self.min_index = self.top_index

    def pop(self):
        """
        remove element, don't need to return
        """
        #check zero
        if self.top_index == -1:
            pass
        
        value = self.array[self.top_index]
        self.top_index -= 1
        
        ## check min_value
        if self.min_value == value:
            #FIXME min_value can be repeated 
              
            self.min_value = self.array[0]
            self.min_index = 0
            for i in range(1, self.top_index):
                if self.array[i] < self.min_value:
                    self.min_value = self.array[i]
                    self.min_index = i
        #return value
        
    def top(self):
        """
        :rtype: int
        """
        if self.top_index > -1:
            return self.array[self.top_index]
        else :
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_index > -1:
            return self.min_value
        else:
            return None

##test case 0
'''
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
[]
[-2]
[-2, 0]
[-2, 0, -3]

top 0, 1, 2
min 0, 0, 2
min_value -2, -2, -3
getMin() 
'''

##test case 1
##pop() when no element
'''

'''
##test case 2
##get_min when no element

##test case 3
##top() when no element 

        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
