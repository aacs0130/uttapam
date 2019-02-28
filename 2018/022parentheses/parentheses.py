class Solution(object):

    calc_dict = {0:[""], 1:["()"]}

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        : it's '(' or ')'
        """
        """
        Q1" is n > 0?
        Q2: what is upper bound of n
        test case:
        gp (1)  = 1
        gp(2)=2
        gp(3)=5 = gp(2)*2+1
        gp(4)=15 = uniq(  gp(3)*gp(2)+gp(2)*gp(2) )
        gp(n)= uniq(gp(n-1)*3+gp(n-2)^2 +qp(n-4)^2+ ...)
    n = 1
        ans = ["()"]
        cnt = 1

        n = 2
        ans = [ "(())", "()()"]
        cnt = 2

        n = 3
        ans = [
      "((()))", // first all (,
      "(()())", //( , then n = 2, then )
      "(())()",
      "()(())", // (), then n = 2
      "()()()"
        ]
        cnt = 5

        n = 4
        cnt = 2*5+1 = 11(X)
            15

        """
        if n < 1:
            self.calc_dict[0] = [""]
            return self.calc_dict[0]
        elif n == 1:
            self.calc_dict[1] = ["()"]
            return self.calc_dict[1]
        #elif n == 2:
        #    self.calc_dict[2] = ["(())", "()()"]
        #    return self.calc_dict[2]
        elif self.calc_dict.has_key(n):
            return self.calc_dict[n]
        else:
            result_dict = {}
            str1 = ""
            for i in range(0, n):
                str1 = "("+str1+")"
            result_dict[str1] = ''

            #n-1
            previous_list = self.generateParenthesis(n-1)
            for i in range(0, len(previous_list)):
                if len(previous_list[i]) == 0:
                    continue
                result_dict["()"+previous_list[i]] = ''
                result_dict["("+previous_list[i]+")"] = ''
                result_dict[previous_list[i]+"()"] = ''

            # even number
            for j in range(2, n):
                j_list = self.generateParenthesis(j)
                previous_list = self.generateParenthesis(n-j)
                #j list X n-j list

                for i in range(0, len(previous_list)):
                    if len(previous_list[i]) == 0:
                        continue
                    for x in range(0, len(j_list)):
                        if len(j_list[x]) == 0:
                            continue
                        result_dict[previous_list[i]+j_list[x]] = ''

            self.calc_dict[n] = sorted(result_dict.keys())
            return sorted(result_dict.keys())

