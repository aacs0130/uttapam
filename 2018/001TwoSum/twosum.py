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
                    try:
                        x = nums.index(copyList[i])
                        if copyList[i] == copyList[j]:
                            #Find the secound apperance of the value of copyList[i]
                            #print "duplicate"
                            y = x+1+nums[x+1:].index(copyList[j])
                        else:
                            y = nums.index(copyList[j])

                        #print "T: found %s" % ([x,y])
                        return [x,y]
                    except ValueError, e:
                        #the value is not in nums array
                        #print "T: value error of [%s]: %s" % ([x,y], e)
                        return None
                    break


        return None

