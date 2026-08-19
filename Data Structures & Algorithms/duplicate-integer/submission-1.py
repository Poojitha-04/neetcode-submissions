class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        vals=list(d.values())
        print(vals)
        for val in vals:
           if val>=2:
                return True
        return False

    
         