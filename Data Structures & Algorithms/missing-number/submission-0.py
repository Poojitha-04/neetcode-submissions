class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sums=0
        n=len(nums)
        total=n*(n+1)/2

        for i in range(len(nums)):
            sums+=nums[i]

        return int(total-sums)
            

           
               

        