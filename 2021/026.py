class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ori_len = len(nums)
        if ori_len <=1:
            return ori_len
        '''
        i : the index after remove duplicate numbers
        j : the index we are checking now
        '''
        i = 0 
        #j = 1
        for j in range(1, ori_len):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i+=1
        return i+1
