class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        prod=1
        count=nums.count(0)
        if count>1:
            return [0]*len(nums)
        else:
            for i in range(len(nums)):
                if nums[i]!=0:
                    prod*=nums[i]
            
            for i in range(len(nums)): 
                if 0 in nums:
                    if nums[i]!=0:
                        l.append(0)
                    else:
                        l.append(int(prod))
                else :
                    l.append(int(prod/nums[i]))
            return l
            



        

        
                
        

        