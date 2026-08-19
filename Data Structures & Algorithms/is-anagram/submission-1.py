class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        d1={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in t:
            d1[i]=d1.get(i,0)+1
        if d==d1:
            return True
        return False

        
        