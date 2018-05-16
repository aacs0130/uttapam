#!/usr/bin/env python 
#@author Cicilia Lee

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]... len??
        :type target: int... max??
        :rtype: List[int]
        """
        #print "T:nums %s target %d" %( nums, target)

        #calculate minus array
        minusList = nums[:]
        arrayLen= len(nums)
        for index in range(arrayLen):
            minusList[index] = target - minusList[index]
        
        #print "T:minus List %s" % minusList

        for i in range(arrayLen):
            for j in range(i+1, arrayLen, 1):
                if nums[i]==minusList[j]:
                    #print "T: found %s" % ([i,j])
                    return [i,j]
                    break

    
        return None

