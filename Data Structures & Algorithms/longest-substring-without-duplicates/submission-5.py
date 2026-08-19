class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p=[]
        if len(s)<=1:
            return len(s)
        i,j=0,1
        while j<len(s):
            if s[j] not in s[i:j]:
                j+=1
            else:
                p.append(s[i:j])
                i+=1
                j=i+1
        if s[i:j] not in p:
            p.append(s[i:j])
        s=max(p,key=len)
        return len(s)

       
            
        
       

        