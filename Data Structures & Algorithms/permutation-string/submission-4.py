class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i,j=0,len(s1)
        print(len(s1))
        
        while j<=len(s2):
            print(s1[i:j],s2[i:j],i)
            if sorted(s1)==sorted(s2[i:j]):
                return True
            else :
                i=i+1
                j=i+len(s1)
        return False
        