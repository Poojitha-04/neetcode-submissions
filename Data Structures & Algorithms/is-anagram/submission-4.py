class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sd,td={},{}
        for i in s:
            sd[i]=sd.get(i,0)+1
        for i in t:
            td[i]=td.get(i,0)+1
        for i in s:
            if i not in t:
                return False
            if sd.get(i)!=td.get(i):
                return False
        return True


       

        