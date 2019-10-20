#This is test on the leetcode platform.
#https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        self.min_index = -1

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.array.append(x)
        print("Array after Push "+str(x) +" : "+ str(self.array))
        #compute min
        ##init min
        if self.min_index == -1:
            self.min_index = 0
            print("init min_index 0 for value"+ str(self.array[self.min_index]))
        elif x < self.array[self.min_index]:
            # x is new value
            self.min_index = len(self.array) -1 
            print("min_index : "+self.min_index+", for new min value"+ self.array[self.min_index])           

    def pop(self):
        """
        :rtype: None
        """
        #-1. be no element
        if self.min_index == -1:
            #dont need to do anything
            return None
        elif self.min_index == 0:
            self.min_index = -1 
            #FIXED forget to pop the element
            value = self.array.pop(len(self.array)-1)
            #FIXME
            print ("Pop at 0 value ", value)
            return None
        
        #0. compute min
        elif self.min_index == len(self.array) -1 :
            #find new min when index > 0
            self.min_index = 0            
            value = self.array[0]
            for i in range(1, len(self.array)-2):
                if self.array[i] < value:
                    self.min_index = i
        #1 pop element 
        value = self.array.pop(len(self.array)-1)
        print ("Pop at "+ str(len(self.array)-1) +" value " + value)

    def top(self):
        """
        :rtype: int
        """
        try :
            return self.array[-1]
        except IndexError:
            return None        

    def getMin(self):
        """
        :rtype: int
        """
        try :
            return self.array[self.min_index]
        except IndexError:
            #should be safe
            print("Weard getMin for array:"+ str(self.array) +"min"+ str(self.min_index))
            return None

        
'''
test case 0
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
expect
[None, None, None, -3, None, 0, -2]
'''

'''
test case 1 : pop when no element
#expect no error
["MinStack","push", "getMin","pop", "pop"]
[[],[-2],[],[],[]]
expect
[None, -2, None, None]
'''
'''
test case 2 : duplicate min
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-2],[],[],[],[]]
expect:
[None,None,None,-2,None,0,-2]
'''
'''
test case Wrong 1:
Input : ["MinStack","push","push","push","getMin","top","pop","getMin"]
Expect:[[],[-2],[0],[-1],[],[],[],[]]
Wrong Output: [null,null,null,null,-2,-1,null,-1]
[null,null,null,null,-2,-1,null,-2]

'''

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

