class Solution:
    def search(self, nums: List[int], target: int) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i
        return d.get(target,-1)
        