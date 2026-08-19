class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        d1=sorted(d.items(),key=lambda x:x[1],reverse=True)
        return [i[0]for i in d1[:k]]




        
       
        

       
        

       