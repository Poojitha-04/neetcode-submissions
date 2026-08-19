class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        for key,value in d.items():
            if value==1:
                return key



        