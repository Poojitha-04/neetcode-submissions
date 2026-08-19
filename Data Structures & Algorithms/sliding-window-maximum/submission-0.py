class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        res=[]
        while i<len(nums) and len(nums[i:i+k])==k:
            print(nums[i:i+k])
            res.append(max(nums[i:i+k]))
        
            i+=1
        return res
        