class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range (len(numbers)):
            d[numbers[i]]=i
        for i in range(len(numbers)):
            num=target-numbers[i]
            if d.get(num,-1)>=0 and d.get(num)!=i:
                return([i+1,d.get(num)+1])
        