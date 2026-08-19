class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        prod=1
        count=nums.count(0)
        if count==0:
            for i in range(len(nums)):
                prod=prod*nums[i]
            for i in range(len(nums)):
                l.append(prod//nums[i])
        elif count==1:
            for i in range(len(nums)):
                if nums[i]!=0:
                    prod=prod*nums[i]
                else:
                    continue
            for i in range(len(nums)):
                if nums[i]!=0:
                    l.append (0)
                else:
                    l.append(prod)
        else:
            for i in range(len(nums)):
                l.append(0)
        return l


        
            



        

        
                
        

        