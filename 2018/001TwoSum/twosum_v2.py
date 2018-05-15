#!/usr/bin/env python 
#@author Cicilia Lee
'''
Op1: sort array
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]... len??
        :type target: int... max??
        :rtype: List[int]
        """
        
        #print "T:nums %s target %d" %( nums, target)

        #calculate minus array
        copyList = nums[:]
        copyList.sort()
        minusList = copyList[:]
        arrayLen= len(nums)
        for index in range(arrayLen):
            minusList[index] = target - minusList[index]
        
        #print "T:minus List %s" % minusList

        for i in range(arrayLen):
            for j in range(i+1, arrayLen, 1):
                if copyList[i]==minusList[j]:
                    x = nums.index(copyList[i])
                    y = nums.index(copyList[j])
                    #print "T: found %s" % ([i,j])
                    return [x,y]
                    break

    
        return None


def main():
        #print "Welcome to test"
        '''
        Test case 1: 
        nums = [1,2,3,4], target = 7
            result =[2,3]
        Test case 2:
        nums = [1,2,3,4], target = 3
            result = [0,1]
        Test case 3:
        nums = [1,3,9,27,81] target = 36
            result = [2,3]
        Test case 4:
        nums = [1,3,9,27,81] target = 82
            result = [0,4]
        '''
        s=Solution();
        nums = [1,2,3,4]
        target = 7

        print "Case 1:%s of %s, t=%s" %(s.twoSum(nums, target), nums, target)
        target = 3
        print "Case 2:%s of %s, t=%s" %(s.twoSum(nums, target), nums, target)
        nums = [1,3,9,27,81]
        target = 36
        print "Case 3:%s of %s, t=%s" %(s.twoSum(nums, target), nums, target)
        target = 82
        print "Case 4:%s of %s, t=%s" %(s.twoSum(nums, target), nums, target)

if __name__ == "__main__":
    main()

