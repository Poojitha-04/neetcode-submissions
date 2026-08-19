class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di={}
        dif=0
        for i in range(len(nums)):
            di[nums[i]]=i
        for i in range(len(nums)):
            dif=target-nums[i]
            if di.get(dif,-1)>0 and i!=di.get(dif):
                return[i,di.get(dif)]


        