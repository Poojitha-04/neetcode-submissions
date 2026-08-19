class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        res=[]
        count=nums.count(0)
        if count==0:
            for i in range(len(nums)):
                if nums[i]!=0:
                    prod=prod*nums[i]
                
            for i in range(len(nums)):
                if nums[i]!=0:
                    res.append(prod//nums[i])
                else:
                    res.append(0)
        elif count>=2:
            return [0]*len(nums)
        else:
            for i in range(len(nums)):
                if nums[i]!=0:
                    prod=prod*nums[i]
            for i in range(len(nums)):
                if nums[i]==0:
                    res.append(prod)
                else:
                    res.append(0)
            
        
        return res
        

            
        