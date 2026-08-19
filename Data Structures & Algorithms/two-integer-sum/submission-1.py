class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            num=target-nums[i]
            if d.get(num,-1)>0 and i!=d.get(num):
                return [i,d.get(num)]

        