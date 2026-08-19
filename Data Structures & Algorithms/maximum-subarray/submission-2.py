class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=(-math.inf)
        current=0
        for i in nums:
            current+=i
            print(current)
            if maxsum<current:
                maxsum=current
            if current<0:
                current=0
        return maxsum
        