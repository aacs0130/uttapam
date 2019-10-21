class Solution(object):
    def get_max(self, a, b):
        if a > b:
            return a
        else:
            return b
        
    def sellAtMax(self, array):
        leng = len(array)
        if leng < 2:
            return 0
        
        max_v = array[-1]
        min_v = array[0]
        for i in range(1, leng-1):
            if array[i] < min_v:
                min_v = array[i]
        #print('sellAtMax array {} and min: {}, max: {}'.format(array, max_v, min_v) )
                
        return max_v - min_v

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''

        #O(N^2)
        XX
        for i in range(len(List)):
            if I buy at day i+1:
                for j in range(i+1, len(List))
                array is what's the profit I sell everyday 
            keep the max value                
        '''
        #print('process prices array {}'.format(prices)) 
        #0 if len(prices) < 2 return 0
        if len(prices) < 2:
            print('leng < 2')
            return 0
        #0.1 if len(prices) == 2, compare
        elif len(prices) == 2:
            #print('leng == 2')
            if prices[1] > prices[0]:
                #print('return {}'.format(prices[1] - prices[0]))
                return prices[1] - prices[0]
            else:
                return 0

        #1 find max O(n)
        max_v = prices[0]
        max_i = 0
        #desc_cnt = True
        for i in range(1, len(prices)):
            if prices[i] > max_v:
                max_v = prices[i]
                max_i = i
            #FIXME Worse case, descending
            #if desc_cnt and prices[i] > prices[i-1]:
                #desc_cnt = False
                
        #if desc_cnt == True:
            #return 0
        #print('max i {} max v {}'.format(max_i, max_v))
              
        #2 maxProfit(array) = get_max(sellAtMax(array[,max_index+1]), maxProfit(array[max_index+1, ]))    O(n)
        profit = self.get_max( self.sellAtMax(prices[: max_i+1]), self.maxProfit(prices[max_i+1:]) )
        return profit
        
        '''        
        ex1:
        max = 7, max_index = 0
        maxPro = max(sellAtMax(array[,0]), max(Profit(array[1,])))
        =maxPro(array[1,5,3,6,4])
        
        maxPro(array[1,5,3,6,4])
        max = 6, max_index = 3
        maxPro = max(sellAtMax(arrya[0,3]), maxPro(array[4,4]))
        = sellAtMax(arrya[0,3]) = 6-1 = 5
        
        '''
        
        
                
        
'''
Thinking

Ex 3:
Input: [1,2,3,4]
Output:3

ex4 :
Input:[]
output: 0, no transaction

ex5:
input:[1,2]
output: 1

ex6:
input:[2,1]
output: 0

'''
