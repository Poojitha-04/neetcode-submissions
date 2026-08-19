class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l1=[]
        count=1
        maxi=0
        if len(nums)==0:
            return 0
        l1=sorted(set(nums))
        print(l1)
        l1=list(l1)
        print(l1)
        for i in range(len(l1)-1):
            if l1[i]+1==l1[i+1]:
                count+=1
                maxi=max(maxi,count)
            else:
                count=1
        return max(maxi,count)
    
        
        
        