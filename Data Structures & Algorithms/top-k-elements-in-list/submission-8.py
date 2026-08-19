class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        sorted_items=sorted(d.items(),key=lambda x:x[1],reverse=True)
        for i in sorted_items:
            l.append(i[0])
        return list(l[:k])
       
        

       
        

       