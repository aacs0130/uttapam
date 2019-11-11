class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        #METHOD 1
        count alphabet of s and t
        use dictionary 
        dict[char] = count
        1. compare leng and check if s == None or t == None 
        2. count s and t 
        3 compare 2 dict, same return true 
        
        #IMPROVE use one dict, s to +, t to -
        '''
        '''
        test case 3: 
        s = None, t = "s"
        out: False
        test case 4:
        s = "abc", t = "a"
        out:False
        test case 5:
        s = "abc", t = "aba"
        out:False
        
        '''
        if s == None or t == None:
            return False
        if len(s) != len(t):
            return False
        if len(s) == 0 and len(t) == 0:
            return True
        
        #count s and t
        leng = len(s)
        dict_s = {}
        dict_t ={}
        
        #O(n)
        for i in range(leng):
            dict_s[ s[i] ] = dict_s.get(s[i], 0) +1
            dict_t[ t[i] ] = dict_t.get(t[i], 0) +1
        
        #compare two dict
        #same return True
        keys = dict_s.keys()
        keys_t = dict_t.keys()
        if len(keys) != len(keys_t):
            return False

        #O(1), only 26 alphabet        
        for key in keys:
            if dict_s.get(key, 0) != dict_t.get(key, 0):
                return False
        
        return True
         
