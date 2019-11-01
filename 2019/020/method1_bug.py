class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #FIX ONE correct order
        #11/1 21:00 
        if (len(s) % 2 == 1):
            return False
        
        big = 0
        mid = 0
        small = 0
        expect_stack = []
        #valid = True
        
        ##'(', ')', '{', '}', '[' and ']'
        
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                small +=1
                expect_stack.append(')')
            elif char == ')':
                correct = expect_stack.pop([index=-1])
                if correct != char:
                    return False
                small -=1
                if small < 0:
                    return False
            elif char == '[':
                mid +=1
                expect_stack.append(']')
            elif char == ']':
                mid -=1
                if mid <0:
                    return False
            elif char == '{':
                big +=1
                expect_stack.append('}')

            elif char == '}':
                big -=1
                if big < 0:
                    return False
            else:
                return False
            
        if (big ==0) and (mid == 0) and (small == 0):
            return True
        else:
            return False
        
        
        
