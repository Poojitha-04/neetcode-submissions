class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            d[numbers[i]]=i+1
        print(d)
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if d.get(diff,-1)>0 and d[diff]!=i:
                return [d.get(numbers[i]),d.get(diff)]
        