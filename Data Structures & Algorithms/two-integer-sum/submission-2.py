class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            temp=target-nums[i]
            if d.get(temp,-1)!=-1 and d.get(temp)!=i:
                return[i,d.get(temp)]
        
       

        
       


        