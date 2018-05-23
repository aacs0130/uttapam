#!/usr/bin/env python
class Solution(object):
    debug = True
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sq = x
        upper_bound = sq*sq/4+1
        root = upper_bound
        while (root*root > sq):
            root -= 1

        if root > 0:
            return root
        else:
            return 0

    def prt(self, string, values):
        if self.debug:
            print string % values

def main():
  
    x = 0
    result = Solution().mySqrt(x)
    print "sqrt of [%d] Expect [0], is [%d]" %(x, result)
    x = 1
    result = Solution().mySqrt(x)
    print "sqrt of [%d] Expect [1], is [%d]" %(x, result)
    x = 3
    result = Solution().mySqrt(x)
    print "sqrt of [%d] Expect [1], is [%d]" %(x, result)
    x = 4
    result = Solution().mySqrt(x)
    print "sqrt of [%d] Expect [2], is [%d]" %(x, result)
    x = 82
    result = Solution().mySqrt(x)
    print "sqrt of [%d] Expect [9], is [%d]" %(x, result)
if __name__ == "__main__":
    main()
