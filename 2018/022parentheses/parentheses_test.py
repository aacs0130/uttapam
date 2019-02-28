#!/usr/bin/env python
from parentheses import Solution

def main():
        #print "Welcome to test"
        s=Solution();
        nums = 2
        target = ''

        print "Case 1:%s of %s, t=%s" %(s.generateParenthesis(nums), nums, target)
        nums = 3
        target = ''
        print "Case 2:%s of %s, t=%s" %(s.generateParenthesis(nums), nums, target)
        nums = 4
        target = ''
        print "Case 3:%s of %s, t=%s" %(s.generateParenthesis(nums), nums, target)

if __name__ == "__main__":
    main()

