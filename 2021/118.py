class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        a[i,j] = 1 if j == 0 or j == i-1
        a[i,j] = a[i-1, j-1]+a[i-1, j] else
        """
        if numRows == 1:
            return [[1]]
        array = [None, [1]]
        for i in range(2, numRows+1):
            new_array = [1]
            last_array = array[i-1]
            for j in range(1, i):
                if j == i-1:
                    new_array.extend([1])
                else:
                    new_array.extend([last_array[j-1]+last_array[j]])
            array.append(new_array)
        return array[1:]
