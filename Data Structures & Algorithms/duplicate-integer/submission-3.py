class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
       
        if any(v > 1 for v in d.values()):
            return True
        return False
        
   

        
    
         