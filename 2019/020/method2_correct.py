class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        expect_s = []
        
        if len(s) % 2 == 1:
            return False
        
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                expect_s.append(')')
            elif char == '[':
                expect_s.append(']')
            elif char == '{':
                expect_s.append('}')
            else:
                ##FIXED check empty list
                if len(expect_s) > 0: 
                    correct = expect_s.pop()
                    if correct == char:
                        pass
                    else:
                        return False
                else:
                    return False
        if len(expect_s) == 0:
            return True
        else:
            return False
        
        
