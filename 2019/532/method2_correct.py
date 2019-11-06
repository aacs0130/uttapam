class Solution(object):
    def findPairs(self, nums, k):
        #Method 2, check solution, O(n)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        ex4: [1,1,1] k = 0, out = 1
        ex5: [1,2,2,2] k = 0, out = 1
        '''
        
        if nums == None or len(nums) < 2 or k < 0 :
            return 0
        
        nums.sort()
        right = 1
        left = 0
        pairs_cnt = 0
        leng_nums = len(nums)

        #deal with k == 0 => ok
        #O(n)
        while (right < leng_nums):
            diff = nums[right] - nums[left] 
            if diff == k :
                pairs_cnt +=1
                right+=1
                left +=1
            elif diff < k:
                right+=1
            else: # diff >k
                left+=1
                
            # skip duplicate
            while right > 0 and right < leng_nums and nums[right] == nums[right-1]:
                right+=1
            
            while left > 0 and left < leng_nums and nums[left] == nums[left-1]:
                left+=1
            
            if left == right:
                right +=1
            elif left > right:
                break
        
        return pairs_cnt
        
