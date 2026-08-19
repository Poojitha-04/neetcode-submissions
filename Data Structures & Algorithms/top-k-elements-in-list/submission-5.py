class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        sorted_items = sorted(d.items(), key=lambda x: x[1],reverse=True)
        sorted_items=sorted_items[:k]
        for i in sorted_items:
            l.append(i[0])
        return l
        

       