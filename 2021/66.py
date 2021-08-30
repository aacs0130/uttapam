class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        '''
        test case 6: 
            input = [9,9]
            output = [1,0,0]
        test case 7:
            input = [9,9,0,9,9]
            output = [9,9,1,0,0]
        '''

        add_one = digits
        add_one[-1] = add_one[-1]+1
        plus = 0
        for i in range(len(add_one)-1, -1, -1):
            #print('bf  i %d, add_one %s, plus %d' % (i, add_one, plus))
            add_one[i] = add_one[i] + plus
            if add_one[i] == 10:
                plus = 1
                add_one[i] = 0
            else:
                plus = 0 
                break
            #print('aft i %d, add_one %s, plus %d' % (i, add_one, plus))
            
        if plus == 1:
            add_one = [1]+add_one
        #print('result add_one %s, plus %d' % (add_one, plus))
            
        return add_one

