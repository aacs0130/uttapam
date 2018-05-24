#!/usr/bin/env python
class Solution(object):
    debug = True
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #x> root^2
        sq = x
        upper_bound = sq/4+1
        lower_bound = 0
        root = (upper_bound+1)/2
        self.prt("x %d, root %d, upper %d", (x, root, upper_bound))


        while (upper_bound>lower_bound):
            if root*root <= sq :
                if (root+1)*(root+1)>sq:
                    return root
                else:
                    if upper_bound == root:
                        break
                    lower_bound = root+1
                    root = (root+upper_bound+1)/2
            else:
                if root == lower_bound :
                    break
                upper_bound = root -1
                root = (root+lower_bound)/2

        self.prt("After compute root %d", (root))
        if root > 0:
            return root
        else:
            return 0

        return root

    def prt(self, string, values):
        if self.debug:
            print string % values

def main():
    #'''
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
    #'''
    x = 2147395599
    result = Solution().mySqrt(x)
    print "sqrt of [%d] Expect [46339], is [%d]" %(x, result)

if __name__ == "__main__":
    main()
