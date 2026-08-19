class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        di={}
        a=[]
        for i in range(len(nums)):
            di[nums[i]]=di.get(nums[i],0)+1
        a= di.values()
        a=list(a)
        for i in range(len(a)):
            if a[i]>1:
                return True
        return False
            

         