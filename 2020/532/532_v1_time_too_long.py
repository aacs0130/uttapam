class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        ex4: [1,1,1,1] k = 0
            output =1
        '''
        nums.sort()
        if k < 0:
            return 0
        if k == 0:
            pairs = {}
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    pairs[nums[i]] = 1
            
            num = len(pairs.keys())
            return num
        else:
            pairs = {}
            num = 0
            for i in range(len(nums)-1):
                #print("i {} nums[i] {}".format(i,nums[i]))
                if i > 0 and nums[i] == nums[i-1]:
                    #print("continue")
                    continue
                expect = nums[i]+k
                if expect in nums:
                    #print("expect {} in nums".format(expect))
                    num+=1 
            return num
        
