class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        result = dict[s[-1]]
        for i in range(len(s)-1):
            if dict[s[i]] < dict[s[i+1]]:
                result -= dict[s[i]]
            else:
                result += dict[s[i]]
        return result
