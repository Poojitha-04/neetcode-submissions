class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        di1={}
        di2={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            di1[s[i]]=di1.get(s[i],0)+1
            di2[t[i]]=di2.get(t[i],0)+1
        print(di1)
        print(di2)
        for i in range(len(s)):
            if di1.get(s[i])!=di2.get(s[i]):
                return False
        return True