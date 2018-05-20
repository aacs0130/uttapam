#!/usr/bin/env python

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]... len??
        :type target: int... max??
        :rtype: List[int]
        """
        """
        Idea: map_index = {key:value}
            key: target - nums[index]
            value: index
        """
        #print "T:nums %s target %d" %( nums, target)

        if (nums == None or len(nums)<=1):
            #nums are wrong
            #print "nums are wrong"
            return []

        map_index = {}
        for i in range(len(nums)):
            if nums[i] in map_index:
                #print "found [%d, %s]" % (map_index[nums[i]], i)
                return [map_index[nums[i]], i]
            else:
                #print "assign {%d:%d}" % (nums[i], i)
                map_index[target - nums[i]] = i

        #print "Not found"
        return []

