#!/env/bin/python 
'''
Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you'd like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!
'''


Q: You have an array of N integers. There are M contiguous segments that are sorted within the segment, but the whole array is not sorted. N >> M. How to produce a sorted version of this array?
data array = [1,3,5    ,2,4,6,    0, 2]
segment array = [0, 3, 6]
O(nlogn)
merge sort

0,3 6
1,3,5     2,4,6
1,2,3, 4, 5, 6  
O(nlogn)

0 3 6 n=3
mer0 3
mer03 6


size of data array = N
number of segments = M
O(MlogM)

**done(mergeit())
howmanymerge()

O(1)*logm
logm



[0, 2, 1, 3]
[0, 2]

class Solution(Object):
    def mergeit(self,dataList, segmentList, segmentTail):
        dataLen = len(dataList) #4
        segLen = len(segmentList)
        datalistcopy = dataList[:]
        if segLen == 2:
            i = segmentList[0]
            j = segmentList[1]
            k = segmentList[0]
            i_tail =segmentTail[0]
            j_tail =segmentTail[1]
            while (i < i_tail and j<j_tail):
                if datalistcopy[i]<= datalistcopy[j]:
                    dataList[k] = datalistcopy[i]
                    i +=1
                else:
                    dataList[k] = datalistcopy[j]
                    j +=1
                
                k +=1
            #copy the last that not compare
            if i< i_tail: #i remains
                while(i< i_tail):
                    datalist[k]= datalistcopy[i]
                    i+=1
                    k+=1
            else:
                while(j< j_tail):
                    datalist[k]= datalistcopy[j]
                    j+=1
                    k+=1
                
                    
        while segLen > 2: 
            frontseg = segmentList[0, segLen/2]
            fronttailseg = segmentTail[0, segLen/2]

            mergeit(dataList, frontseg, fronttailseg)

            backseg = segmentList[segLen/2+1, segLen]
            backtailseg = segmentTail[segLen/2+1, segLen]

            mergeit(dataList, backseg, backtailseg)
            
                
        
        
    def mergesort(self, dataList, segmentList):
        '''data array = [1,3,5    ,2,4,6,    0, 2]
            segment array = [0, 3, 6]
        '''
        
        dataLen = len(dataList) #4
        segLen = len(segmentList) #2
        segmentTail = segmentList[1:]+ segLen

        if segLen == 2:
            mergeit(dataList, segmentList)
                
        while segLen > 1:
            frontseg = segmentList[0, segLen/2]
            mergeit(dataList, frontseg)
            backseg = segmentList[segLen/2+1, segLen]
            mergeit(dataList, backseg)
            
        
        
        
        
        
        
    
    def prt(self, sting, values):
        print string @values 
    
    def __init__(self):
        self.prt("haha %s", oh)
    
        
def main():
    int temp = 123

    
if __name__ = '__main__':
    main()
           i = segmentList[0]

