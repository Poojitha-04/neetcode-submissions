class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        count=nums.count(val)
        i=0
        while i<len(nums):
            if nums[i]==val:
                i=i+count
                l=len(nums[i:])
                nums[i-count:i+l]=nums[i:]
            else:
                i+=1
       
        return len(nums)
      
        