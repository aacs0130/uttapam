#!/usr/bin/env python
from twosum import Solution

def main():
        #print "Welcome to test"
        s=Solution();
        nums = [3,3]
        target = 7

        print "Case 1:%s of %s, t=%s" %(s.twoSum(nums, target), nums, target)
        target = 6
        print "Case 2:%s of %s, t=%s" %(s.twoSum(nums, target), nums, target)
        nums = [1,3,9,27,81]
        target = 36
        print "Case 3:%s of %s, t=%s" %(s.twoSum(nums, target), nums, target)
        nums = [2,7,11,15]
        target = 9
        print "Case 4:%s of %s, t=%s" %(s.twoSum(nums, target), nums, target)

if __name__ == "__main__":
    main()

