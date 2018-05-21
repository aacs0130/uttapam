class Solution(object):
    debug = False
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        """
        dict_map: number: letters
        result_list:[]
        Input digits
        for every digit:
            add one letter to every element in result list

        """
        #key: number, value: letters
        dict_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
                "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result_list = []

        self.sprint("Get digits %s, type %s", (digits, type(digits)))
        if len(digits) <1:
            return []
        #O(N^3)
        for i in range(len(digits)):
            if digits[i] in dict_map:
                letters = dict_map[digits[i]]
                self.sprint("Get letter %s, type: %s, from digit %s", (letters, type(letters),
                    digits[i]))
                old = result_list[:]
                result_list = []
                for k in range(len(letters)):
                    if len(old) == 0:
                        result_list.append(letters[k])
                        self.sprint("letter[k]: %s, result: %s", (letters[k], result_list))
                    else:
                        for j in range(len(old)):
                            result_list.append(old[j]+letters[k])
                        self.sprint("letter[k]: %s, result: %s", (letters[k], result_list))
                
                self.sprint("i %d, digit %s: result%s", (i, digits[i], result_list))
        
        return result_list

    def sprint(self, string, values):
        if self.debug == True:
            print string % values

def main():
    digits = ""
    result = Solution().letterCombinations(digits)
    print "\nCase 1:digits: %s, len(result):%d\n\t result:%s"% (digits,len(result), result)

    digits = "23"
    result = Solution().letterCombinations(digits)
    print "\nCase 2:digits: %s, len(result):%d\n\t result:%s"% (digits,len(result), result)

    digits = "79"
    result = Solution().letterCombinations(digits)
    print "\nCase 3:digits: %s, len(result):%d\n\t result:%s"% (digits,len(result), result)

    digits = "222"
    result = Solution().letterCombinations(digits)
    print "\nCase 4:digits: %s, len(result):%d\n\t result:%s"% (digits,len(result), result)

if __name__ == "__main__":
    main()
