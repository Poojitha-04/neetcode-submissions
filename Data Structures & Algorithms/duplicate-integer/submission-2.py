class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in range (len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        l=list(d.values())
        for i in range(len(l)):
            if l[i]>=2:
                return True
        return False
       
    
         