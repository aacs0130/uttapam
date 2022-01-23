class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #copy solution two-pointer
        leng = len(numbers)
        index1 =0
        index2 = leng -1
        while(index1 < index2):
            sum = numbers[index1]+numbers[index2]
            if sum == target:
                return [index1+1, index2+1]
            elif sum < target:
                index1+=1    
            else:
                # sum > target:
                index2-=1
        return []
