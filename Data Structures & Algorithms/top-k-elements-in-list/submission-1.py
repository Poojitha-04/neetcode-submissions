class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di={}
        l=[]
        l_new=[]
        for i in nums:
            di[i]=di.get(i,0)+1
        l=list(di.items())#[(1,1),(2,2),(3,3)]
        print(l)

        l.sort(key=lambda x:x[1])#[(1,1),(2,2),(3,3)]
        print(l)
        l.reverse()#[(3,3),(2,2),(1,1)]
        l=l[:k]#[(3,3),(2,2)]
        for i in l:
            l_new.append(i[0])
        return l_new
        
        